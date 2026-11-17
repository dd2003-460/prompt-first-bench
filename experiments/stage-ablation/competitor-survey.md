# Deep Research 竞品与基准调研（对标最高水平）

> origin: ai · 2026-11-03 · D指令「以后就对标最高水平」
> 用途：stage-ablation D1 判据 + 后续论文 related work 的事实基础。所有外部数字带来源和观察日期，未独立复测的标 conf。

## 1. 开源 deep research agent 格局（2026-11-03 观察）

| 项目 | 路线 | 强项 | 弱项/注意 | 来源 |
|------|------|------|-----------|------|
| GPT Researcher (assafelovic) | 固定流水线+LLM决策点；子查询 asyncio.gather 并行；deep mode = breadth×depth 递归树 | 工程成熟、30k star、MIT、pip 可装、MCP 集成 | 无阶段门禁/质量检查；citation grounding 弱（DREAM 评测结论）；skills/researcher.py 单文件 1149 行耦合 | github.com/assafelovic/gpt-researcher；ACL 2026 DREAM (aclanthology.org/2026.acl-long.448) |
| STORM / Co-STORM (stanford-oval) | 模拟多 persona 专家对话→大纲→正文（Wikipedia 写作流程） | 引用质量高、star 最多、长篇结构化文章 | 仓库更新慢（~10 个月无 push，2026-03 观察）；面向文章生成非问答 | digitalapplied.com 2026 开源 DRA 实测指南 |
| Open Deep Research (LangChain) | LangGraph supervisor+subagent 图，工具调用循环 | 灵活、可换模型/MCP、DeepResearch Bench 曾上榜 | DREAM 评测 Factuality 最低(44.64)，claim attribution 差 | langchain.com/blog/open-deep-research；DREAM |
| OpenResearcher (OPPO, arXiv:2603.20278) | 离线语料(15M doc)+三原语(search/open/find)合成 97K 轨迹→SFT 30B-A3B | 训练透明可复现；BrowseComp-Plus 54.8% (+34.0 over base) | 是训练 pipeline 非推理产品；需 vLLM+veRL | arxiv.org/abs/2603.2020278 (EMNLP 2026 main.42) |
| Tongyi DeepResearch (阿里) | 30.5B MoE (激活 3.3B) RL 长程搜索 | 开源权重、工业规模 | 需集群；DREAM 中 CI≈1.03（几乎不做 claim 落地） | DREAM；EMNLP 2026 |
| ASearcher-QwQ-32B / WebDancer / CutBill-30B | RL 系（GRPO/异步 RL） | 长程多轮搜索能力 | 学术实验为主 | EMNLP 2026 OpenResearcher 相关工作 |
| navinsreyas/research-agent (LangGraph, MIT) | 并行搜+credibility scorer+critique 循环 | **唯一见到显式来源权威度打分**：base 0.5 + authority(.edu/.gov/Reuters)+0.2 + freshness+0.2 + depth(>5k chars)+0.1；缺口检测(detective logic) | 小项目(9 commits)；启发式非学习式 | github.com/navinsreyas/research-agent |

**关键空白（我们的差异化空间）**：
- 没有开源系统做「分解+标注缺口+留空」的前置质检模块（decomp 的定位）。
- 没有成熟的「交叉验证置信度」实现——现有 credibility scorer 全是单源打分；两独立源相互印证才升级 conf 的结构未见成熟开源版。T22 闸2(矛盾检测)+r3 citation_check 拼起来是雏形。
- ACL 2026 DREAM 结论：所有开源 DRA 普遍栽在 citation grounding（claim→source 对应关系烂），报告可读性尚可但不可信。这正是三道闸要解的问题。

## 2. 基准格局（2026-11-03 观察）

