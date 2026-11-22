# N43: 当 α=1.1 时，Pareto 分布的方差无穷大，导致总字节数 E[S] 对 X_min 极度敏感，需使用截断 Pareto 分布（截断上限 S_max）或数

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

当 α=1.1 时，Pareto 分布的方差无穷大，导致总字节数 E[S] 对 X_min 极度敏感，需使用截断 Pareto 分布（截断上限 S_max）或数值积分计算总字节数，避免解析解失效。

## Corrected Claim

当 α=1.1 时，Pareto 分布的方差无穷大，导致总字节数 E[S] 对 X_min 极度敏感，需使用截断 Pareto 分布（截断上限 S_max）或数值积分计算总字节数，避免解析解失效。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布当α≤2时方差无穷大，α=1.1满足此条件，导致矩估计失效，需截断或数值积分。
