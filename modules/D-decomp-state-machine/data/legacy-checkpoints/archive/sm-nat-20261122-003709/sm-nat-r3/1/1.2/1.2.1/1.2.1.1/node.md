# N106: Pareto(α=1.1)分布截断均值 E[S] 的正确解析公式为 E[S] = (α * s_min) / (α - 1) * [1 - (s_min/s_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Pareto(α=1.1)分布截断均值 E[S] 的正确解析公式为 E[S] = (α * s_min) / (α - 1) * [1 - (s_min/s_max)^(α-1)] / [1 - (s_min/s_max)^α]，其中 α=1.1, s_min=1KB, s_max=1GB，需代入计算验证正负号。

## Corrected Claim

Pareto(α=1.1)分布截断均值 E[S] 的正确解析公式为 E[S] = (α * s_min) / (α - 1) * [1 - (s_min/s_max)^(α-1)] / [1 - (s_min/s_max)^α]，其中 α=1.1, s_min=1KB, s_max=1GB，需代入计算验证正负号。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式为截断帕累托分布均值的正确解析解，量纲与数值范围合理（α>1时截断均值小于无截断均值，且为正数）。