| 基准 | 设计 | 头部表现 | GPT Researcher 位置 |
|------|------|----------|---------------------|
| DeepResearchGym (CMU, 2025-05) | 1000 复杂查询 | GPT Researcher 第一（超 Perplexity/OpenAI 闭源） | ✅ 唯一坐实的"第一" |
| DeepResearch Bench (100 PhD 级任务, 22 领域) | RACE 四维, GPT-5.5 判 | Gemini-2.5-Pro DR 48.92 榜首；OpenAI/Claude 二三 | ❌ 非头部（被当并行架构代表引用） |
| DRACO (Perplexity+Harvard, 2026-02) | 100 真实用户任务+专家 rubric | Perplexity 70.5% / Gemini 59% / o3 52.1% | ❌ 不在被测名单 |
| BrowseComp (Meta 2025) | 精确匹配、多步导航 | Kimi K2.5 Swarm 72.1%；人类专家 87.5% | — |
| xbench-DeepSearch (清华) | 深度搜索 | — | — |
| ResearchRubrics (101 queries+专家 rubric) | 过程+结果 | LongCat-DeepResearch 79.83 | — |
| Mercor DeepResearch Bench II | 28 configs 榜单 | Opus 5 web-research agent 56.10% 榜首 | — |
| 社区小基准 (Reddit, HotpotQA/TruthfulQA/MMLU) | 非正式 3 题平均 | GPT Researcher 66.3 vs OpenResearcher 64.0 | ⚠️ 民间测试不算数 |

**对 D1 判据的含义**：「S5 ≥ GPT Researcher」= 打过开源工程最强的开箱水平（定位：star 最高+最成熟+可本地部署），**不能外推**为「比所有 deep research 系统都强」。跨基准 SOTA 目前是闭源 Gemini/Perplexity/OpenAI，跑不了也不该跑。scoring.md 必须写这个限定。

## 3. GPT Researcher 代码解剖（2026-11-03 读源码，clone @ runs/d1-gpt-researcher）

- 总量 16,115 行 Python；最大文件 skills/researcher.py 1149 行（研究循环+上下文+错误处理糊一起）、prompts.py 904 行纯模板字符串、deep_research.py 655 行（JSON 解析 4 套 fallback 正则）。
- 结构：`conduct_research()` → LLM 选 agent+role → `research_conductor` 拆子查询 → `asyncio.gather` 并行检索+爬取 → 一趟式汇总。**无 while 回退边、无阶段门禁、无回执**——框架是死管道，智能全在 LLM 单次调用里。
- deep mode：breadth(默认4)×depth(默认2) 递归树展开，每层「生成查询→搜→爬→下一层」。最接近状态机但本质是树不是带转移条件的图。
- 为什么不做质量检查：①商业激励=快出报告，检查=token 翻倍用户无感；②质量外包给模型层（prompt 写 "be accurate" 赌自觉）；③开放域无 ground truth，他们只做便宜版（引用格式存在）跳过贵版（内容核验）。
- 借鉴清单：✅ 检索器抽象(retrievers/)、MCP 接入方式、visited_urls 去重传递（父 researcher 传给子避免重复爬）。❌ prompt 管理（904 行字符串堆砌）、JSON 解析（4 套正则说明对模型输出没信心）。对比：gates.py 177 行的信息密度 > 其整个 scraper 模块。

## 4. 对标承诺（D 2026-11-03）

> 注意：这不是 pfb 独有的新标准。「对标领域顶刊/高 star 开源，先复刻再创新」是 `sop/goal-template.md` §3 对所有 goal 的硬规则；「纸面协议防护力为零」「统计量引用强制带口径限定」是 pfb AUDIT 于 2026-11-02 升格进 goal-template §4 的全局规则。本文件做的是把这条通用原则**实例化**到 deep research 这个具体领域——明确对手是谁、用哪把尺子、差异化在哪。

以后所有实验对标最高水平：
- 端到端对手 = GPT Researcher（开源最强工程基线）+ 公开榜 SOTA 数字（Gemini/Perplexity，只引不跑）。
- 评分器标准 = DREAM/RACE 的 claim-grounding 维度 + 自家 M1-M6（信息型分歧机判优先，主观维度多裁判+conf）。
- 来源可信度 = 参考 navinsreyas 启发式做 baseline，目标是做出交叉验证置信度（双源印证升级）这一别人没有的维度。
- 论文 related work 按本文件 §1-§3 组织，每个外部数字保留 URL+观察日期。

## 5. 对标目标 / bench 选择 / 可优化点（思考层，非资料清单）

### 5.1 对标目标分三层，别混

- **L1 工程基线**：GPT Researcher 开箱水平。这是 stage-ablation D1 直接打的对象，本地能跑、可复现、pip 装得动。过 L1 = 「我们的六阶段流水线比最强开源开箱水平强」——这是论文的主 claim。
- **L2 榜单 SOTA**：Gemini-2.5-Pro / Perplexity / OpenAI。这些是闭源，跑不了也不该跑，只能作为「天花板参照系」引用数字。作用是给读者一个量感：我们离绝对 SOTA 多远、差在哪。
- **L3 能力空白**：decomp（分解+缺口标注）、交叉验证置信度、三道闸的内容核验——这三样是所有开源 DRA 都没有的（§1 关键空白）。这才是真正的差异化，不是「比别人分高」而是「别人根本没有这个维度」。

