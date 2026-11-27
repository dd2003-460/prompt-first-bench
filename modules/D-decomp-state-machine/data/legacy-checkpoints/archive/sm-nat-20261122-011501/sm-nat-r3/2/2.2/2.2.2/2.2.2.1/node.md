# N107: 截断误差项 ε 的精确解析式：对于 Pareto(α=1.1) 分布，截断均值 E[S|S<s_max] = (α*s_min)/(α-1) * (1 - (s

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

截断误差项 ε 的精确解析式：对于 Pareto(α=1.1) 分布，截断均值 E[S|S<s_max] = (α*s_min)/(α-1) * (1 - (s_min/s_max)^(α-1)) / (1 - (s_min/s_max)^α)。当 s_min=1KB, s_max=1GB 时，(s_min/s_max)^0.1 ≈ 0.5，E[S] ≈ 11 * 0.5 / 0.5 ≈ 11KB（需修正分母），实际 E[S]_trunc ≈ 10.5KB，误差项 ε = 1 - E[S]_trunc/E[S]_unbounded ≈ 5%。

## Corrected Claim

对于 Pareto(α=1.1) 分布，当 s_min=1KB, s_max=1GB 时，(s_min/s_max)^(α-1) ≈ 0.251。截断均值 E[S|S<s_max] 约为 1.1KB，而非 10.5KB。由于截断上限远小于无界均值的发散中心，截断误差项 ε 远大于 5%（实际上截断均值仅为无界理论均值的极小比例，若以截断均值近似无界均值，误差接近 100%）。

## Evidence

[质询]数值计算存在严重错误：当 s_min=1KB, s_max=1GB 时，s_min/s_max = 10^-6，其 0.1 次方应为 10^-0.6 ≈ 0.251，而非陈述中声称的 0.5；且截断均值公式推导及最终误差项 5% 的结论与基于该参数的实际计算结果（截断均值约为 1.1KB，误差远大于 5%）不符。 | 先验知识/题面给定，逻辑校验失败：数值量级与中间步骤计算错误，导致结论不可信。
