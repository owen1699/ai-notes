# AINotes · AI 学习笔记

将学习对话整理成可以反复复习的知识：按概念依赖组织，保留专业术语、公式、例子、流程图与问答，并持续修正容易混淆的边界。

- [知识索引](wiki/index.md)：先按问题定位，再进入章节阅读。
- [变更日志](wiki/log.md)：按时间追加本次学到什么、改了什么。
- [维护约定](AGENTS.md)：任何 AI 工具维护本库前先读。
- [技术方案](docs/技术方案.md)：目录职责、知识组织与演进决策。

## 全部笔记（4 篇，按最近更新倒序）

| 更新 | 创建 | 标题 | 类型 | 标签 | 内容规模 |
| --- | --- | --- | --- | --- | --- |
| 2026-11-08 | 2026-11-02 | [Agent 与 MCP 接入原理](wiki/2026-11-02-Agent与MCP接入原理.md) | 原创学习笔记 | Agent、MCP、CLI、stdio、IPC、Streamable HTTP、JSON-RPC、Claude Code、发现缓存、工具搜索、上下文管理、OAuth | 13 章、56 个复习问答、8 张流程图 |
| 2026-11-08 | 2026-11-08 | [MCP 官方协议中文版指南：2026-07-28 正式版](wiki/2026-11-08-MCP官方协议中文版指南.md) | 原创学习笔记（官方译述） | MCP、JSON-RPC、MRTR、OAuth、Elicitation、Apps、Tasks、Skills、Registry | 10 章、12 个复习问答、3 张流程图 |
| 2026-11-08 | 2026-11-01 | [大模型学习笔记：从参数、注意力到完整推理流程](wiki/2026-11-01-大模型基础学习笔记.md) | 原创学习笔记 | Transformer、分词器、Embedding、Logits、Softmax、参数、神经元、激活函数、反向传播、张量、MoE、FP8、量化、模型包、FFN、推理、BERT、搜索 | 18 章、121 个复习问答、15 张流程图 |
| 2026-11-05 | 2026-11-04 | [RAG 检索原理与工程实践](wiki/2026-11-04-RAG检索原理与工程实践.md) | 原创学习笔记 | RAG、分词、倒排索引、BM25、语义检索、K-means、IVF、PQ、HNSW、ES、Redis | 14 章、36 个复习问答、2 张流程图 |

正文只维护一份；旧目录中的阅读入口不计为第二篇笔记。当前原始资料全文归档为 0 篇，论文与官方文档以正文引用链接追溯。

## 本轮新增

### HTTP、JSON-RPC 分层与 Claude Code 完整案例