对标最高水平的正确姿势：主 claim 打 L1（可证伪、可复现），用 L2 定坐标（我们在哪），用 L3 讲故事（我们独有的是什么）。

### 5.2 bench 怎么选：三个不同的尺子量三件事

- **stage-ablation 自研 5 题**（现在在跑）：量的是「每个模块的边际贡献」——S0→S5 每加一个阶段涨多少分。公开 bench 给不出这个，它们只有端到端总分。这是我们的核心科学问题，必须自研。
- **DeepResearch Bench / DRACO / BrowseComp**：量的是「端到端绝对水平」——在固定题目集上跟所有人比总分。用途是定位（L2 坐标）和投稿时的可比性证据，不是用来证明模块价值的。等 ablation 过了再投这些，顺序不能反。
- **DREAM 评测**：量的是「citation grounding」——claim 到来源的对应质量。这恰好戳中所有开源 DRA 的死穴（§1），也是我们三道闸要解的问题。所以 DREAM 的维度应该进我们评分器，而不是当成又一个总分榜。

一句话：自研 ablation 回答「为什么强」，公开 bench 回答「有多强」，DREAM 维度回答「强在哪一维别人做不到」。三者互补，缺一个故事都不完整。

### 5.3 可优化的地方（按杠杆大小排，不是按难度）

- **最大杠杆：把「交叉验证置信度」做成显式机制**。现状是所有系统单源打分（navinsreyas 那种启发式也是单源），没人做「两个独立来源相互印证才升级 conf」。T22 闸2（矛盾检测）+ r3 citation_check 已经是雏形，下一步是把「双源印证」从隐式行为变成有回执的显式步骤。这是 L3 里最硬的一块，做完就是别人抄不走的结构。
- **第二杠杆：decomp 前置质检模块坐实独立价值**。stage-ablation 如果显示 S1（加 decomp）相对 S0 的增量集中在 M4（缺口识别维度），就证明它不是重复造轮子而是补了行业空白。反过来如果增量不明显，要诚实面对——可能缺口标注需要更细的粒度才能体现。
- **第三杠杆：内容核验替代格式核验**。GPT Researcher 只做便宜版（引用存在），我们做贵版（页面上有这个数 ≠ 说的是同一件事）。r3 已证明这是假等价。优化方向是把 citation_check.py 从「URL 可达+数字出现」推进到「证据支持判断」（FActScore/SourceCheckup 那条路）。
- **小杠杆（先记着别急着做）**：检索器抽象可以借鉴 GR 的 retrievers/ 设计；prompt 管理不要学它（904 行字符串堆砌是反面教材）；JSON 解析对模型输出要有信心边界，别学它 4 套 fallback 正则。

### 5.4 分项数据的两个用途（双向判据）

L1 的「S5 ≥ GPT Researcher」判据依赖一个隐含假设：GR 在我们那 5 题上的表现代表它的真实上限。D1 每道题的分项数据有两个用途，缺一不可：

- **防 cherry-picking 嫌疑**：如果 GR 只在某类题（如开放式综述）上弱、其他题都强或持平，说明我们的题目集可能隐性偏向 pfb，结论不硬。缓解：补一两条 GR 擅长的题进对照集。
- **定位 pfb 的结构性优势**：反过来，如果 GR 在数值锚点密集的题（GPU 规格类）上系统性偏弱、pfb 稳定领先，这是最有价值的发现——证明六阶段流水线（交叉核对+缺口标注）在精确事实核验场景提供了通用流水线给不了的能力。论文主 claim 应落在「X 类任务上 Y 模块带来 Z 提升」，而不是笼统的总分对比。

真正的风险信号只有一种：GR 全面持平或更强，仅个别题 pfb 偶然赢——那说明优势来自题目偶然性而非结构。

## 6. 细粒度数值调研 bench 调研（2026-11-17 追加）

