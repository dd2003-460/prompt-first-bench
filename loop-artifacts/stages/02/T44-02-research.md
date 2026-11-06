# T44 · Related Work Update (Nov 2026) — 阶段 02：资料搜集（research.md）

> 创建时间：2026-11-06 UTC · 阶段：02（信息调研）
> 规则包：`loop/prompt-first/00-common-review.md` + `02-information-research.md` + `02.5-cross-check.md`
> 上游输入：`loop-artifacts/stages/01/T44-01-goal-decomposition.md`（空缺 G1–G7，冻结域 D1–D5，排除规则 E-dup / E-noid / E-time）
> **阶段边界声明**：本阶段严格围绕 G1–G6 收集公开一手题录证据、双源回执、核心实证观察与未决差异；**不在此阶段写最终 §2 推荐修改段落**（留待阶段 03/04）。所有观察时间戳均为本会话真实工具调用时间（2026-11-06T08:53Z–08:59Z UTC）。

---

## 0. 检索通道实测回执（含不可用通道登记）

| 通道编号 | 工具 / 目标接口 | 调用次数 | 状态与回执摘要 | 观察时间 (UTC) | 处置 |
|---------|----------------|---------|---------------|---------------|------|
| C1 | `ego-browser` + `ego-verify`（网页 LLM 交叉询问） | 0（环境探测） | **不可用**：Arena Agent Mode 沙箱未安装 `ego-browser` 与 `ralph` CLI，且 bash 外网仅白名单放通 `github.com` / `npmjs.org` / `pypi.org` | 2026-11-06T08:47Z | 按 `02-information-research.md` 规则第 2 条快速记录原因，不等待不重试，切换至平台原生公开学术检索工具 |
| C2 | `fetch_page` → arXiv 官方 Atom API (`export.arxiv.org/api/query`) | 4 批（共核验 31 个 ID，含 3 个既有 ID + 28 个候选/去重） | **HTTP 200 全部成功**，完整返回官方 `<entry>`（精确标题、全部作者、v1/v2/v3 提交时间戳、摘要、venue comment、DOI） | 2026-11-06T08:53:28Z – 08:56:26Z | **独立主源 A**（100% 覆盖全部入选 arXiv 文献） |
| C3 | `fetch_page` → DBLP Publication API (`dblp.org/search/publ/api?format=json`) | 16 次 | **HTTP 200**；2026-07~09 文献命中 CoRR 或正式会议/期刊条目（含 TMLR 2026、EMNLP 2026 Main）；2026-10 中下旬新挂预印本因 DBLP CoRR 批处理滞后约 2–3 周返回 `hits=0` | 2026-11-06T08:56Z – 08:58Z | **独立次源 B1**（覆盖 10 篇 2026-07~09 文献） |
| C4 | `fetch_page` / `web_search` → ACL Anthology (`aclanthology.org`) | 3 次 | **HTTP 200**，实取 EMNLP 2026 Findings (`2026.findings-emnlp.1571`)、AACL-IJCNLP 2026 Main (`2026.aacl-long.207`)、EMNLP 2026 W-NUT (`2026.wnut-1.7`)、EMNLP 2026 Main (`2026.emnlp-main.389`) 官方页码与 DOI | 2026-11-06T08:58Z – 08:59Z | **独立一手出版源 B2**（同行评审正式会议录） |
| C5 | `web_search` → 外部独立索引与官方项目仓库（GitHub / PapersWithCode / ResearchGate / AwesomePapers） | 19 次 | **成功**，用于候选发现及 2026-10 中下旬尚未入库 DBLP 的 5 篇最新预印本的独立外部存在性印证 | 2026-11-06T08:53Z – 08:59Z | **独立次源 B3**（注明预印本外部聚合索引属性） |

**源独立性准则**：`arxiv.org/abs/*` 网页与 `export.arxiv.org/api/query` 同属康奈尔 arXiv 后端，本文件**绝不**将二者算作双源；每篇文献的第二源均来自不同机构（DBLP 德国达戈斯图尔 / ACL Anthology 国际计算语言学学会 / OpenReview / GitHub 作者独立代码仓 / ResearchGate / PapersWithCode）。

---

## 1. 既有 2026-09 引用顺带核查回执（闭合 G5 子问题 2）

对 `experiments/stage-ablation/paper-draft.md` 现有 References 中仅有的 3 篇 `2609.*` 条目调用 `export.arxiv.org/api/query?id_list=2609.19644,2609.20541,2609.34454`（观察时间 `2026-11-06T08:53:28Z`）：
1. **`arXiv:2609.19644`（原稿 Ref #6）**：真实存在（v1 `2026-09-17T03:37:42Z`，作者 Jaehyun Nam, Jinsung Yoon, Yanzhou Pan, Yubo Wang, Rui Meng, Parthasarathy Ranganathan, Tomas Pfister）。**发现细微题录偏差**：arXiv 真实标题为 *"ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI"*，而 `paper-draft.md` Ref #6 误写副标题为 *"ScientistTwo: An Autonomous Multi-Agent Framework for Scientific Discovery"*。将在阶段 04 建议修改中顺带提示修正。
2. **`arXiv:2609.20541`（原稿 Ref #22）**：真实存在（v1 `2026-09-17T15:10:28Z`，Lukas Meyer, Sofia Rossi, Wei Chen, Thomas Laurent, Yiming Li，标题与摘要数字 AUROC 0.956/0.937 vs 0.765/0.790 完全一致）。
3. **`arXiv:2609.34454`（原稿 Ref #23）**：真实存在（v1 `2026-09-28T07:12:49Z`，Yekun Xu, Ante Wang, Jingyi Ren, Xuanyi Chen, Weizhi Ma, Yang Liu，标题 *"When Words Fall Short: Iterative Synergy Between Verbalized Reasoning and Hidden Features for LLM Confidence Estimation"* 完全一致）。

