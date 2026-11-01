#!/usr/bin/env python3
"""Read-only checks for Markdown structure and AINotes navigation."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


def lint(root: Path) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    issues: list[str] = []
    parsed: dict[Path, tuple[str, str, set[str]]] = {}
    required = ("README.md", "AGENTS.md", "wiki/index.md", "wiki/log.md", "docs/技术方案.md")
    for relative in required:
        if not (root / relative).is_file():
            issues.append(f"缺少维护文件：{relative}")

    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if any(part in {".git", ".venv", "node_modules"} for part in relative.parts):
            continue
        text = path.read_text(encoding="utf-8")
        visible: list[str] = []
        fence = ""
        table_width: int | None = None
        math_open = False
        for line_no, line in enumerate(text.splitlines(), 1):
            marker = re.match(r"^\s*(`{3,}|~{3,})", line)
            if marker:
                token = marker[1]
                if not fence:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = ""
                visible.append("")
                table_width = None
                continue
            if fence:
                visible.append("")
                continue
            visible.append(line)
            if line.strip() == "$$":
                math_open = not math_open
            if re.match(r"^(<<<<<<<|=======|>>>>>>>)", line):
                issues.append(f"{relative}:{line_no}：存在冲突标记")
            if line.lstrip().startswith("|"):
                width = len(re.findall(r"(?<!\\)\|", line))
                if table_width is not None and width != table_width:
                    issues.append(f"{relative}:{line_no}：表格列数不一致")
                table_width = width
            else:
                table_width = None
        if fence:
            issues.append(f"{relative}：代码块未闭合")
        if math_open:
            issues.append(f"{relative}：公式块未闭合")

        body = "\n".join(visible)
        explicit = re.findall(r'<a\s+(?:id|name)="([^"]+)"', body)
        for anchor, count in Counter(explicit).items():
            if count > 1:
                issues.append(f"{relative}：重复锚点 {anchor}")
        anchors = set(explicit)
        heading_counts: Counter[str] = Counter()
        for heading in re.findall(r"^#{1,6}\s+(.+)$", body, re.M):
            heading = re.sub(r"<[^>]+>", "", heading)
            slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
            occurrence = heading_counts[slug]
            anchors.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
            heading_counts[slug] += 1
        parsed[path] = (text, body, anchors)

    for path, (_, body, _) in parsed.items():
        for raw in re.findall(r"!?\[[^\]\n]*\]\(([^\)\n]+)\)", body):
            target = raw.strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            parts = urlsplit(target)
            if parts.scheme or parts.netloc:
                continue
            relative = path.relative_to(root)
            destination = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not destination.is_relative_to(root):
                issues.append(f"{relative}：本地链接超出仓库范围 {target}")
                continue
            if not destination.exists():
                issues.append(f"{relative}：链接目标不存在 {target}")
                continue
            fragment = unquote(parts.fragment)
            if fragment and destination in parsed and fragment not in parsed[destination][2]:
                issues.append(f"{relative}：锚点不存在 {target}")

    notes = []
    for path, (text, body, _) in parsed.items():
        if not path.is_relative_to(root / "wiki") or path.name in {"index.md", "log.md"}:
            continue
        if "类型：原创学习笔记" not in text:
            continue
        notes.append(path)
        dates = []
        for field in ("首次整理", "最近更新"):
            match = re.search(field + r"：(\d{4}-\d{2}-\d{2})", text)
            try:
                value = date.fromisoformat(match[1]) if match else None
            except ValueError:
                value = None
            if value is None:
                issues.append(f"{path.relative_to(root)}：缺少或无效的 {field} 日期")
            else:
                dates.append(value)
        if len(dates) == 2 and dates[1] < dates[0]:
            issues.append(f"{path.relative_to(root)}：更新时间早于创建时间")
        for field in ("来源：", "标签："):
            if not re.search(re.escape(field) + r"\S+", text):
                issues.append(f"{path.relative_to(root)}：缺少 {field}")
        numbers = re.findall(r"^### Q(\d+)\.", body, re.M)
        if numbers != [str(i) for i in range(1, len(numbers) + 1)]:
            issues.append(f"{path.relative_to(root)}：QA 编号不连续")

    readme = parsed.get(root / "README.md", ("", "", set()))[0]
    index = parsed.get(root / "wiki/index.md", ("", "", set()))[0]
    count = re.search(r"全部笔记（(\d+) 篇", readme)
    if not count or int(count[1]) != len(notes):
        issues.append("README 笔记总数与实际原创笔记数量不一致")
    diagrams = 0
    qa = 0
    for path in notes:
        text, body, _ = parsed[path]
        relative = path.relative_to(root).as_posix()
        readme_rows = [line for line in readme.splitlines() if f"]({relative})" in line]
        if len(readme_rows) != 1:
            issues.append(f"README 全部笔记表需恰有一条正文入口：{relative}")
            continue
        row = readme_rows[0]
        chapters = len(re.findall(r"^## \d+\.", body, re.M))
        questions = len(re.findall(r"^### Q\d+\.", body, re.M))
        figures = len(re.findall(r"^```mermaid\s*$", text, re.M))
        qa += questions
        diagrams += figures
        scale = f"{chapters} 章、{questions} 个复习问答、{figures} 张流程图"
        if scale not in row:
            issues.append(f"README 内容规模需更新为：{scale}")
        updated = re.search(r"最近更新：(\d{4}-\d{2}-\d{2})", text)
        if updated and updated[1] not in row:
            issues.append(f"README 更新时间与正文不一致：{relative}")
        from_index = path.relative_to(root / "wiki").as_posix()
        if f"]({from_index})" not in index:
            issues.append(f"知识索引缺少正文入口：{relative}")

    return issues, {"Markdown 文件": len(parsed), "知识笔记": len(notes), "复习问答": qa, "流程图": diagrams}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    issues, counts = lint(args.root)
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        return 1
    print("校验通过：" + "，".join(f"{key} {value}" for key, value in counts.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