> 触发：D 问"我的 bench 是 GPU 调研这种颗粒度，深宽很细的大规模研究，有没有别的同类 bench？如果要可靠和宣传应该怎么做？"
> 核心发现：现有 DR bench 全是 flat claims 或报告级 LLM judge，没有测"分解树结构质量 + 多约束同时满足 + 每节点数值锚定"的。pfb 的差异化在结构和约束维度。

### 6.1 最接近的 bench（按颗粒度排序）

| Bench | 出处 | 评什么 | 粒度 | 结构 | 数值锚定 | 开源 | 免费跑 |
|-------|------|--------|------|------|---------|------|--------|
| **LiveDRBench** | Microsoft, ICLR 2026 | 中间 claim 生成步骤的 precision/recall | 单 claim | 无（flat） | 弱 | 代码+数据公开 | 需 LLM judge（可本地） |
| **DeepFact** | Duke+Amazon, ACL 2026 | DRR claim-level 事实性（Audit-then-Score） | 单 claim | 无 | 中 | 论文公开，数据 [待核验] | 需 LLM judge |
| **DRACO** | Perplexity+Harvard, 2026-02 | 4 维 rubric（accuracy/completeness/presentation/citation），每题 39.3 条 | 单条 rubric | 无 | 强（20.5/39.3 条测数值） | 数据在 HF 公开 | 需 LLM judge |
| **FALCA** | BAAI+THU+CASIA, 2026-10 (arXiv:2610.28361) | 不是 bench 是方法（propose-falsify 架构 + SFT+RL） | 研究状态 | 有（Searcher-Falsifier 双 agent） | 中 | 论文公开，**代码未开源** | 不能（需 8×H100 训练） |
| **DEER** | LG, ICML 2026 | 101 条 fixed rubric + 7 维 25 子维 taxonomy + claim 验证 | 单条 rubric + claim | 无 | 强 | 数据在 HF（密码 7z） | 需 LLM judge |
| **LiveResearchBench** | Salesforce, ICLR 2026 | 100 题 expert-curated，DeepEval 6 维（coverage/depth/citation/consistency/presentation） | 报告级 + claim 级 | 无 | 中 | 代码+数据公开 | 需 LLM judge |
| **DRBench** | ServiceNow, ICLR 2026 | 企业级 DR（公开 web + 私有 KB），100 题 10 域 | 报告级 | 无 | 中 | 代码+数据公开（github.com/ServiceNow/drbench） | 需 LLM judge |
| **WebDetective** | ICLR 2026 | 200 道 hint-free 多跳推理题（2-6 hops） | 单答案 | 无 | 弱 | 数据公开 | 纯字符串匹配，完全免费 |

### 6.2 pfb 的差异化定位

**所有现有 bench 都是 flat claims 或报告级打分，没有测"分解树结构质量"的。**

pfb 独有的维度：
1. **分解树结构**：fanout cap 8、quotient 比例（≤20%）、gap_check 维度覆盖率、edge 分类（cartesian/quotient）——这些是树结构指标，flat claims 没有
2. **多约束同时满足**：32K ctx 可行性 + TCO 全成本项 + 精度质量损失论证 + 性价比排序——不是单维打分，是约束交集
3. **每节点数值锚定**：27.5% verified（每个 verified 节点有外部数值源），对比 LiveDRBench 上 DeepResearcher+Qwen32B 的 0.06-0.12 F1
4. **rework 机制**：105 条 rework events 是"发现缺口→重新分解→再验证"的闭环，FALCA 的 propose-falsify 是同类思路但 pfb 有显式状态机

**主 claim 不是"分数比 X 高"，而是"分解质量 + 数值锚定率 + 约束满足度"三个维度别人没有。**

### 6.3 如果要可靠和宣传，最低可信度门槛

1. **样本量**：≥5 题（不是 1 题），覆盖 ≥3 个领域（硬件/金融/科学），每题 ≥2 次运行取均值 ± SD
2. **judge 一致性**：抽 20 条 judge 结果做人工标注对照，报 Cohen's κ 或 Spearman ρ（27b 同族自判的绝对值不可信，但一致率可以证明"判分不是随机的"）
3. **结构指标独立报告**：fanout、quotient%、gap_check 覆盖率、verified 率、rework 率——这些不依赖 judge，是纯计算指标，可信度最高
4. **数值锚定率**：verified 节点 / 总节点，每个 verified 节点必须有外部数值源（URL + 抓取时间戳）——这是最硬的指标
5. **约束满足矩阵**：每题列出所有约束（ctx 容量、TCO 项、精度选项、价格区间），逐条标注满足/未满足/部分满足
6. **完整 trace 公开**：源码 + 所有中间产物（节点 JSON、rework events、synth 报告、judge 输出）
7. **对比对象**：至少 2 个开源 DRA（GPT Researcher、Open Deep Research），用同一个 judge 评
8. **防刷题证明**：源码公开 + rubric 不是自己造的（用 DRACO/LiveDRBench 的公开 rubric）+ 完整 trace