上述 3 篇按冻结规则 **E-dup** 排除在本次新增计数之外。

---

## 2. 五大方向新增 2026 H2 文献证据表（共 16 篇候选全部通过一手核验）

### 2.1 方向 D1：LLM Agent Benchmarks 2026 H2（对应空缺 G1，3 篇）

#### [N01] AgentHop（2026-09 / v2 2026-11 · NeurIPS 2026 Evaluations & Datasets Track）
- **标题**：*AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Question Answering over Scientific Citation Graphs*（注：v1 与 DBLP 标题为 *AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Scientific Question Answering*，见阶段 02.5 版本漂移核对）
- **作者**：Chanhee Park, Jeongho Yoon, Sungbin Han, Hyeonseok Moon, Heuiseok Lim
- **标识符**：`arXiv:2609.34428`（`DOI: 10.48550/arXiv.2609.34428`）
- **发表/提交时间**：v1 `2026-09-28T06:45:01Z`；v2 `2026-11-02T03:48:35Z`；arXiv comment: *"Accepted to NeurIPS 2026 Evaluations and Datasets Track"*
- **双源回执**：源 A = arXiv API (`08:56:04Z`)；源 B = DBLP `journals/corr/abs-2609-34428` (`08:56Z`)
- **具体观察**：包含 1,011 道多跳科学问答与受控 7 工具沙箱（固定 token/turn/tool-call 预算）。批评既有基准仅给单一总分，提出沿 **4 个正交运行轴（retrieval, synthesis, tool-call, resource management）** 诊断 19 个模型，发现显著的**模型家族行为指纹**（GPT 提早提交、Anthropic/GLM 提交前核验、DeepSeek/Kimi 过度搜索；Claude Opus 4.6 与 Sonnet 4.6 总分仅差 1 分但在检索 vs 综合上显著分化）。
- **设定分类暂判**：相关但不同设定（有 7 工具沙箱；多维诊断思路与本文 7 维 rubric 同向）。`conf: 0.95`

#### [N02] CXBench（2026-10）
- **标题**：*CXBench: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows*
- **作者**：Boxi Yu, Yuzhong Zhang, Zhenfeng Su, Linfu Xi, Yinghan Yao, Shitao Chen, Yang Cao, Lin Liting (Liting Lin), Lionel Briand, Emir Muñoz
- **标识符**：`arXiv:2610.25954`（`DOI: 10.48550/arXiv.2610.25954`）
- **发表/提交时间**：v1 `2026-10-19T07:46:04Z`
- **双源回执**：源 A = arXiv API (`08:56:04Z`)；源 B = 官方项目站 `https://cxbench.github.io/` 及 GitHub `CXBench/cxbench.github.io` (`08:59Z`)（注：因 10 月 19 日提交，DBLP CoRR 尚未入库）
- **具体观察**：横跨 6 个受监管领域、120 个任务、7 个模型（840 次保留执行），将**结果正确性（outcome pass）**与**过程合规性（process compliance）**分离评估，采用确定性规则校验 + LLM 裁判混合评分。发现 **80.1% 的结果通过运行实为过程违规的「假通过」（false-pass，占全量运行的 55.5%，双通过仅 13.8%）**，且纳入过程评测会改变模型排名。
- **设定分类暂判**：相关但不同设定（含工具环境；混合确定性门禁 + LLM 裁判与本文 `gates.py` + M1–M7 架构同构）。`conf: 0.90`

#### [N03] Backtrader-Bench（2026-07/08 · IJCAI 2026 FinLLM Workshop）
- **标题**：*Backtrader-Bench: Benchmarking LLM Agents on Algorithmic Trading with Self-Generated MCQs*
- **作者**：Ruoxi Zhao, Maziar Raissi
- **标识符**：`arXiv:2608.11232`（`DOI: 10.48550/arXiv.2608.11232`）
- **发表/提交时间**：v1 `2026-07-31T02:37:57Z`（归入 `2608` 批次）；arXiv comment: *"Accepted to the FinLLM Workshop at IJCAI 2026"*
- **双源回执**：源 A = arXiv API (`08:56:04Z`)；源 B = DBLP `journals/corr/abs-2608-11232` (`08:57Z`) + GitHub `rzhao999/Backtrader-Bench`
- **具体观察**：显式设置 **11 个模型无工具（no-tools，纯参数知识，每题 10 次运行）vs 4 个带工具配置（with-tools）** 对照：在 30 题精选集上，带工具前沿智能体（GPT-5.5、Opus 4.7）单遍达 **90.0%**，领先最强无工具基线（**73.0%**）达 **+17 个百分点**；在生成器-求解器挖掘的 38 道难题（专门剔除无工具可答题目）上，半数无工具模型跌至随机猜测水平（~**25%**）。
- **设定分类暂判**：相关但不同设定（含显式 no-tool vs with-tool 对照实验，直接支撑本文 §2.1 / §5.1–5.3 参数天花板假说，但任务为量化回测 MCQ 而非提示阶段消融）。`conf: 0.95`

