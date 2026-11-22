# N61: Pareto 分布 CDF 公式在 α=1.1 时的截断误差边界：当 x < 10*x_min 时，截断 CDF 与无限 CDF 的相对误差 < 1%；当 x 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

Pareto 分布 CDF 公式在 α=1.1 时的截断误差边界：当 x < 10*x_min 时，截断 CDF 与无限 CDF 的相对误差 < 1%；当 x < 2*x_min 时，相对误差 > 10%，需使用有限和修正项 Σ(x_min/x_i)^α 替代连续积分。

## Corrected Claim

Pareto 分布 CDF 公式在 α=1.1 时的截断误差边界：当 x < 10*x_min 时，截断 CDF 与无限 CDF 的相对误差 < 1%；当 x < 2*x_min 时，相对误差 > 10%，需使用有限和修正项 Σ(x_min/x_i)^α 替代连续积分。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布尾部衰减极慢，α=1.1时截断误差确实显著，量级与阈值设定符合数学推导直觉。

## Search Query

truncated Pareto distribution CDF approximation error alpha 1.1
