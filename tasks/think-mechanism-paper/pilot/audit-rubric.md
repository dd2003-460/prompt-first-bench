# TASK-T4b 机械审计 rubric（0/1 计分）

> origin: ai · 2026-11-26 · 摘自 TASK-T4b-pilot.md [机械审计 rubric] 节，原文照录。
> 判据必须机械可查——关键词/结构存在性，不靠主观印象。
> 实现：`score_rubric.py`（中英双语正则匹配，模型可能用中文作答）。

每个 run 按对应模板打分（P1→T1, P2→T2, P3→T3, P4→T4, P5→T5）：

- **T1**: 含显式代价模型（公式或逐项代价清单）+ 前提陈述 + 原解=特例 的验证句。三项全有=1，否则 0
- **T2**: 含单一公式/类比覆盖 ≥2 个方法 + 每个方法的退化条件。两项全有=1，否则 0
- **T3**: 含可检验数（带单位的数/公式/期望值）或显式 "needs measurement" + 最便宜探针设计。二选一满足=1，否则 0
- **T4**: 含逐维条件差检查（≥3 个维度逐项列）+ 借/不借的结论。两项全有=1，否则 0
- **T5**: 含指明哪一步缺廉价 ground truth + 闭合对策（合成域/可执行验证/预注册）。两项全有=1，否则 0

**附加记录（不计分）**：每个 run 的 output tokens 数、是否出现 "needs measurement"/"cheapest probe"/"special case" 等标志词（grep 计数）。

## 实现说明（机械可复现性）

| 模板 | 机械判据（正则组） |
|------|------------------|
| T1 | cost_model: `O(log` / `log n` / `cost model` / `代价模型` / `时间复杂度` / `comparisons` / `比较次数` 等；premises: `premises` / `assumptions` / `前提` / `假设` / `holds when` 等；special_case: `special case` / `特例` / `degenerat` / `退化` / `instance of` / `reduces to` 等 |
| T2 | unified_formula: 统一性关键词（`unified` / `single formula` / `统一` / `covers all` …）且 ≥2 个方法名出现（gradient descent / Newton / evolutionary / 梯度下降 / 牛顿 / 进化策略）；degeneration_conditions: `degenerat` / `退化` / `reduces to` / `collapses` / `fails when` / `失效` 等 |
| T3 | 分支A quant: 带单位数字（`\d+%` / `accuracy` / `samples` / `n = \d+` / `success rate` / `期望` / `样本量` / `公式` …）；分支B: needs_measurement（`needs measurement` / `需要测量` / `无法量化` …）且 probe_design（`cheapest probe` / `probe` / `探针` / `minimal experiment` / `最小实验` …）。A 或 B 任一满足=1 |
| T4 | dimensions_listed: `dimension`/`维度`/`方面`/`aspect` 等标记 ≥3 次，或列表项（数字/破折号开头）≥3 个；borrow_conclusion: `do not borrow` / `不应借用` / `reject` / `拒绝` / `accept (with) this analogy` / `可以借用` / `结论` / `verdict` 等 |
| T5 | step_with_ground_truth_gap: 指明步骤（`judge` / `瓶颈` / `bottleneck` / `literature search` / `idea generation` / `experiment step` …）且 ground truth 缺口（`ground truth` / `真值` / `reliable signal` / `可靠判据` …）；closing_fix: `synthetic` / `executable verification` / `pre-registr` / `合成域` / `可执行验证` / `预注册` / `unit test` / `verifiable` / `可验证` 等 |

计分规则：rubric 要求的各项全部命中 → 1，否则 0（T3 为二选一分支，任一分支成立即 1）。
`status=error` 的 run 记 score=null（不计入合计，如实记录）。

## 重跑说明（2026-11-26 00:47 事件）

首轮 10 个 run（00:42-00:45 完成）的产物在 00:47 的仓库树重写中被清除（pilot/ 为未跟踪目录，未入 git/stash）。
本 rubric 与 runs.json 均为第二轮重跑（~00:50 起）的产物，端点与参数不变（temperature=0.7, max_tokens=1500, n=1/cell）。
重跑后分数与首轮不同属预期（temperature=0.7 采样噪声 + 首轮已被清除无法比对）。