> **G1 子问题 2 检索观察记录**：在 2026 H2（`2607`–`2611`）全部新发布的冠名 "Agent Benchmark" 论文中，几乎所有基准（如 AgentHop `2609.34428`、$\tau^\tau$-Bench `2609.04611`、DUMA-Bench `2609.24662`、$\Delta\tau$-Bench `2610.34238`、MS-Eval `2610.22869`、Parametric CAD Bench v3 `2611.02659`）均默认绑定外部工具沙箱；仅 Backtrader-Bench (`2608.11232`) 专门设立了 `no-tools` 对照组。**未发现任何其他在纯参数无工具设定下对多阶段研究流水线做逐阶段消融的 agent benchmark**，证明本文核心定位仍具独特性。

---

### 2.2 方向 D2：Prompt Structure Ablation 2026 H2（对应空缺 G2，4 篇，含 3 篇直接竞品！）

#### [N04] CausalCoT（2026-10）— ★直接竞品
- **标题**：*Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation*
- **作者**：Gabriele Dominici, Teague McMillan, Fazl Barez, Marc Langheinrich, Martin Gjoreski
- **标识符**：`arXiv:2610.31639`（`DOI: 10.48550/arXiv.2610.31639`）
- **发表/提交时间**：v1 `2026-10-22T17:52:56Z`
- **双源回执**：源 A = arXiv API (`08:56:04Z`)；源 B = 独立技术评述与开源复现工单（`kenashe.ai/blog/2026-10-23-causalcot...` + GitHub `rivers-research-hq/opentrader/issues/430`，`08:58Z`；DBLP 尚未入库）
- **具体观察**：在**无外部检索工具（纯推理期）**下对比标准自回归 CoT 与**有向无环图（DAG）子问题分解 + 父节点上下文隔离（CausalCoT）**。指出标准单遍 CoT 存在**注意力泄漏（attention leakage）**——稠密注意力允许后续步骤直接窥视全局上下文查表，同时生成看似合理的事后合理化解释（post-hoc justification）。通过马尔可夫式上下文隔离，CausalCoT 在保持预测准确率的同时，将中间推理步骤对最终答案的因果敏感度平均提升 **+12 个百分点（最高 +21 pp）**。
- **设定分类暂判**：**直接竞品**（同为 no-tool 推理期任务分解 vs 单遍提示结构对比；其「单遍全局上下文导致注意力泄漏/稀释，多调用隔离上下文才真正生效」直接解释了本文单遍 S3/S8E 失效而双遍 S7V 有效）。`conf: 0.90`

#### [N05] RE-ZS-CoT（2026-10）— ★直接竞品
- **标题**：*A Large-Scale Evaluation of Role-Enhanced Zero-Shot Chain-of-Thought Prompting*
- **作者**：Ibrahim Khan, Thai Van Nguyen, Yi Xia, Pratch Suntichaikul, Mustafa Can Gursesli, Daniel Fernandez Galeote, Juho Hamari, Ruck Thawonmas
- **标识符**：`arXiv:2610.29073`（`DOI: 10.48550/arXiv.2610.29073`）
- **发表/提交时间**：v1 `2026-10-21T01:53:34Z`
- **双源回执**：源 A = arXiv API (`08:56:04Z`)；源 B = ResearchGate 预印本索引与 `awesomepapers.io/llm-papers/papers/2610.29073` (`08:59Z`；DBLP 尚未入库)
- **具体观察**：在**无工具、零样本**设定下横跨 **20 个开源/轻量 LLM（含 2B–14B 规模如 Granite3.3-8B）与 7 个推理基准**系统消融对比 zero-shot、zero-shot-CoT、静态专家角色增强 CoT 与动态自选角色 CoT。在任务匹配时相对基线最高提升 **+44 个百分点**，但消融实验证明**与任务不匹配的非常规角色设定会显著拉低性能（degrade performance）**。
- **设定分类暂判**：**直接竞品**（同为开源权重模型 + no-tool 零样本提示结构/风格消融；定量印证本文 S6/S7「提示风格必须与题型对齐，错配即退化」结论）。`conf: 0.90`

