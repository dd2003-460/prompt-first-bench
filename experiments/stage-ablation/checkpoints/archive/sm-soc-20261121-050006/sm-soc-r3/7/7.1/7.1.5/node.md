# N322: 相关系数 ρ 的显著性检验：t 统计量 = ρ * sqrt((n-2) / (1 - ρ^2))，其中 n 为时间窗口数量；若 t 值 > t_{0.05, 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102, N103, N104

## Claim

相关系数 ρ 的显著性检验：t 统计量 = ρ * sqrt((n-2) / (1 - ρ^2))，其中 n 为时间窗口数量；若 t 值 > t_{0.05, n-2}（如 n=50 时 t > 2.01），则拒绝 ρ=0 的原假设，支持同源性假设；若 n < 30，则检验功效不足，需改用 Fisher Z 变换或 Bootstrap 方法估计 ρ 的置信区间，此时置信度提升至 0.75 的条件需附加 n ≥ 30 的样本量约束。

## Corrected Claim

相关系数 ρ 的显著性检验：t 统计量 = ρ * sqrt((n-2) / (1 - ρ^2))，其中 n 为时间窗口数量；若 t 值 > t_{0.05, n-2}（如 n=50 时 t > 2.01），则拒绝 ρ=0 的原假设，支持同源性假设；若 n < 30，则检验功效不足，需改用 Fisher Z 变换或 Bootstrap 方法估计 ρ 的置信区间，此时置信度提升至 0.75 的条件需附加 n ≥ 30 的样本量约束。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Pearson correlation significance test small sample bootstrap
