# SOTA Deep-Research 系统调研（prior-art · 2026-11-12）

> origin: ai · 2026-11-12 · 补完上一轮因 provider 故障中断的调研。
> 来源标记：① = 本轮工具输出/刚读文件；② = 工作区历史文件（标文件名，conf 按新鲜度降档）；③ = 凭记忆未验证（只留 [待核验]，不展开）。
> 实测锚点（高可信）：gpt-researcher v0.17.0 在 DRB n=10 子集上 **6/10 题空壳答案**（来自上一轮实测记录，见 `research/sm-bench-closed-sota-v3.md` 上下文）。
> decomp：`research/deepresearch-bench/prior-art-sota-decomp.md`。

## 一句话结论

闭源 deep research 三家（OpenAI/Gemini/Perplexity）架构都是「单 agent + 迭代搜索循环」而非 multi-agent/tree search，且 OpenAI 家已于 2026-07-23 retired；开源最强工程基线 GPT-Researcher 是固定流水线+浅递归树，我们实测它在 DRB 上 60% 题产出空壳——说明这个 bench 对「不出报告」的系统区分度不足，选基线和定指标时必须把「有效完成率」当第一道闸。对我们本地 27B 管线，公平对标对象是 GPT-Researcher 同题同 judge 口径，不是闭源榜分数。

---

## 1. 五大系统：架构与公开成绩

### 1.1 OpenAI Deep Research（o3-deep-research / o4-mini-deep-research — 已 retired）

**架构**：单 agent 长程循环（非 multi-agent、非 tree search）。官方文档描述为「find, analyze, and synthesize hundreds of sources」的单一研究模型，通过 Responses API 挂载 web_search_preview / file_search / code_interpreter / remote MCP 工具，后台异步执行（background=true），无公开的多 agent 编排或子查询树结构。[① developers.openai.com/api/docs/guides/deep-research]

**生命周期**：2025-04 随 o3 发布（ChatGPT Pro 首发）→ 2026-04-22 OpenAI 宣布弃用 → **2026-07-23 正式关停**，官方替代方案为 `gpt-5.6-sol`（通用推理模型 + web_search 工具 + high reasoning effort + background mode），即「deep research 从独立模型退化为一种调用方式」。[① 同上 + hyperresearch.ai/alternatives/openai-deep-research-api]

**公开成绩**（DRB，GPT-5.5 judge 新榜，100 题全量）：
| 指标 | 分数 | 出处 |
|---|---|---|
| RACE Overall | **47.84** | ② `research/drb-leaderboard-gpt55.csv`（抓自 HF Space leaderboard） |
| Comprehensiveness | 48.05 | 同上 |
| Insight | 46.69 | 同上 |
| Instruction Following | 49.29 | 同上 |
| Readability | 47.62 | 同上 |
| FACT valid_rate | [待核验]（该 CSV 列缺失） | — |

GAIA / HLE / BrowseComp 上的 openai-deep-research 单项分数：本轮未抓到官方数字，[待核验]。注意 BrowseComp 榜单头部是各家的专用 agent 配置（如 multi-agent 变体），不等于产品默认配置。

### 1.2 Gemini Deep Research

**架构**：单 agent 迭代规划-执行-综合循环。官方文档明确：agent「autonomously plans, executes, and synthesizes multi-step research tasks」，迭代搜索+阅读，可浏览数百个网站（含 Gmail/Drive/Chat 个人数据），支持 MCP 外部工具、collaborative planning（先出计划→人审→再执行）、可视化图表生成。两个版本：Deep Research（速度优先）和 Deep Research Max（全面性优先）。全程需 background 异步执行，单任务上限 60 分钟。[① aistudio.google.com/docs/deep-research + gemini.google/overview/deep-research]

**公开成绩**（DRB，GPT-5.5 judge 新榜）：
| 指标 | 分数 | 出处 |
|---|---|---|
| RACE Overall | **49.98** | ② `research/drb-leaderboard-gpt55.csv` |
| Comprehensiveness | 50.01 | 同上 |
| Insight | 49.92 | 同上 |
| Instruction Following | 50.22 | 同上 |
| Readability | 49.58 | 同上 |