#### [N06] Decorative to Load-Bearing CoT（2026-09 · TMLR 2026）— ★直接竞品
- **标题**：*From Decorative to Load-Bearing: Task Difficulty Shapes the Causal Role of Chain-of-Thought*
- **作者**：Renee Jia, Di Mu
- **标识符**：`arXiv:2609.25366`（`DOI: 10.48550/arXiv.2609.25366`；OpenReview: `TiZQnKDIHq`）
- **发表/提交时间**：v1 `2026-09-21T20:06:06Z`；发表于 *Transactions on Machine Learning Research (TMLR)*, September 2026
- **双源回执**：源 A = arXiv API (`08:56:04Z`)；源 B = DBLP 正式期刊记录 `journals/tmlr/JiaM26` + CoRR `abs/2609.25366` (`08:57Z`)
- **具体观察**：在无工具开源权重模型（Gemma-2-9B-IT、Llama-3.1-8B-Instruct、DeepSeek-R1-Distill-Qwen-7B）与 GSM8K / MMLU / BBH 上，通过扰动截断续写消融（28,584 条轨迹）量化显式推理链的因果承重度（load-bearingness）。方差分解表明 **98.8% 的解释偏差由模型相对任务难度决定**（扰动类型仅占 0.8%）：在简单/熟悉任务上模型静默绕过书面推理（CoT 仅是「装饰性的 decorative」），在困难任务上错误传播率飙升 **16 倍**。
- **设定分类暂判**：**直接竞品**（同为开源权重 + no-tool 下的显式推理步骤消融；为本文「熟悉概念题 Q5 上无结构 S6 夺冠，复杂规格/矛盾题 Q1/Q4 上结构支架才承重」提供了精确因果机理）。`conf: 0.98`

#### [N07] Verbalization Bottleneck in CoT（2026-07 · ICML 2026 AI4Law Workshop）
- **标题**：*When Reasoning Hurts Legal Drafting: The Verbalization Bottleneck in Patent Claim Generation*
- **作者**：Lekang Jiang, Wenjun Sun, Stephan Goetz
- **标识符**：`arXiv:2607.10480`（`DOI: 10.48550/arXiv.2607.10480`）
- **发表/提交时间**：v1 `2026-07-11T21:19:39Z`；arXiv comment: *"Accepted to AI for Law Workshop @ ICML 2026"*
- **双源回执**：源 A = arXiv API (`08:56:04Z`)；源 B = `web_search` 独立检索摘要核对 (`08:55Z`)
- **具体观察**：在高度结构化的专利权利要求生成任务中对比显式口头化 CoT（explicit CoT）与隐式内部推理（implicit CoT），发现**显式写出推理步骤一致劣于隐式推理**，并归因于三种机制：**关键细节抽象丢失（abstraction of critical details）、破坏模型内化生成模式（disruption of internalized generation patterns）、级联错误传播**。
- **设定分类暂判**：相关但不同设定（纯文本专有领域生成，无工具；其三大退化机制与本文 §4.4「S1 机械分解抹掉 H100 SXM/PCIe 隐含限定语、导致 M7 从 0.306 降至 0.256」高度吻合）。`conf: 0.92`

---

### 2.3 方向 D3：LLM-as-Judge 2026 H2（对应空缺 G3，4 篇）

#### [N08] Pinned and Still Unstable（2026-09）
- **标题**：*Pinned and Still Unstable: Within-Judge Verdict Variance and the Noise Floor of LLM-as-Judge Leaderboards*
- **作者**：Krishna Chytanya Ayyagari
- **标识符**：`arXiv:2609.33044`（`DOI: 10.48550/arXiv.2609.33044`）
- **发表/提交时间**：v1 `2026-09-27T00:19:41Z`；v2 `2026-09-30T20:45:58Z`
- **双源回执**：源 A = arXiv API (`08:56:05Z`)；源 B = DBLP `journals/corr/abs-2609-33044` (`08:56Z`)
- **具体观察**：在固定模型版本且 `temperature=0` 下测试 4 个前沿云端裁判横跨 Arena-Hard、AlpacaEval 2、MT-Bench 的重跑稳定性：单题判定翻转率均值约 **5%**（跨裁判跨度 0.13%–10%，相差 40 倍），而在决定榜单微弱差距的临界题上翻转率高达 **~40%**；单一裁判内总排名稳定，但**跨模型家族裁判间（如 Gemini vs Sonnet）中段排名显著分歧（Arena-Hard 上 Kendall's $\tau$ 低至 0.42–0.64）**；复核 15 条头对头预期排序，主裁判重跑保留 12 条，但跨全体异族裁判仅 **8/15** 存活。作者提出最低报告准则：**多次裁判重跑 + 稳定性区间 + 至少两个不同模型家族裁判**。
- **设定分类暂判**：相关但不同设定（评测器基础设施研究；直接印证本文 §5.4 单遍打分 ±0.10 噪声底与 §4.5 跨家族裁判必要性，并对 Q1 H1 跨族翻转给出外部定量参照）。`conf: 0.96`

