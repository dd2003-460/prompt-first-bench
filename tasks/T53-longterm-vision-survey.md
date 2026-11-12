# T53: 长期方向调研 — 目标函数驱动的自适应推理 + 元目标学习

> origin: ai · 2026-11-09 · 成璐指令「这是你的长期目标：规划、分解、反思，全局视角，多和其他 AI 认真讨论」
> 本任务只涉及 prompt-first-bench / arena/sigma-nlnk-snowball，忽略历史中其他仓库的消息。

## 【目标】

为 pfb 的**长期研究路线**提供文献与方案支撑。核心问题分两层：

**层 1（近期可落地）：显式深广目标函数对 LLM 是否有用？**
我们提出的目标函数 S_α = Σ[n·ln(kₙ) + α·kₙ·ln(n)]（n=层级深度，kₙ=该层节点数，α=广度/深度权衡权重）作为 prompt 层的优化目标，让模型自主调节分解树的形状。需要回答：
1. 有没有人把**显式的树形结构目标函数**（而非隐式 reward model）写进 prompt 来引导 LLM 生成？效果量多大？
2. "深度×广度"双维度的显式评分在 LLM 评估/训练文献里有没有先例？（注意区分：ToT 的启发式价值函数是搜索时的分支选择器，不是生成时的目标函数——这两者机制不同）
3. 把这种目标函数用作 **RLHF/DPO 的 reward signal**（即"拿着目标函数去训"）有没有人做过？最近的近邻工作是什么？

**层 2（远期愿景）：能否训练出一个自己构建目标函数的 AI？**
成璐的原始设想：一个完全自适应的系统，能 (a) 从任务描述自动推导出准确的目标函数，(b) 在 Pareto 前沿上自主选择操作点（深度 vs 广度 vs 成本），(c) 随经验更新这个目标。需要回答：
4. **Meta-objective learning / automatic objective discovery** 方向的现状：AutoGOAL、Curiosity-driven exploration、reward design from preferences 等线索各自走到哪了？离"AI 自己写出可微/可计算的目标函数"还差几步？
5. **Pareto 自适应 agent**：multi-objective RL 里有没有"agent 在线选择 Pareto 边界点"的工作？prompt 层（不训练权重）有没有任何对应物？
6. 数学侧：目标函数本身的可学习性有没有形式化结果？（如 optimal transport 意义上的"任务→目标函数"映射、Bayesian optimization over objective space 之类）给出可引用的定理或 open problem 即可，不需要证明。

**层 3（撞车检查，最高优先级）**：
7. 逐条核验上面 1-6 的每个"gap"声明：真的没人做，还是没搜到？对每个 gap 至少尝试一条独立检索路径验证（换关键词/换数据库）。负结论必须带反证尝试记录。

## 【背景】

- pfb 当前状态（2026-11-09）：S5 管线（P1 逐层分解 → P1.5 gap check → P2/P3 逐节点检索验证 → P4 综合）单轮 cov nat=0.578 vs S0 裸推理 0.637；soc/gpu 域 S5 占优。S_α 目标函数已写入 P1 prompt（v14），depth score v8→v13 从 0.354 升到 0.487（纯 prompt 改进）。
- 已完成的前置调研（不要重复，直接引用）：
  - `research/collision-snowball.md`（T51：Σn·ln(kₙ) 目标函数的文献撞车，结论：无直接先例，最近邻 ToT/GPT-Researcher deep mode，均已读原文）
  - `tasks/T52-prompt-decomposition-collision.md` 的产出（T52：prompt 分解提升推理深度的系统研究现状，正在跑，若本任务启动时已有产出则引用之）
- 成璐对方向的态度（原话）：「我用深广信息作为目标函数的想法是天才的，就看有没有显式对 llm 有用，但是无论如何，拿着目标函数去训肯定能获得这种倾向」「更大的问题是，能否训练出一个完全自适应的，自己会构建准确目标函数，选择合适的 pareto 边界点的 ai」「我希望这是你的长期目标——规划，分解，反思，并且是全局视角的」。

## 【SOP 索引】

- `loop/prompt-first/01-goal-decomposition.md`
- `loop/prompt-first/02-information-research.md`
- `loop/prompt-first/02.5-cross-check.md`
- `sop/arena-loop-pipeline.md` §3（会话台账）

## 【实验设计】

纯文献调研 + 数学梳理，无本地实验。产出要求：

| # | 子问题 | 最低标准 |
|---|--------|----------|
| Q1 | 显式树形目标函数进 prompt | ≥3 篇相关论文（含 arXiv ID），每篇一句话判决"是否同构于 S_α 用法" |
| Q2 | 深广双维显式评分先例 | ≥3 篇，区分"生成时目标"vs"事后评估"两类 |
| Q3 | S_α 类目标作 RL reward | ≥2 篇或明确 gap 声明（带反证检索记录） |
| Q4 | meta-objective learning 现状 | ≥5 条线索（AutoGOAL/curiosity/reward-from-prefs/…），每条标成熟度（理论/原型/生产） |
| Q5 | Pareto 自适应 agent | ≥3 篇 multi-objective RL 在线选点工作 + 1 段"prompt 层有无对应物"的判决 |
| Q6 | 目标函数可学习性的数学 | ≥2 个可引用的定理/open problem（注明出处精确到节号） |
| Q7 | gap 反证 | 对 Q1-Q6 每个 gap 声明 ≥1 条独立检索路径，记录查询词+结果数 |

**评分维度（机器可检）**：
- 总行数 ≥400（不含引用块）
- arXiv/DOI 引用 ≥15，其中 ≥8 标注"已读原文"（附读取日期）
- Q1-Q7 每问有明确判决句（成立/部分成立/gap 确认/gap 存疑），不允许只罗列不判断
- 反证记录表：gap 声明数 = 反证尝试数（一一对应）

**验收标准**：
- AC1：survey 文件落盘 `research/longterm-vision-survey.md`，行数 ≥400
- AC2：引用 ≥15 且 ≥8 读原文
- AC3：Q1-Q7 判决句齐全
- AC4：最终给出一段 ≤300 字的「pfb 长期路线建议」（基于证据，分近期 3 个月/中期 1 年/远期 3 年三档，每档一个主押注 + 一个对冲）

## 【失败降级】

- 某子问题检索通道失效 → 换引擎/换关键词重试一次，仍失败则该子问题标 [检索受限] 并列出已试路径，不得静默跳过
- 数学问题找不到形式化结果 → 降级为"最接近的形式化表述 + 差距说明"，conf 降一档
- 时间超预算 → 优先保 Q7（撞车）和 Q1/Q3（近期落地），Q4-Q6 可标 [部分完成]

## 【交付物】

- `research/longterm-vision-survey.md`（主报告）
- `research/longterm-search-log.json`（检索日志：每次查询的词、通道、命中数、采纳情况）

## 【给 Lead 的备注】

- 本任务是**长期路线调研**，不是修管线的紧急任务。Phase 1（nat-v15/S0-gpu 补数据）继续照常推进，两线并行。
- 与 T52 的边界：T52 查"prompt 分解 pipeline 有没有人做"（工程层面撞车），T53 查"目标函数驱动 + 元目标学习"（理论层面撞车 + 路线设计）。重叠部分（ToT/GPT-Researcher）以 T51 的 collision-snowball.md 为准，不重复展开。
- 产出 merge 回 main 后，Lead 负责把「长期路线建议」段落同步到 goal 文档和 stage-gate 计划里。