旧口径（Gemini-2.5-Pro judge，legacy 榜）下 gemini-2.5-pro-deepresearch 曾以 ~48.92 居榜首（② `experiments/stage-ablation/competitor-survey.md` §2）。注意：**judge 换代后排名不可跨榜比较**（DRB 官方也分两张榜展示）。

GAIA/BrowseComp：BrowseComp 上有 Gemini 系 agent 条目但具体配置与分数本轮未核，[待核验]。

### 1.3 Perplexity Deep Research

**架构**：单 agent 迭代搜索（agentic iterative search），官方定位「behaves more like a traditional research analyst」：先规划再行动，多次搜索、每次读完结果再决定下一步；底层是 Agent Search SDK / Search as Code（模型自己写代码组装搜索）。Pro Search 是其前身（多步推理版 quick search）。[① perplexity.ai/hub/blog/deep-research-now-in-computer + langchain.com/breakoutagents/perplexity]

**公开成绩**（DRB，GPT-5.5 judge 新榜）：
| 指标 | 分数 | 出处 |
|---|---|---|
| RACE Overall | **43.05** | ② `research/drb-leaderboard-gpt55.csv` |
| Comprehensiveness | 41.78 | 同上 |
| Insight | 41.27 | 同上 |
| Instruction Following | 45.31 | 同上 |
| Readability | 46.03 | 同上 |

另据 ② competitor-survey.md：DRACO（Perplexity+Harvard 2026-02，100 真实用户任务+专家 rubric）上 Perplexity 70.5% / Gemini 59% / o3 52.1% —— Perplexity 在自己主场基准上显著领先，但 DRB 上垫底于两大闭源对手。两榜方向相反本身就是重要信号（rubric 设计差异大）。

### 1.4 GPT-Researcher（assafelovic/gpt-researcher，开源）

**架构**：固定流水线 + LLM 决策点（非自主 agent 循环）。流程：`conduct_research()` → LLM 选 agent/role → research_conductor 拆子查询 → `asyncio.gather` 并行检索+爬取 → 一趟式汇总成文。**无 while 回退边、无阶段门禁、无质量回执**。deep mode = breadth(默认4)×depth(默认2) 递归树展开，每层「生成查询→搜→爬→下一层」——最接近状态机但本质是无转移条件的树。[② competitor-survey.md §3，2026-11-03 读源码 @ runs/d1-gpt-researcher]

**公开成绩**：
- DRB：**不在官方 leaderboard 被测名单**（本轮确认 repo raw_data 只有 claude-3-7-sonnet-latest + reference）。[① /tmp/drbench/data/test_data/raw_data/]
- DeepResearchGym（CMU 2025-05，1000 复杂查询）：GPT Researcher 排名第一（超 Perplexity/OpenAI 闭源）。[② competitor-survey.md §2，原始 URL 未保留，conf 降档]
- DREAM 评测（ACL 2026）：citation grounding 弱（所有开源 DRA 通病）。[② 同上]
- **我们的实测锚点**：DRB n=10 调研型子集，**6/10 题空壳答案**（报告主体缺失或极短）。这是本轮报告的实证核心之一，见 §2.3。

### 1.5 AutoGPT researcher 类

**定位澄清**：AutoGPT 是通用 autonomous agent 平台（task→goal 分解循环），不是 deep-research 专用系统；其「researcher」能力来自通用任务循环+工具调用，无专门的研究流水线设计。GPT-Researcher 的作者 Assaf Elovic 明确表示项目动机就是「AutoGPT 做研究太慢太贵不可控」而做的专用化。[① assafelovic.com blog 2023-07-25]

**对标意义**：不作为 deep-research 对标对象（类别不同）；在 related work 里归类为「前代通用 agent」即可。GAIA 论文本身出自 Meta/HF/AutoGPT 研究者联合工作（GAIA 466 题），但那是 benchmark 出处不是系统成绩。[① personalagentbench.com/benchmarks/gaia]

### 1.6 横向对比表