### 6.4 免费可执行路径

1. **借 LiveDRBench 的 claim extraction**：对 gpu 题 synth 报告做 claim-level precision/recall，跟 OpenAI DR 的 0.48-0.61 F1 对比（需本地 27b 做 claim agreement judge）
2. **借 DRACO 的 rubric**：从 DRACO 100 题里挑 5-10 道数值密集的题，用 pfb 状态机跑，对比 39.3 条 rubric 通过率
3. **结构指标独立成表**：fanout/quotient%/gap_check/verified 率/rework 率，不依赖 judge，直接算
4. **WebDetective 免费跑**：200 道多跳题，纯字符串匹配评分，不需要 LLM judge，完全免费——作为"多跳推理能力"的辅助证据
5. **完整 trace + 源码公开**：GitHub repo，README 写清"如何复现"

### 6.5 跟现有 bench 的关系（不是替代，是互补）

- **LiveDRBench**：量 claim precision/recall（"说的对不对、全不全"）→ pfb 的 verified 率是它的结构升级版
- **DRACO**：量 rubric 通过率（"数值对不对、分析深不深"）→ pfb 的多约束满足是它的约束升级版
- **DeepFact**：量 claim 事实性（"引用是否支持 claim"）→ pfb 的 citation_check 是同类
- **WebDetective**：量多跳推理（"能不能串起来"）→ pfb 的分解树是它的结构升级版

一句话：现有 bench 回答"报告质量如何"，pfb 回答"分解过程质量如何 + 数值锚定率如何 + 约束满足度如何"。三者互补，缺一个故事都不完整。

### 6.6 FALCA 深度分析（2026-11-17 追加）

> 来源：arXiv:2610.28361（BAAI+THU+CASIA，2026-10-20）+ homepage（douzj-llm.github.io/FALCA）
> 核心发现：Falsifier 是主要增益来源（ablation -11.9 最大 drop），验证了 pfb rework 机制方向正确。但 FALCA 代码未开源、搜索用本地 HNSW（非开放 web）、训练需 8×H100。

#### 架构

- **Searcher-Falsifier 双 agent**：Searcher 提候选假设 → 独立 Falsifier（contradiction-first）找反例/查未满足约束/识别冲突 → 返回结构化 falsification report（verdict: reject/survive/uncertain + 被否约束 + 证据 + 建议后续搜索）→ Searcher 修订研究状态 → 循环
- **5 个工具**：Search（batched queries）/ Visit（webpage 摘要）/ Update Context（压缩研究状态：verified facts + unresolved constraints + plans）/ Finish（终止+最终答案）/ Refute（Falsifier 返回结构化对抗报告）
- **共享 evidence environment**：Searcher 和 Falsifier 用同一个搜索+浏览工具，但各自独立 context
- **研究状态**：压缩文本（非结构化树），通过 Update Context 维护

#### 成绩（4B 模型，5 个 benchmark）

| 配置 | BrowseComp | GAIA | DeepSearchQA | xbench-2510 | WideSearch-en | 均值 |
|------|-----------|------|-------------|-------------|---------------|------|
| Qwen3.5-4B（默认 harness） | 32.7 | 65.0 | 62.6 | 45.0 | 53.9 | 51.8 |
| Qwen3.5-4B（+Falsifier harness） | 39.0 | 62.1 | 63.3 | 49.0 | 64.3 | 55.5 |
| **FALCA-4B**（+SFT+RL） | **56.0** | **72.8** | **70.8** | **58.0** | **65.8** | **64.7** |
| Qwen3.5-9B（同 harness） | 41.4 | 68.0 | 65.0 | 48.0 | 67.2 | 57.9 |
| Tongyi-DeepResearch-30B | 43.4 | 70.9 | – | 55.0 | – | ~55 |
| GPT-5 | 54.9 | 76.4 | 79.0 | 75.0 | 59.7 | ~65 |
| Gemini-3.1-Pro | 85.9 | 80.6 | 93.3 | 53.0 | 66.4 | ~75.6 |