2026-11-08，继续融入既有《Agent 与 MCP 接入原理》，补齐 [HTTP 方法／RPC 方法／工具名](wiki/2026-11-02-Agent与MCP接入原理.md#http-rpc-method)、[多 URL 与服务端分发](wiki/2026-11-02-Agent与MCP接入原理.md#endpoint-dispatch)、[方法实现条件及规范入口](wiki/2026-11-02-Agent与MCP接入原理.md#method-contract)。区分[配置、能力目录、客户端和模型上下文](wiki/2026-11-02-Agent与MCP接入原理.md#catalog-state)，展开[探测触发](wiki/2026-11-02-Agent与MCP接入原理.md#discovery-timing)、[保存与缓存](wiki/2026-11-02-Agent与MCP接入原理.md#catalog-storage)、[能力更新](wiki/2026-11-02-Agent与MCP接入原理.md#catalog-refresh)、[工具与 skill 加载](wiki/2026-11-02-Agent与MCP接入原理.md#catalog-model)及[共享范围](wiki/2026-11-02-Agent与MCP接入原理.md#client-sharing)。

末尾新增[第 13 章完整案例](wiki/2026-11-02-Agent与MCP接入原理.md#claude-code-case)：从可运行的只读服务器、CLI 配置和冷/暖启动，到发现请求、目录保存、模型决策、HTTP 调用、结果回送、变更通知与退出恢复。保留请求/结果、状态表、流程图和[可运行示范 Host](wiki/2026-11-02-Agent与MCP接入原理.md#cc-host-code)，追加 Q31—Q56。

本地复核固定 Claude Code 2.1.319 / MCP Python SDK 2.3.0。真实 HTTP、CLI 健康检查和 SDK 调用与回放模型输出分别标注；交互式启动、磁盘缓存命中及通知刷新未实测，详见[验证边界](wiki/2026-11-02-Agent与MCP接入原理.md#cc-validation)。不新增重复笔记，官方协议中文版指南保持原样。

### MCP 最新正式版官方指南

2026-11-08，新建按官方 Documentation → Specification → Extensions → Registry 结构展开的中文指南，覆盖 78 个官网入口、完整核心类型与 128 个关联 JSON 示例，并追读官方天气、参考服务器、Inspector 和扩展示例。明确 2026-07-28 与旧版握手／SDK 的边界，标注官方材料差异及未执行的端到端验证。

直接阅读：[开发与 SDK](wiki/2026-11-08-MCP官方协议中文版指南.md#ch1) · [基础协议／MRTR／传输](wiki/2026-11-08-MCP官方协议中文版指南.md#ch3) · [授权与安全](wiki/2026-11-08-MCP官方协议中文版指南.md#ch4) · [客户端](wiki/2026-11-08-MCP官方协议中文版指南.md#ch5) · [服务端](wiki/2026-11-08-MCP官方协议中文版指南.md#ch6) · [扩展](wiki/2026-11-08-MCP官方协议中文版指南.md#ch7) · [Schema 示例](wiki/2026-11-08-MCP官方协议中文版指南.md#ch9) · [来源与验证边界](wiki/2026-11-08-MCP官方协议中文版指南.md#sources)。该次新增指南时，既有三篇笔记保持不变。

### 同日的大模型基础更新

2026-11-08，在原有大模型基础笔记中分别展开 **[Part 1：预训练](wiki/2026-11-01-大模型基础学习笔记.md#training-pipeline)** 与 **[Part 2：推理](wiki/2026-11-01-大模型基础学习笔记.md#sec8-5)**，用“法国的首都是巴黎。”串起目标构造、前向、损失／梯度／联合更新，以及 Prefill、Decode、缓存和停止。两张主图均单一起止、从上向下，回环分别进入下一批与新 Token。

本轮追问：[三种学习方式](wiki/2026-11-01-大模型基础学习笔记.md#sec1-18) · [Sigmoid 直觉与手算](wiki/2026-11-01-大模型基础学习笔记.md#sec2-11) · [词表／嵌入与权重绑定](wiki/2026-11-01-大模型基础学习笔记.md#sec3-9) · [Qwen3.5 词表扩展与容量选择](wiki/2026-11-01-大模型基础学习笔记.md#sec3-11) · [SwiGLU 的准确位置](wiki/2026-11-01-大模型基础学习笔记.md#sec5-10) · [全词表投影与 GPU 分块](wiki/2026-11-01-大模型基础学习笔记.md#sec6-13) · [0.61 MB、计算量与带宽](wiki/2026-11-01-大模型基础学习笔记.md#sec6-15)。保留远端已有 98 个问答，将重复主题融入对应解释，再新增 Q99—Q121，公式、术语和案例回链同步更新。

### 同日此前已收录的内容

此前一轮基于远端 `b37834cf` 对照去重，在既有正文内补齐尚未入库的阶段流程与 MCP 追问；以前已收录的激活函数、分词器和 RAG 内容继续保留。

- 两阶段流程：[预训练、标签移位与教师强制](wiki/2026-11-01-大模型基础学习笔记.md#training-pipeline) · [训练主流程与层依赖](wiki/2026-11-01-大模型基础学习笔记.md#training-flow) · [Prefill/Decode 完整循环](wiki/2026-11-01-大模型基础学习笔记.md#sec8-5)。
- 输出头追问：[全词表矩阵投影与贪心/采样](wiki/2026-11-01-大模型基础学习笔记.md#vocabulary-projection) · [并行计算与成本](wiki/2026-11-01-大模型基础学习笔记.md#sec6-14) · [0.61 MB 的前提与算式](wiki/2026-11-01-大模型基础学习笔记.md#logits-memory)。
- MCP 深入：[stdio/HTTP/普通 HTTP 比较](wiki/2026-11-02-Agent与MCP接入原理.md#transport-comparison) · [协议版本分界](wiki/2026-11-02-Agent与MCP接入原理.md#mcp-versioning) · [标准流与 IPC](wiki/2026-11-02-Agent与MCP接入原理.md#stdio-ipc) · [CLI 包装](wiki/2026-11-02-Agent与MCP接入原理.md#cli-wrapper)。
- Agent 工具生命周期：[四步发现](wiki/2026-11-02-Agent与MCP接入原理.md#discovery-stages) · [选择、执行与结果时序](wiki/2026-11-02-Agent与MCP接入原理.md#tool-decision) · [六类“卸载”对象](wiki/2026-11-02-Agent与MCP接入原理.md#mcp-unload)。

此前该轮追加 32 个复习问答；各项原问题到正文的对应关系见[模型流程追问表](wiki/2026-11-01-大模型基础学习笔记.md#incremental-question-map)和[MCP 追问表](wiki/2026-11-02-Agent与MCP接入原理.md#mcp-question-map)。

### 既有专题入口

大模型基础追问：[激活函数为何必要与舒适度反例](wiki/2026-11-01-大模型基础学习笔记.md#sec2-10) · [分词器训练与复用](wiki/2026-11-01-大模型基础学习笔记.md#sec3-6) · [不同分词器的区别](wiki/2026-11-01-大模型基础学习笔记.md#sec3-7) · [陌生词、字节回退与向量查表](wiki/2026-11-01-大模型基础学习笔记.md#sec3-8)。

新增类比：[K-means 的 K 个中心与 Transformer 的 H 个头](wiki/2026-11-04-RAG检索原理与工程实践.md#kmeans-attention)，区分结构超参数、可学习参数、均值更新、反向传播和头内权重归一化。

RAG 追问补充：[KNN／范围／ANN 的概念分层](wiki/2026-11-04-RAG检索原理与工程实践.md#vector-taxonomy) · [FLAT／IVF／HNSW／PQ 对比](wiki/2026-11-04-RAG检索原理与工程实践.md#ann-methods) · [K-means 手算](wiki/2026-11-04-RAG检索原理与工程实践.md#kmeans) · [IVF 参数与 PQ 压缩](wiki/2026-11-04-RAG检索原理与工程实践.md#ivf-pq) · [Redis KNN 参数语义](wiki/2026-11-04-RAG检索原理与工程实践.md#redis-knn-syntax) · [范围召回与分页](wiki/2026-11-04-RAG检索原理与工程实践.md#redis-vector-range) · [查询能力与融合](wiki/2026-11-04-RAG检索原理与工程实践.md#redis-query-capabilities)。

大模型基础新增：[Logits 与输出形状](wiki/2026-11-01-大模型基础学习笔记.md#sec6-7) · [0 分为什么仍约 9%](wiki/2026-11-01-大模型基础学习笔记.md#sec6-8) · [为什么取指数、用 e](wiki/2026-11-01-大模型基础学习笔记.md#sec6-9) · [分数差与概率比](wiki/2026-11-01-大模型基础学习笔记.md#sec6-10) · [交叉熵与生成](wiki/2026-11-01-大模型基础学习笔记.md#sec6-11) · [稳定计算与 Python 复现](wiki/2026-11-01-大模型基础学习笔记.md#sec6-12)。

RAG 专题新增：[完整链路](wiki/2026-11-04-RAG检索原理与工程实践.md#pipeline) · [两类分词器与训练](wiki/2026-11-04-RAG检索原理与工程实践.md#tokenization) · [BM25 公式与手算](wiki/2026-11-04-RAG检索原理与工程实践.md#bm25) · [向量化](wiki/2026-11-04-RAG检索原理与工程实践.md#embedding) · [语义检索方案](wiki/2026-11-04-RAG检索原理与工程实践.md#semantic-retrieval) · [过滤、融合与重排](wiki/2026-11-04-RAG检索原理与工程实践.md#hybrid) · [Redis Search 分工](wiki/2026-11-04-RAG检索原理与工程实践.md#redis-search) · [故障与评测](wiki/2026-11-04-RAG检索原理与工程实践.md#evaluation)。

Agent 专题新增：[角色与进程](wiki/2026-11-02-Agent与MCP接入原理.md#roles) · [Gmail 例子](wiki/2026-11-02-Agent与MCP接入原理.md#gmail) · [生财有术例子](wiki/2026-11-02-Agent与MCP接入原理.md#shengcai) · [URL 直连](wiki/2026-11-02-Agent与MCP接入原理.md#url) · [command 本地服务](wiki/2026-11-02-Agent与MCP接入原理.md#stdio) · [utoo-proxy 双角色](wiki/2026-11-02-Agent与MCP接入原理.md#proxy) · [完整调用循环](wiki/2026-11-02-Agent与MCP接入原理.md#runtime)。

| 想解决的问题 | 直接阅读 |
| --- | --- |
| 预训练与推理怎样分别走完端到端流程？ | [Part 1：预训练](wiki/2026-11-01-大模型基础学习笔记.md#training-pipeline) · [Part 2：推理](wiki/2026-11-01-大模型基础学习笔记.md#sec8-5) |
| 词表、Embedding、输出头分别是什么，是否共享与联合训练？ | [资产与训练依赖](wiki/2026-11-01-大模型基础学习笔记.md#sec3-9) · [实际共享配置](wiki/2026-11-01-大模型基础学习笔记.md#sec3-10) |
| 词表越大代表知识越多吗，Qwen3.5 为什么扩大？ | [覆盖与编码效率](wiki/2026-11-01-大模型基础学习笔记.md#sec3-11) · [容量怎样设计](wiki/2026-11-01-大模型基础学习笔记.md#sec3-12) |
| Sigmoid、SiLU、SwiGLU 怎样计算，放在模型哪里？ | [S 形函数与导数](wiki/2026-11-01-大模型基础学习笔记.md#sec2-11) · [块内位置与门控乘法](wiki/2026-11-01-大模型基础学习笔记.md#sec5-10) |
| 每步全词表打分怎样并行，0.61 MB 又怎样算？ | [投影与分块](wiki/2026-11-01-大模型基础学习笔记.md#sec6-13) · [容量、带宽和优化](wiki/2026-11-01-大模型基础学习笔记.md#sec6-15) |
| 训练的批次循环、层循环与生成循环怎样区分？ | [训练完整流程](wiki/2026-11-01-大模型基础学习笔记.md#training-flow) · [推理完整流程](wiki/2026-11-01-大模型基础学习笔记.md#sec8-5) |
| 每次都要算全部词表分数吗，0.61 MB 怎样计算？ | [输出矩阵与选词](wiki/2026-11-01-大模型基础学习笔记.md#vocabulary-projection) · [空间手算](wiki/2026-11-01-大模型基础学习笔记.md#logits-memory) |
| MCP 是如何通过标准流或 HTTP 把 CLI 能力交给模型的？ | [CLI 包装](wiki/2026-11-02-Agent与MCP接入原理.md#cli-wrapper) · [完整时序](wiki/2026-11-02-Agent与MCP接入原理.md#tool-decision) |
| “卸载工具”是压缩历史还是关掉服务？ | [工具、历史、连接、进程、配置与授权](wiki/2026-11-02-Agent与MCP接入原理.md#mcp-unload) |
| 为什么需要激活函数，多堆几层乘加还不够吗？ | [表示不了的目标与 ReLU 构造](wiki/2026-11-01-大模型基础学习笔记.md#sec2-10) |
| 分词器可以复用吗？分词训练和向量学习有何区别？ | [训练阶段与资产分工](wiki/2026-11-01-大模型基础学习笔记.md#sec3-6) |
| 模型碰到陌生词，怎样切分并得到向量？ | [分词器差异](wiki/2026-11-01-大模型基础学习笔记.md#sec3-7) · [切分、字节兜底与查表](wiki/2026-11-01-大模型基础学习笔记.md#sec3-8) |
| KNN、范围查询、ANN 与 K-means 哪些可以对标？ | [概念分层](wiki/2026-11-04-RAG检索原理与工程实践.md#vector-taxonomy) · [索引方案](wiki/2026-11-04-RAG检索原理与工程实践.md#ann-methods) |
| K-means 怎样迭代，nlist、nprobe、top-k 有何区别？ | [六点手算](wiki/2026-11-04-RAG检索原理与工程实践.md#kmeans) · [IVF 与 PQ](wiki/2026-11-04-RAG检索原理与工程实践.md#ivf-pq) |
| Redis 的 $vector AS distance、范围查询和混合检索如何理解？ | [KNN 语法](wiki/2026-11-04-RAG检索原理与工程实践.md#redis-knn-syntax) · [范围查询](wiki/2026-11-04-RAG检索原理与工程实践.md#redis-vector-range) · [过滤与融合](wiki/2026-11-04-RAG检索原理与工程实践.md#redis-filter-fusion) |
| Logits 怎样变成概率，为什么 0 分仍有概率？ | [分数与形状](wiki/2026-11-01-大模型基础学习笔记.md#sec6-7) · [Softmax 手算](wiki/2026-11-01-大模型基础学习笔记.md#sec6-8) |
| Softmax 为什么取指数、用 e，分差与概率比有什么关系？ | [指数及底数选择](wiki/2026-11-01-大模型基础学习笔记.md#sec6-9) · [分差与平移](wiki/2026-11-01-大模型基础学习笔记.md#sec6-10) |
| 超参数与可学习参数有什么区别？ | [超参数](wiki/2026-11-01-大模型基础学习笔记.md#sec1-7) |
| 一个神经元怎样计算？偏置起什么作用？ | [神经元](wiki/2026-11-01-大模型基础学习笔记.md#sec1-8) · [偏置](wiki/2026-11-01-大模型基础学习笔记.md#sec1-9) |
| 神经元与层怎样对应，为什么 7 个单元会有 29 个参数？ | [连接与计数](wiki/2026-11-01-大模型基础学习笔记.md#sec1-13) · [Transformer 统计口径](wiki/2026-11-01-大模型基础学习笔记.md#sec1-14) |
| 前馈、前向计算、反向传播与优化器怎样分工？ | [职责分工](wiki/2026-11-01-大模型基础学习笔记.md#sec5-7) · [一次训练手算](wiki/2026-11-01-大模型基础学习笔记.md#sec5-8) |
| 激活函数与偏置怎样共同影响一个单元？响应位置如何学习？ | [超过 8 小时的例子与非线性](wiki/2026-11-01-大模型基础学习笔记.md#sec2-9) · [偏置梯度](wiki/2026-11-01-大模型基础学习笔记.md#sec5-9) |
| 量化为什么能省空间？是否减少参数数量？ | [量化、PTQ 与 QAT](wiki/2026-11-01-大模型基础学习笔记.md#sec1-10) |
| 张量的轴、形状与向量维度是什么关系？ | [张量 Tensor](wiki/2026-11-01-大模型基础学习笔记.md#sec3-5) |
| 残差为什么加回输入？FFN 做什么？ | [残差连接](wiki/2026-11-01-大模型基础学习笔记.md#sec5-3) · [前馈网络](wiki/2026-11-01-大模型基础学习笔记.md#sec5-6) |
| 一个词元为何只调用部分专家？33 亿为什么不能直接乘 16？ | [MoE 路由](wiki/2026-11-01-大模型基础学习笔记.md#sec2-5) · [Qwen 参数拆分](wiki/2026-11-01-大模型基础学习笔记.md#sec2-7) |
| 模型结构代码是什么？如何选层数、头数和维度？ | [结构代码](wiki/2026-11-01-大模型基础学习笔记.md#architecture-code) · [架构设计](wiki/2026-11-01-大模型基础学习笔记.md#architecture-design) |
| FP32、FP16、BF16、FP8 有何区别？怎样转换与另存？ | [精度与量化](wiki/2026-11-01-大模型基础学习笔记.md#precision-quantization) |
| 量化文件小，是否运行内存也一定小？ | [保存、加载、常驻与峰值](wiki/2026-11-01-大模型基础学习笔记.md#sec-precision-9) |
| HF 模型包每个文件有什么用，如何加载和检查权重？ | [真实模型包](wiki/2026-11-01-大模型基础学习笔记.md#hf-package) |

## 建议阅读顺序

1. 两条端到端主线：先读 Part 1 预训练和 Part 2 推理，区分学习参数与使用参数。
2. 参数与训练：区分架构配置、可学习参数、数值表示和推理时的状态。
3. Transformer 内部计算：理解张量、Token、嵌入、QKV、注意力、多头、多层与 FFN。
4. 完整生成流程：从输出头选 Token，到 Prefill、Decode 与 KV Cache。
5. 模型工程：读结构代码，理解架构取舍、文件大小、浮点精度与量化。
6. 发布模型：对照 Qwen 的配置、权重、分词器与加载示例。
7. 模型应用：理解 BERT、FinBERT、BioBERT、搜索排序与 M6。
8. 复习巩固：按问答归档、公式速查、术语表和分组自测检查理解。

## 目录职责与维护

| 路径 | 用途 |
| --- | --- |
| `wiki/` | 持续维护的知识笔记、知识索引与追加日志 |
| `docs/` | 管理方案与决策记录 |
| `scripts/lint.py` | 检查链接、锚点、笔记元信息和内容计数 |
| `AGENTS.md` | 维护规则与工作流 |
| `大模型基础/` | 已发布旧链接的兼容入口 |

目录按实际内容增长；有需要归档且获许可的原始材料时，再建立 `sources/`，有本地图片时再建立 `assets/`。知识笔记与原始材料分开管理，参考来源保留原始链接。

本地校验：`python3 scripts/lint.py`。正文、索引、首页和日志在同一次提交中更新。

公式使用 LaTeX，流程图使用 Mermaid；GitHub 可直接阅读。教学用数字不代表真实模型内部权重；参数规模、许可及产品信息均需结合具体版本与核对日期理解。