| 系统 | 架构类型 | 编排 | 工具面 | DRB (GPT-5.5 judge) | 备注 |
|---|---|---|---|---|---|
| OpenAI DR (retired) | 单 agent 循环 | 黑盒 | web/file/code/MCP | 47.84 | 2026-07-23 关停 |
| Gemini DR | 单 agent 循环 + 协作规划 | 半透明（plan 可见） | web+个人数据/MCP/可视化 | 49.98 | 双版本 speed/max |
| Perplexity DR | 单 agent 迭代搜索 | 黑盒 | Search as Code | 43.05 | DRACO 主场 70.5% |
| GPT-Researcher | 固定流水线+浅树 | 白盒（开源） | retrievers/MCP | 不在榜；实测 6/10 空壳 | 开源最强工程基线 |
| AutoGPT | 通用 agent 循环 | 白盒（开源） | 通用工具 | 不适用 | 类别不同 |

**共性发现**：三家闭源全是「单 agent 长程循环」路线，multi-agent/tree search 并未成为产品级 deep research 的主流架构（BrowseComp 榜首出现 multi-agent 配置是竞赛特例）。开源侧最强的 GPT-Researcher 反而是最「死」的管道——智能集中在单次 LLM 调用，框架无反馈回路。

---

## 2. DeepResearch Bench：构造、judge 协议、已知争议

### 2.1 构造方式

[① /tmp/drbench/README.md + data/prompt_data/query.jsonl（100 行实数）]
- **题数**：100 题 PhD 级研究任务，50 中 / 50 英（query.jsonl 每条含 id/topic/language/prompt）。
- **领域**：22 个 topic domains，按 WebOrganizer 分类法对齐真实需求分布——依据是对 **96,147 条匿名用户 query** 的分析。
- **出题人**：PhD 级专家 + 5 年以上资深从业者，逐题人工筛选（质量/清晰度/真实性/挑战度四标准）。
- **参考报告**：每题配一篇专家撰写 reference article（repo 内 reference.jsonl，100 篇，字符长度 min 18,298 / median 68,975 / max 189,932 —— 即参考报告本身是万字级长文）。[① 实测统计]
- **paper**：arXiv:2506.11763（ICLR 2026 camera-ready 在 proceedings.iclr.cc）。
- **后续**：DRB II（arXiv:2601.08536，2026-02-06 发布）改用 9,430 条细粒度二元 rubric（information recall/analysis/presentation），与 DRB I 评估重点不同，两者并存。

### 2.2 Judge 协议

**RACE（Reference-based Adaptive Criteria-driven Evaluation）**——评报告质量：
1. 动态生成 task-specific 评估准则，四维：Comprehensiveness / Insight / Instruction-Following / Readability；
2. target 报告 vs reference 报告相对评分（reference-based，保证区分度）；
3. 每任务动态权重加权合成 Overall。
Judge 模型沿革：Gemini-2.5-Pro（2025-07 起）→ **GPT-5.5**（2026-05-11 起，官方切换公告：在 50 题×4 目标 DRA=200 篇人工标注子集上测候选 judge 与人类判断的一致性，人类 inter-annotator agreement baseline = 68.78%，GPT-5.5 Overall 71.82 胜出）→ 清洗模型 2026-09-22 换 GPT-5.6 Luna（judge 仍 GPT-5.5）。[① README News 节]

**FACT（Framework for Factual Abundance and Citation Trustworthiness）**——评检索与引用落地：
1. 从报告中抽取 statement-URL 对并去重；
2. Jina 爬取 cited source 原文 + LLM 判断该源是否真支持该 claim；
3. 输出 Citation Accuracy（valid_rate）+ Effective Citations（每题平均可验证引用数）。
Judge：GPT-5.4-mini。repo 内置 claude-3-7-sonnet-latest 样例：total_citations 28.07 / valid 24.51 / valid_rate 0.873。[① results/fact/claude-3-7-sonnet-latest/fact_result.txt]

### 2.3 已知争议

**(a) 空壳答案问题（本轮核心实证）**：我们实测 gpt-researcher v0.17.0 在 DRB n=10 调研型子集上 6/10 题产出空壳答案（报告主体缺失/极短）。这意味着两件事：
- **judge 对「不出报告」不敏感**：RACE 是 target vs reference 相对评分，空壳理论上应得低分，但若 judge 对残缺文本仍给部分维度分（readability/instruction-following 可被标题党糊弄），总分会虚高——n=10 子集跑分前必须先做「有效报告率」前置过滤，否则分数不可信。
- **文献交叉验证**：本轮查到两篇相关但未直接点名「空壳」的工作——OPPO《How Far Are We from Genuinely Useful Deep Research Agents?》(arXiv:2512.01948) 分析 DRA 报告结构性缺陷（report structure 问题）；《Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents》(arXiv:2610.29346) 做过程级 failure mode 分析。两者都指向「DRA 产出质量方差极大、常见结构性失败」，与我们观察方向一致，但**没有文献精确复现「10 题 6 空壳」这一比例**——这是我们的独立实证，写入报告时标「本组实测」。[① arxiv.org/html/2512.01948v2 + arxiv.org/html/2610.29346]