#### Ablation

| 变体 | 均值 | Δ |
|------|------|---|
| FALCA（完整） | 64.7 | — |
| w/o Falsifier | 52.8 | **-11.9**（最大 drop） |
| w/o Agentic RL | 60.5 | -4.2 |
| w/o Process-level Reward | 60.1 | -4.6 |

**Falsifier 是主要增益来源**，RL 和 process reward 是次要的。

#### 训练

- **SFT warmup**：在 falsification trajectories 上做 rejection sampling（保留正确答案+有效工具交互+充分证据支持的轨迹），masked LM 目标（mask 环境观测）
- **Agentic RL**：PPO-style，hierarchical credit assignment（trajectory→segment→turn 三级 reward），parallel rollouts（n 条轨迹并行），asynchronous trajectory execution + asynchronous process evaluation
- **Turn-level reward**：LLM judge（Qwen3.5-35B-A3B）给每个 turn 打分 s_t ∈ {-1, 0, 1, 2}（harmful/neutral/useful/critical）
- **Segment-level reward**：多跳任务的 subgoal 完成信号，均匀分配到对应研究阶段
- **Trajectory-level reward**：最终答案正确性（exact match + LLM judge）
- **硬件**：8× NVIDIA H100 80GB
- **搜索工具**：本地 HNSW 索引（BGE-m3 embedding），**不是开放 web 搜索**

#### 问题

1. **代码未开源**（截至 2026-11-17）。GitHub 搜不到 repo，homepage 只有论文和结果表
2. **搜索用本地 HNSW**（固定语料），不是开放 web——结果不能直接跟开放 web 系统比
3. **训练成本极高**：8×H100，SFT+RL 两阶段
4. **Falsifier 用同一 4B backbone**：falsification 能力受限于 4B 推理能力，如果 Falsifier 自己不懂，找到的"反例"可能是假的
5. **WideSearch-en 增益最小**：falsification 在"广覆盖"任务上收益有限，主要在"约束密集+多步验证"任务上有效

#### 跟 pfb 的对比

| 维度 | FALCA | pfb |
|------|-------|-----|
| 架构 | Searcher + 独立 Falsifier（双 agent） | 单状态机（分解→验证→rework） |
| Falsification | 显式 Falsifier agent，contradiction-first | rework 机制（发现缺口→重新分解→再验证） |
| 研究状态 | Update Context 压缩（verified facts + unresolved constraints + plans） | 分解树（cartesian/quotient 边、层级、fanout） |
| 训练 | SFT + agentic RL（8×H100） | 无训练（prompt + hook，不改权重） |
| 搜索 | 本地 HNSW（BGE-m3） | 开放 web（DDG/wiki/arxiv/ego-browser） |
| 约束 | 任务约束（answer type, hard/soft constraints） | 多约束（32K ctx、TCO、精度、价格） |
| 结构 | flat（research state 是压缩文本） | **树结构**（153 节点、6 顶层维度、edge 分类） |
| 可复现 | 代码未开源 | 源码可公开 |

#### 对 pfb 的启示

1. **FALCA 证明 falsification 是主要增益来源**（-11.9 最大 drop）→ 验证 pfb rework 机制方向正确
2. **双 agent vs 单 agent**：FALCA 的 Falsifier 是独立 agent（避免 confirmation bias），pfb 的 rework 是同一状态机内部循环（省 token 但可能有 self-confirmation bias）。pfb 的 27.5% verified 率 vs FALCA 的 4B 模型 58.0 xbench——不同 benchmark 不可直接比，但 pfb 在开放 web 上跑（更难），FALCA 在本地 HNSW 上跑（更受控）
3. **hierarchical credit assignment**（trajectory→segment→turn）跟 pfb 的 gain 轨迹（r1 0.968→r2 0.916→r3 0.892）思路类似——过程级信号比终局信号更有信息量
4. **如果 pfb 在开放 web 上能拿到 FALCA 在本地 HNSW 上的分数**，那是更强的 claim（开放 web 更难、更真实）
5. **FALCA 的 harness 部分（5 工具 + Searcher-Falsifier 循环）理论上可以用 prompt 实现**（不需要训练），但效果会差（55.5 vs 64.7）——pfb 的 rework 机制本质上就是 prompt 版的 falsification