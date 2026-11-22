# N31: Pareto(α=1.1) 大小分布的理论均值 E[size] 在 x_min > 0 时发散（因 α ≤ 1），必须引入截断上限 S_max 或截断下限 S_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

Pareto(α=1.1) 大小分布的理论均值 E[size] 在 x_min > 0 时发散（因 α ≤ 1），必须引入截断上限 S_max 或截断下限 S_min 才能计算有限均值，否则 N6 中'确保 E[size] 有限'的前提不成立。

## Corrected Claim

Pareto(α=1.1) 大小分布的理论均值 E[size] 在 x_min > 0 时发散（因 α ≤ 1），必须引入截断上限 S_max 或截断下限 S_min 才能计算有限均值，否则 N6 中'确保 E[size] 有限'的前提不成立。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布（α≤1）的期望值在数学上确实发散，需截断方可有限，符合第一性原理。