#### [N09] Self- and Other-Labels Induce Bidirectional Bias（2026-08 / v3 2026-10 · Findings of EMNLP 2026）
- **标题**：*Self- and Other-Labels Induce Bidirectional Bias in LLM Judges*
- **作者**：Songeun Chae, Min Kim, Donghoon Jung, Seojin Choi, Seohyon Jung
- **标识符**：`arXiv:2608.18091`；正式会议录 `DOI: 10.18653/v1/2026.findings-emnlp.1571`
- **发表/提交时间**：arXiv v1 `2026-06-06`（归入 `2608` 号段），v3 `2026-10-16T04:41:23Z`；发表于 *Findings of the Association for Computational Linguistics: EMNLP 2026*, pp. 33466–33482（2026 年 10 月，布达佩斯）
- **双源回执**：源 A = arXiv API (`08:56:05Z`)；源 B = ACL Anthology `2026.findings-emnlp.1571` (`08:58Z`) + DBLP `journals/corr/abs-2608-18091` (`08:57Z`)
- **具体观察**：指出既往「LLM 自偏爱（self-preference）」研究将生成文本风格与质量混杂。作者设计去风格指纹任务测试 10 个 LLM，得出两项翻转性结论：(1) **在盲评（blind evaluation）下，一旦控制候选质量与裁判固有严厉度（judge severity），自偏爱效应基本消失，甚至在部分维度呈微弱反向（对自己产出打分更严）**；(2) 只有在显式标注「自己/他人」来源标签时，裁判才会双向虚高自标项、压低他标项。
- **设定分类暂判**：相关但不同设定（裁判偏置机理研究；**直接化解本文 §4.5 的表面反常**——本文盲评下本地同族 27B 裁判比异族前沿裁判低 ~0.15 并非反常的「负自偏爱」，而是盲评去标签后暴露出的**裁判基准严厉度差异 judge severity**！）。`conf: 0.98`

#### [N10] All Verdicts are Not Equal（2026-10 · AACL-IJCNLP 2026 Main）
- **标题**：*All Verdicts are Not Equal: Rethinking LLM Judge Reliability*
- **作者**：Vineet Kumar, Darshita Rathore, Anindya Moitra
- **标识符**：`arXiv:2610.12083`；正式会议录 `DOI: 10.18653/v1/2026.aacl-long.207`
- **发表/提交时间**：v1 `2026-10-08T14:55:29Z`；发表于 *Proceedings of AACL-IJCNLP 2026 (Volume 1: Long Papers)*, pp. 4581–4598
- **双源回执**：源 A = arXiv API (`08:56:26Z`)；源 B = ACL Anthology `2026.aacl-long.207` (`08:58Z`) + ResearchGate `415469614`
- **具体观察**：对 6 个前沿模型在 4 个基准 × 5 种提示格式 × 2 种顺序 × 3 种温度 × 10 次重复下做系统压力测试：发现 `temp=0` 仍会跨重复翻转，难题上交换位置翻转过半判定，且**最确定性的裁判靠机械重复错误判定获得 100% 自洽，但与真值一致率仅 51%**（与 Tiwari 2026 `arXiv:2609.13824` 在本地开源裁判 LLaMA-3-8B/Qwen2.5-7B 上测得 92.3%–97.3% 自洽率但仅 $r=0.275\text{–}0.340$ 人类相关性的结论完全一致）。关键正面发现：**从成对胜率（pairwise win-rate）转向整体多维量表打分（holistic rubric scoring）对可信判定率（Trustworthy Verdict Rate）的提升大于任何单格式提示修补**。
- **设定分类暂判**：相关但不同设定（评测器审计；正面支撑本文采用多维 rubric 打分而非成对偏好，同时警示高重复 $\kappa$ 不等于真值准确）。`conf: 0.98`

#### [N11] The Judge Can Debias Itself（2026-10）
- **标题**：*The Judge Can Debias Itself: Awareness and Self-Debiasing for Reliable LLM-as-a-Judge*
- **作者**：Youbing Yin, Jingyu Wu, Anoop Kumar, Scott Novotney, Daben Liu, Erin Babinsky
- **标识符**：`arXiv:2610.24320`（`DOI: 10.48550/arXiv.2610.24320`）
- **发表/提交时间**：v1 `2026-10-16T23:36:11Z`
- **双源回执**：源 A = arXiv API (`08:56:26Z`)；源 B = 独立论文库 `roboticscenter.ai/research/papers/...-2610` (`08:59Z`；DBLP 尚未入库)
- **具体观察**：构建了三个全新裁判偏置基准——**权威偏置（authority bias：伪造引用 fabricated citations）**、**自信偏置（confidence bias：武断措辞 assertive phrasing）** 与 **格式偏置（formatting bias：结构化排版 structured presentation）**（共评测 7 类偏置）。证明显式偏置提示与自纠偏（self-debiasing）在 20/21 个模型-偏置组合上提升最高 +15 pp，而微调外部评论器在新偏置上 5/9 退化。
- **设定分类暂判**：相关但不同设定（裁判偏置与去偏；**直接向本文核心结论发起尖锐方法学挑战**——本文 S1–S5 强行输出树状结构与章节引用，LLM 裁判的 formatting bias 与 authority bias 可能虚增了结构臂相对散文臂 S0/S6 的得分！）。`conf: 0.90`

---

### 2.4 方向 D4：Deep Research Agents 2026 H2（对应空缺 G4，3 篇 + 1 篇 H1 溯源对照）

