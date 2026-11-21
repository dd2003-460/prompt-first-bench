# 过程/深度细颗粒度评测调研：私有小规模 bench + 树结构指标（2026-11-21）

> origin: ai · 2026-11-21 · 触发：D 问"相当于私有小规模 bench，但可以针对过程和深度细颗粒度打分？这种 bench 方法有吗，相关论文有吗"
> 范围：两条线——① rubric 化深度研究评测（对产物细粒度打分）② process reward / step-level（对过程打分）。
> 方法：local-first 检查（pfb/lit-survey 无覆盖、competitor-survey.md 已有 DRACO/ResearchRubrics 条目但无论文级细节）→ arXiv API 实时拉取（来源①，本轮工具输出）。
> 置信度：所有 arXiv ID/日期/摘要来自 arXiv API 本轮返回；论文自报数字未独立复现 [待交叉验证]。
> D 指示（2026-11-21）：撞车也落盘——撞车论文 = 套磁对象，撞车不是坏事。

## §1 结论先行

我们的方法（私有 3 题 × 阶段消融 × 分解树 depth/coverage 结构指标）卡在两条成熟路线的**缝隙**里：
- 路线一（rubric bench）量**最终报告**——rubric 再细也是对产物的细粒度，不是对过程的；
- 路线二（PRM / step-level）量**轨迹步骤**——但为 RL 训练服务，多数要 ground truth 或无监督训练管线。

缝隙 = "私有小规模题集 + 管线阶段消融（每阶段边际贡献）+ 树结构深度作为一等指标"。
本轮检索未见占位的发表工作（conf 0.7，检索词有限，非穷尽）。

## §2 路线一：rubric 化深度研究评测（5 篇，最接近我们形态）

**1. ResearchRubrics** — arXiv:2511.07685（2025-11-10）
101 个领域多样化 prompt + 2500+ 专家手写细粒度 rubric（2800+ 人工小时），评 factual grounding / reasoning soundness / clarity。
复杂度框架三轴：conceptual breadth / **logical nesting** / exploration。
**与我们的关系：logical nesting 轴 ≈ 我们的 depth 分概念（推理嵌套深度），是最直接的指标近邻。套磁首选。**

**2. DeepResearch Bench II** — arXiv:2601.08536（2026-01-13，v3）
132 个 grounded 任务 × 22 领域，9430 条细粒度**二元** rubric，从专家调查报告经 4 阶段 LLM+human 管线反推。
三维：information recall / analysis / presentation。
**与我们的关系：rubric 从专家报告反推 ≈ 我们从 gold 树反推 coverage 判据；二元 rubric 的"可验证性"设计值得抄（我们的 coverage 节点判定也是二元：命中/未命中）。**

**3. FinResearchBench II** — arXiv:2607.12252（2026-07-14，v2）
104 题，自动合成 14450 条候选 rubric → 共识筛选出 gold rubric；3 专家 vs 3-LLM judge panel 对照，
98.67% 标签级一致（jointly unanimous 项）→ 证明 LLM judge 可替代专家**执行** rubric。
**与我们的关系：给"judge 用 qwen3.8-27b 单模型（non-IRR）"提供了文献背书路径——若被质疑 judge 可靠性，可引此篇做 judge panel 一致性验证。**

**4. DEEPRUBRIC** — arXiv:2606.17029（2026-05-20，v2）
evidence-tree 结构的 rubric 监督：先确定"证据支撑的报告应被评什么"，再反向合成 query-rubric 对；
rubric 挂在证据树上而非平铺清单。
**与我们的关系：结构上最像——rubric/判据挂在树上，跟我们的"gold 树 + 节点级 coverage"同构。套磁次选。**

**5. Dr.Credit** — arXiv:2609.34296（2026-09-28）
rubric-grounded 过程信用分配：用 rubric 做共享参照，给轨迹里每个中间决策算贡献；
区分"新证据"vs"轨迹中已有证据"，支持部分满足。
**与我们的关系：最接近"对过程细颗粒度打分"的单篇；我们的阶段消融（每阶段边际贡献）是它的粗粒度版本。套磁三选。**

## §3 路线二：process reward / step-level（服务 RL，方法可借）

- **ScalePRM** — 2512.03244：无 ground truth 训练 PRM（scaling verification compute）。
- **FreePRM** — 2506.03570：无过程标签训练 PRM。
- **GPRM** — 2611.20755（2026-11-16，最新）：全局视角 PRM。
- **Hard2Verify** — 2510.13744：开放题步骤级验证基准（frontier math）。
- **PRO-Step** — 2609.01658：RAG 场景 step-level 过程奖励优化。
- **Truncated Step-Level Sampling** — 2602.23440：RAG 推理的过程奖励采样。

**与我们的关系：这条线不占我们的缝隙（目标函数是 RL reward 不是评测），但"无 ground truth 的过程分"
（ScalePRM/FreePRM）是 depth 分未来若要脱离 gold 树、做成自动指标时的方法储备。**

## §4 我们的定位（投稿/对标叙事）

| 尺子 | 量什么 | 谁占位 |
|---|---|---|
| 公开 rubric bench（§2） | 最终报告质量（细粒度 rubric） | ResearchRubrics / DRB II / FinRB II |
| PRM / step-level（§3） | 轨迹步骤（RL 服务） | ScalePRM / FreePRM / Dr.Credit |
| **自研（我们）** | **管线阶段边际贡献 + 树结构 depth/coverage** | 未见占位（conf 0.7） |

competitor-survey.md §5.2 已有定位句："自研 ablation 回答『为什么强』，公开 bench 回答『有多强』"。
本调研补上理论锚点：depth 指标最近邻 = ResearchRubrics 的 logical nesting 轴；
阶段边际贡献最近邻 = Dr.Credit 的 rubric-grounded credit（粗粒度版）。

## §5 套磁名单（D 指示：撞车 = 社交资产）

按缝隙接近度排序：
1. **ResearchRubrics**（2511.07685）— logical nesting 轴与 depth 分撞概念；问他们 nesting 轴怎么操作化打分。
2. **Dr.Credit**（2609.34296）— 过程信用分配，2026-09 很新；问开放题无 gold 时 rubric 参照的失效边界。
3. **DEEPRUBRIC**（2606.17029）— 树上挂 rubric 与我们 gold 树同构；问 evidence-tree 的构建成本。
4. **FinResearchBench II**（2607.12252）— judge panel 一致性方法可借；套磁价值低但方法可抄。

套磁切入点（统一叙事）：我们在做"管线阶段消融 + 分解树结构指标"的私有评测，
发现与贵文 X 轴/机制概念相邻，想请教 Y 问题 + 分享我们的 T53b 结果（3 题 × 2 臂 × 10 轮，
formula 臂 depth +0.113 p=0.008 / coverage +0.186 p=0.006，27b 本地模型）。

## §6 检索记录（可复现）

- arXiv API（https://export.arxiv.org/api/query），2026-11-21 本轮：
  - `all:"deep research" AND all:"rubric"` → 10 条，取 §2 五篇
  - `all:"step-level" AND all:"process reward" AND cat:cs.CL` → 8 条，取 §3 六篇
  - `all:"reasoning tree" AND all:"evaluation" AND all:"depth"` → 1 条（无关，排除）
- 未穷尽：未查 OpenReview/ACL Anthology 非 arXiv 渠道；未查 2024 前 PRM 经典（Math-Shepherd/PRM800K，凭记忆未本轮验证 [待核验]）。