**(b) judge 版本漂移**：同一批提交在 Gemini-2.5-Pro 榜和 GPT-5.5 榜分数不同，官方设双榜过渡期（2026-05-11 至 06-01）。任何引用 DRB 分数必须带 judge 版本，否则不可比。[① README]

**(c) 论文自报 vs 第三方**：② sm-bench-sota-table.json 记过官网 v1 / ICLR camera-ready / aiwiki 三源数字矛盾（contradictions.X1）；本轮未重新核三源差异，沿用该记录。

**(d) 相对评分的天花板效应**：RACE 依赖 reference 质量，reference 本身是单一专家产物；target 超过 reference 时的打分行为未在文档中明说 [待核验]。

---

## 3. 成本口径（每题 token 成本 / 时间）

公开数据极少且各家计费模型不同，以下为能查到的全部（[① paywithlocus.com/guides/deep-research-api，2026-11-10 核价] + [① hyperresearch.ai/alternatives/deep-research-pricing，2026-10-22 核价]）：

| 系统 | 计费方式 | 单题成本 | 单题耗时 |
|---|---|---|---|
| Gemini Deep Research | tokens + Google Search 工具费 | **$1–3**（Google 官方估计） | 数分钟，上限 60 min |
| Gemini Deep Research Max | 同上 | **$3–7**（官方估计） | 上限 60 min |
| OpenAI o3-deep-research (retired) | $10/M input + $40/M output + $10/千次 web search | 变动（token 计） | 未公布 |
| OpenAI o4-mini-deep-research (retired) | $2/M input + $8/M output + 搜索费 | 更低，变动 | 未公布 |
| Perplexity Agent API (high effort) | 模型 tokens + $0.0025/web search + $0.0005/page fetch | 变动 | 未公布 |
| Parallel Task API | 按 run 固定价 | $0.10–$2.40 | 2 min – 2 h |
| Exa Agent | 按 run | $0.012–$1.00 | 异步 |

**关键量化锚点（Google 官方口径）**：典型 Gemini DR 任务 ≈ **80 次搜索 query + 250K input tokens + 60K output tokens**；Max 版可达 160 次搜索 + 900K input tokens。[① paywithlocus]

**GPT-Researcher 本地跑**：无 token 成本（本地 27B），单题 ~90s–5min（② sm-bench-closed-sota-v3.md 粗估）。

**学术侧成本测量**：arXiv:2601.06007《Don't Break the Cache》在 DeepResearch Bench 上测 prompt caching 对 long-horizon agentic 任务的 API cost 与 time-to-first-token 影响（覆盖 OpenAI/Anthropic/Google 三家缓存策略）——这是目前唯一见到「在 DRB 上系统性测成本」的公开工作，具体数值本轮未提取，[待核验]（需要时拉全文）。

**诚实声明**：没有任何一家闭源厂商公布「每份报告的确定价格」——成本取决于 agent 自己决定读多少，账单事后才知道。引用成本数字时必须带「官方估计/第三方核价」标签。

---

## 4. 对我们本地 27B + prompt 管线的对标意义

### 4.1 合理基线选谁

分层结论（延续 ② competitor-survey.md §5.1 三层框架，结合本轮新证据修订）：

- **L1 主基线 = GPT-Researcher 开箱水平**（不变，且更强了）。理由更新：本轮确认它不在 DRB 官方榜（无法引榜上分数），意味着**唯一公平的 L1 对比是同题同 judge 自跑对照**——我们在 DRB n=10 子集上已经跑了 GR 臂（6/10 空壳），pfb 臂只要在同一子集同一 RACE judge 下跑，就是严格配对比较。这是论文主 claim 的可证伪载体。
- **L2 坐标参照 = 闭源 DRB 榜分数**（openai 47.84 / gemini 49.98 / perplexity 43.05，GPT-5.5 judge）。只引不跑，作用是给读者量感：我们离绝对 SOTA 多远。注意 Claude-3.7-Sonnet 裸模型 0.4218（② repo 内置 100 题全量）可作为「无 agent 框架的纯模型下界」参照。
- **L3 差异化 = 别人没有的维度**（decomp 前置质检 / 交叉验证置信度 / 内容核验三道闸）——本轮新增证据：GR 的 6/10 空壳恰好证明「无质量门禁的管道会静默产出无效报告」，这正是 decomp+gate 模块存在的理由。