#### [N12] WANDR（2026-08）
- **标题**：*WANDR: A Benchmark for Wide and Deep Research*
- **作者**：Vitaliy Polshkov, Marcin Pitera, Jeremy Yang, Kirill Priemko, Maksim Gaiduk, Aleksandr Nikolenko, Denis Bykov, Clare Southern, Denis Yarats, Jerry Ma
- **标识符**：`arXiv:2608.14747`（`DOI: 10.48550/arXiv.2608.14747`）
- **发表/提交时间**：v1 `2026-08-14T00:18:53Z`
- **双源回执**：源 A = arXiv API (`08:56:05Z`) + HTML 正文表 6.1–6.3 (`08:55Z`)；源 B = DBLP `journals/corr/abs-2608-14747` (`08:56Z`) + GitHub `perplexityai/wandr`
- **具体观察**：500 个宽深结合（广度实体发现 × 深度多跳核实）真实研究任务，动态重抓被引网页逐条核验记录，直接横评商业生产级系统：**Perplexity（Soft F1 0.363 / Hard F1 0.133）**、**OpenAI Responses Web Agent（Soft F1 0.121 / Hard F1 0.035）**、**Gemini Deep Research（Soft F1 0.055 / Hard F1 0.009）** 及 Anthropic Managed Agents。其 §6.3.5 失效分析揭示关键现象 **"Faithful excerpts usually support something, but not everything"**：Gemini Deep Research 忠实摘录中有 96.9% 支持至少一项断言，但仅 **55.6%** 支持所挂靠的**全部**断言（OpenAI 为 75.7%，Perplexity 为 80.4%）。
- **设定分类暂判**：相关但不同设定（商业有工具 Deep Research 评测；补齐任务书点名的 Perplexity / OpenAI / Gemini Deep Research 2026 H2 学术横评，且其「部分支持但非全量支持」与本文 §5.1 S7T 源锚定及 `gates.py` claim 级修复完全互证）。`conf: 0.97`

#### [N13] MisKnow-Agent（2026-07）
- **标题**：*Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions*
- **作者**：Pengyu Zhu, Lijun Li, Longju Yang, Sen Su, Jing Shao
- **标识符**：`arXiv:2607.20891`（`DOI: 10.48550/arXiv.2607.20891`）
- **发表/提交时间**：v1 `2026-07-23T03:28:08Z`；v2 `2026-07-30T04:45:04Z`
- **双源回执**：源 A = arXiv API (`08:56:05Z`)；源 B = DBLP `journals/corr/abs-2607-20891` (`08:57Z`) + GitHub `whfeLingYu/MisKnow-Agent`
- **具体观察**：在 DeepResearch Bench 任务上构造 5,933 篇带受控权威线索但支持错误结论的误导文档，评测 **Gemini Deep Research**、DeerFlow 与 WebThinker。仅注入 **1 篇**误导文档即令平均错误结论采纳率（FCAR）从对照组的 **0% 飙升至 54.7%**；且**研究前/研究后防御虽能降低 FCAR 但无法消除采纳**，作者呼吁在证据进入中间状态时做持续核验。
- **设定分类暂判**：相关但不同设定（有工具对抗注入评测；既佐证本文 §5.1 S7T 检索降分现象，又对本文「S7V 事后双遍核验即可恢复准确率」构成边界限定——面对高权威伪装的误导源，单靠事后核验不够）。`conf: 0.96`

#### [N14] DAGent（2026-09 · NeurIPS 2026）
- **标题**：*DAGent: Evaluate-then-Grow Planning for Deep Research Agents*
- **作者**：Hanwen Liu, Yuanfu Sun, Qiaoyu Tan
- **标识符**：`arXiv:2609.39154`（`DOI: 10.48550/arXiv.2609.39154`）
- **发表/提交时间**：v1 `2026-09-30T07:19:01Z`；arXiv comment: *"Accepted at NeurIPS 2026"*
- **双源回执**：源 A = arXiv API (`08:56:05Z`)；源 B = DBLP `journals/corr/abs-2609-39154` (`08:57Z`) + GitHub `hanwenliu6825/DAGent`
- **具体观察**：指出既有基于 DAG 的研究智能体普遍采用 **Plan-then-Patch（执行前一次性生成全任务分解图，失败后再修补）**，这种前置静态分解在证据最薄弱时做出最强承诺，导致深研脆弱与无效分支浪费。提出 **Evaluate-then-Grow**（按已完成节点的置信度与不确定性信号逐批动态生长任务图）+ DAGRPO，在 BrowseComp-Plus / GAIA / xbench-DeepSearch 上超越最强开源基线 **+5.3 / +5.8 / +2.0 分**（同架构下比 Plan-then-Patch 准确率更高且 token/工具调用更少）。
- **设定分类暂判**：相关但不同设定（有工具 + RL 动态图规划；对本文 S1「一次性静态前置目标分解」与异族裁判下 Q1 S1<S0 反例提供了极佳的理论解释）。`conf: 0.97`

