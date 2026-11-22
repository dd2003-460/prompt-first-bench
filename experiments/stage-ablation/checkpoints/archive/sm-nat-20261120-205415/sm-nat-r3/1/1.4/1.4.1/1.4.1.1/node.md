# N108: Pareto(α=1.1) 分布的期望收敛性约束：由于 α=1.1 < 2，二阶矩 E[S²] 发散，导致方差 Var[S] 不存在，这使得基于中心极限定理的正

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Pareto(α=1.1) 分布的期望收敛性约束：由于 α=1.1 < 2，二阶矩 E[S²] 发散，导致方差 Var[S] 不存在，这使得基于中心极限定理的正态近似在计算截断分布 E[S|S≤S_max] 时失效，必须使用截断 Pareto 的精确积分形式。

## Corrected Claim

Pareto(α=1.1) 分布的期望收敛性约束：由于 α=1.1 < 2，二阶矩 E[S²] 发散，导致方差 Var[S] 不存在，这使得基于中心极限定理的正态近似在计算截断分布 E[S|S≤S_max] 时失效，必须使用截断 Pareto 的精确积分形式。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布α<2时二阶矩发散，方差确实不存在，导致标准CLT正态近似失效，需使用截断分布精确积分。
