# N132: f_min 的精确计算：基于截断 Pareto 分布均值公式 E[F] = (β * f_min) / (β - 1) * [1 - (f_min/f_max)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

f_min 的精确计算：基于截断 Pareto 分布均值公式 E[F] = (β * f_min) / (β - 1) * [1 - (f_min/f_max)^(β-1)]。由于 β=0.9 < 1，标准 Pareto 分布均值发散，必须使用截断分布。在 β<1 时，总请求量由头部主导，f_min 无法仅由 E[F] 唯一确定，需引入 f_max 或头部占比约束。假设头部 1% 对象贡献 50% 请求，可反推 f_min 与 f_max 的比值。

## Corrected Claim

f_min 的精确计算：基于截断 Pareto 分布均值公式 E[F] = (β * f_min) / (β - 1) * [1 - (f_min/f_max)^(β-1)]。由于 β=0.9 < 1，标准 Pareto 分布均值发散，必须使用截断分布。在 β<1 时，总请求量由头部主导，f_min 无法仅由 E[F] 唯一确定，需引入 f_max 或头部占比约束。假设头部 1% 对象贡献 50% 请求，可反推 f_min 与 f_max 的比值。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布均值公式正确，β<1时标准分布均值发散需截断，头部主导导致f_min非唯一确定需额外约束，逻辑自洽且符合统计学原理。