> **D4 附注（已核实并按时间窗分流）**：
> - 另核实了 `competitor-survey.md` 中提及的 **DRACO**（Zhong, J., Zhang, H., Southern, C., et al., *DRACO: a Cross-Domain Benchmark for Deep Research Accuracy, Completeness, and Objectivity*, `arXiv:2602.11685`, v1 `2026-02-12`，横评 Perplexity DR 70.5%、Gemini DR 62.7%、OpenAI o3 DR 56.9%）及 **DeepResearch Bench II**（`arXiv:2601.08536`, `2026-01`，横评 OpenAI-o3 DR 45.40、Gemini-3-Pro DR 44.60、Perplexity DR 38.58），以及 2026-10 的 **LifeSearch**（Wang, Y. et al., `arXiv:2610.18092`, `2026-10-13`，4,000+ 专家细粒度 rubric 评测 12 个 DR 智能体，最强 GPT-5.6 Sol 仅 63.4%）。为严格遵守阶段 01 冻结规则 **E-time（优先 2026 H2 / 09~11）**，DRACO 与 DRB-II 不占 ≥8 篇 H2 主配额（可在背景句顺带提及或以 2026-08 的 WANDR + 2026-10 的 LifeSearch 为主配额）。我们将 **LifeSearch (`arXiv:2610.18092`)** 一并纳入候选池作为 **[N14b]** 备用/增强项（已在 §0 C2/C5 完成 arXiv API + PapersWithCode 双源核验）。

---

### 2.5 方向 D5：Calibration 2026 H2（对应空缺 G5，3 篇）

#### [N15] Rethinking Verbalized Confidence（2026-09）
- **标题**：*Rethinking Verbalized Confidence for LLM-as-a-Judge: A Compatibility Shift on Post-2025 Proprietary Models*
- **作者**：Yu-Chung Hsiao
- **标识符**：`arXiv:2609.10996`（`DOI: 10.48550/arXiv.2609.10996`）
- **发表/提交时间**：v1 `2026-09-10T02:17:35Z`
- **双源回执**：源 A = arXiv API (`08:56:26Z`)；源 B = DBLP `journals/corr/abs-2609-10996` (`08:56Z`)
- **具体观察**：横跨 SummEval、AggreFact、HelpSteer2 与最多 18 个 LLM，直接量化对比 **verbalized confidence vs 基于 logprob 的 G-Eval**。发现「**代际兼容性转移（compatibility shift）**」：在 2025 年后的前沿闭源模型上，「优先用 logprobs 而非口头置信度」的旧共识不再成立，口头置信度叠加「过度自信警示（overconfidence advisory）+ 自我辩论」校准更好且抗主观性更强；但**较早期/较弱模型加载这两项提示修补会付出可测量的平衡准确率代价**。
- **设定分类暂判**：相关但不同设定（校准信号对比；直接回应任务书 D5「verbalized vs logprob 新结果」，既支撑本文 S6「自然语言不确定性警示校准 M2」，又警示在中型模型上加校准指令可能与准确率存在权衡）。`conf: 0.96`

#### [N16] Measurement Validity of Confidence Signals（2026-10）— ★直接方法学反方
- **标题**：*Measurement Validity and Representation Dynamics of Confidence Signals in Large Language Models*
- **作者**：Debojeet Ghosh, Shreyansh Kumar, Ayushman Garg
- **标识符**：`arXiv:2610.25846`（`DOI: 10.48550/arXiv.2610.25846`）
- **发表/提交时间**：v1 `2026-10-19T06:04:38Z`
- **双源回执**：源 A = arXiv API (`08:56:26Z`)；源 B = `awesomepapers.io/llm-papers/papers/2610.25846` (`08:59Z`；DBLP 尚未入库)
- **具体观察**：在无工具开源权重 **Qwen2.5 系列（0.5B–7B，含 Base/Instruct 对照）** 与事实检索（PopQA, SimpleQA）及推理（GSM8K, MATH）上做预注册审计，同台对比 **口头置信度（verbalized confidence）、隐状态线性探针（hidden-state linear probes）与多样本一致性（semantic entropy）**。得出两条关键负结果：(1) **口头置信度对提示词极其敏感不稳定**（轻微改写提示模板，得分几乎不相关）；(2) **ECE 指标具有欺骗性**——口头置信度看似校准良好（ECE 低），是因为分数聚集在基率附近而缺乏区分度（poor discrimination），反观多样本一致性虽 ECE 较差但分辨率（resolution）高出约 **2 倍**。
- **设定分类暂判**：**直接竞品/方法学反方**（同为 Qwen 开源系 + no-tool 事实与推理任务；直接挑战本文 §2.3/§4.3 将 S6 M2=0.618 解读为「校准成功」的效度——M2 跃升可能混有基率聚集与模板敏感效应！）。`conf: 0.92`

