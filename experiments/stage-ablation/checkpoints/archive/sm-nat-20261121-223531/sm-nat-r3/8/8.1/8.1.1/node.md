# N209: 对象大小分布采用 Pareto(α=1.1) 模型，概率密度函数 f_S(s) = α * s_min^α / s^(α+1)，其中 s_min = 1KB。该

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

对象大小分布采用 Pareto(α=1.1) 模型，概率密度函数 f_S(s) = α * s_min^α / s^(α+1)，其中 s_min = 1KB。该分布的截断均值 E[S] 在 α < 2 时由下界 s_max 主导，需计算具体截断均值以替代发散的理论均值。

## Corrected Claim

对象大小分布采用 Pareto(α=1.1) 模型，概率密度函数 f_S(s) = α * s_min^α / s^(α+1)，其中 s_min = 1KB。该分布的截断均值 E[S] 在 α < 2 时由下界 s_max 主导，需计算具体截断均值以替代发散的理论均值。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)在α<2时理论均值发散，截断均值确实由上界s_max主导，数学推导自洽。

## Search Query

Pareto distribution truncated mean alpha < 2