### 4.2 比什么指标公平

1. **第一道闸：有效报告率**（非空壳率）。GR 60% 空壳说明端到端总分会被无效产出污染。任何系统先报「10 题里几题产出了 ≥N 字的有效报告」，再报分数。这是本轮最重要的方法学收获。
2. **RACE Overall + 四维分项**（comprehensiveness/insight/instruction-following/readability），同 judge（GPT-5.5）、同子集（n=10 调研型，中英各 5，分开报 zh/en 两组——Qwen 系中文有主场优势）。
3. **FACT valid_rate + effective citations**：citation grounding 是所有开源 DRA 的死穴（DREAM 结论），也是我们三道闸要解的维度——这一项 pfb 应该显著优于 GR，是最可能出 headline 的分项。
4. **成本/时间**：本地 27B 免费 vs 闭源 $1–7/题——报告里作为效率维度附报，不作主判据。
5. **不比的东西**：GAIA/BrowseComp/HLE 分数（题目类型不同：答案型 vs 报告型，且那些榜上是各家特调 agent 配置，不是产品默认形态）；DRACO 分数（Perplexity 主场，rubric 设计不同）。

### 4.3 风险与限定（写进 scoring.md 的话）

- 「打过 GPT-Researcher」≠「打过所有 deep research 系统」——跨 bench SOTA 是闭源 Gemini/Perplexity，我们跑不了也不该跑。
- n=10 子集方差大：对方闭源分数是 100 题均值，我们是 10 题子集，严格比较需同子集（目前无人公开 GR 在 DRB 的 100 题结果，所以我们的 n=10 自跑对照是唯一可行方案）。
- judge 受限风险：本机无 OpenRouter/OpenAI key 时 judge 降级为 qwen2.5-7b，结论须标「judge 受限，下界估计」（② sm-bench-closed-sota-v3.md 风险节）。

---

## Confidence 自评表

| 断言 | 来源档 | conf | 说明 |
|---|---|---|---|
| OpenAI DR 2026-07-23 retired，替代 gpt-5.6-sol | ① 官方 docs 页 | 0.95 | 两处独立页面一致 |
| 三家闭源均为单 agent 循环架构 | ① 官方 docs 描述 | 0.8 | 官方描述支持，但内部实现黑盒，不排除未公开的 sub-agent |
| DRB 新榜分数（47.84/49.98/43.05） | ② drb-leaderboard-gpt55.csv（上轮抓 HF Space） | 0.85 | JS 渲染页抓取，未二次核对当前值 |
| DRB 构造细节（100 题/22 域/96147 queries/reference 长度分布） | ① repo README + 实测数据统计 | 0.95 | 本地文件可直接复现 |
| RACE/FACT 协议与 judge 沿革 | ① repo README | 0.9 | 公式细节在 paper 正文，本轮未逐条核 |
| Gemini 典型任务 80 searches/250K in/60K out | ① paywithlocus（转述 Google 官方估计） | 0.7 | 二手转述，未直读 Google 原文 |
| GR 不在 DRB 官方榜 | ① repo raw_data 目录实测 | 0.9 | 目录列表为证，但不排除社区提交未被收录 |
| GR n=10 6 空壳 | ② 上轮实测记录（本轮未复跑） | 0.8 | 实测锚点，建议正式报告前复跑一次固化 |
| 空壳问题文献交叉（2512.01948 / 2610.29346 方向一致但未精确复现） | ① 摘要级阅读 | 0.6 | 只读了 abstract/开头，未核全文细节 |
| GAIA/HLE/BrowseComp 上各 DRA 具体分数 | — | [待核验] | 本轮未抓到，不编 |
| arXiv:2601.06007 的具体成本数值 | — | [待核验] | 只确认了存在性和测量对象，数值未提取 |