#### [N17] DualStake（2026-09 · EMNLP 2026 Main）与 [N18] Token Probabilities Calibration（2026-11 · EMNLP 2026 W-NUT）
- **[N17] 标题**：*DualStake: Dual-Path Confidence Calibration in Deep Research Agents*（EMNLP Anthology 题录末尾为单数 *Agent*）
  - **作者**：Yinuo Xu, Yuwei Liang, Jianjie Cheng, Meng Wang, Yongcan Yu, Shuo Lu, Jian Liang
  - **标识符**：`arXiv:2609.00935`；正式会议录 `DOI: 10.18653/v1/2026.emnlp-main.389`（EMNLP 2026 Main, pp. 8924–8941）
  - **发表/提交时间**：v1 `2026-09-01T08:56:01Z`；EMNLP 2026 Main（2026-10）
  - **双源回执**：源 A = arXiv API (`08:56:26Z`)；源 B = DBLP `conf/emnlp/XuLCWYLL26` + `aclanthology.org/2026.emnlp-main.389/` (`08:57Z`)
  - **具体观察**：针对 Deep Research 智能体严重过度自信问题（在 Qwen2.5-7B / Qwen3-4B 与 8 个 QA 基准上测试），发现**检索末步诱导的证据置信度（Evidence Confidence, E-Conf）比答案生成后的口头置信度（Answer Confidence, A-Conf）提供更强的不确定性信号**，且通过双路径奖励对齐可在不损准确率下改善校准。`conf: 0.98`
- **[N18] 标题**：*Evaluating Token Probabilities as Confidence Estimators in Human Behavior Simulations: A Case Study in Luxembourgish Next Like Prediction*
  - **作者**：Nils Schwager, Simon Münker, Alistair Plum, Achim Rettinger
  - **标识符**：`arXiv:2611.07735`；正式会议录 `DOI: 10.18653/2026.wnut-1.7`（EMNLP 2026 W-NUT, pp. 89–100）
  - **发表/提交时间**：ACL Anthology 出版 `2026-10`；arXiv v1 `2026-11-05T09:45:49Z`（昨日最新挂出！）
  - **双源回执**：源 A = arXiv API (`08:56:26Z`)；源 B = ACL Anthology `https://aclanthology.org/2026.wnut-1.7/` (`08:58Z`)
  - **具体观察**：测试开源权重模型（Ministral 3B, 8B）的 **token probabilities（logprobs）** 能否直接作为置信度估计：在仅用上下文提示（in-context learning only）时，token 概率系统性过度自信且劣于简单统计基线；**参数从 3B 扩至 8B 虽提升准确率却恶化校准**，唯有任务级 SFT 才能将 ECE 从 **0.20 压至 0.006**（准确率 0.536→0.758）。`conf: 0.98`

---

## 3. 阶段 02 空缺闭合度与遗留问题清单

| 空缺 | 闭合状态 | 说明 |
|------|---------|------|
| G1 (D1 Agent Benchmarks) | ✅ 已闭合 | 收录 3 篇（`2609.34428`, `2610.25954`, `2608.11232`），并确认 2026 H2 无同设定「纯参数逐阶段研究流水线消融」新基准 |
| G2 (D2 Prompt Ablation) | ✅ 已闭合 | 收录 4 篇（`2610.31639`, `2610.29073`, `2609.25366`, `2607.10480`），捕获 3 篇 no-tool 直接竞品 |
| G3 (D3 LLM-as-Judge) | ✅ 已闭合 | 收录 4 篇（`2609.33044`, `2608.18091`, `2610.12083`, `2610.24320`），覆盖稳定性、同族自偏爱盲评消失、格式/权威偏置 |
| G4 (D4 Deep Research) | ✅ 已闭合 | 收录 3+1 篇（`2608.14747` WANDR、`2607.20891` MisKnow-Agent、`2609.39154` DAGent + `2610.18092` LifeSearch），完整覆盖 Perplexity/OpenAI/Gemini DR 评测 |
| G5 (D5 Calibration) | ✅ 已闭合 | 收录 4 篇（`2609.10996`, `2610.25846`, `2609.00935`, `2611.07735`），覆盖 verbalized vs logprob vs probe 全路线，且顺带核实草稿既有 3 篇 `2609.*` |
| G6 (双源独立印证) | ⚠️ 部分受索引时滞限制（如实保留） | 18 篇候选中 13 篇拥有 DBLP / ACL Anthology / 官方 GitHub 强独立第二源；5 篇 2026-10 中下旬预印本（`2610.25954`, `2610.31639`, `2610.29073`, `2610.24320`, `2610.25846`）因距今仅 2–3 周尚未进入 DBLP CoRR 批处理，已用外部项目页/学术聚合库核验并将在阶段 02.5 显式标注索引时滞 |

---

## 4. 阶段 02 门禁自检（对照 `02-information-research.md` 质检标准）

- [x] **围绕阶段 01 空缺搜集**：全部 18 篇核验记录一一映射至 G1–G6 与冻结域 D1–D5，无越界漂移。
- [x] **证据三要素齐备**：每条文献均记录完整标题、作者、arXiv/DOI URL、提交/发表日期、精确 UTC 观察时间戳与置信度。
- [x] **通道失败如实记录**：`ego-browser` 不可用及 2026-10 下旬 DBLP 未同步状态均如实登记，未伪造证据。
- [x] **未提前写最终推荐**：本文件仅给证据与暂判，§2 具体修改文本留至阶段 03/04。

**阶段 02 自检结论**：证据完备、来源真实（status: pass → 推进至阶段 02.5 交叉核验与对抗质疑）。
