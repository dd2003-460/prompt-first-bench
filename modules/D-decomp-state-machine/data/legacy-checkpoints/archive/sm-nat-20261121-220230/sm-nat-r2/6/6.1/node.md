# N87: Pareto(α=1.1) 分布的期望值 E[s] 在数学上发散（因为 α≤1），N26 中使用的 E[s]=11KB 是基于截断上限 s_max 的有限样本均

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

Pareto(α=1.1) 分布的期望值 E[s] 在数学上发散（因为 α≤1），N26 中使用的 E[s]=11KB 是基于截断上限 s_max 的有限样本均值，其精确值需通过积分 ∫_{s_min}^{s_max} s * f(s) ds 计算，其中 s_max 需设定为 100MB 以反映 CDN 对象实际上限。

## Corrected Claim

Pareto(α=1.1) 分布的期望值 E[s] 在数学上发散（因为 α≤1），N26 中使用的 E[s]=11KB 是基于截断上限 s_max 的有限样本均值，其精确值需通过积分 ∫_{s_min}^{s_max} s * f(s) ds 计算，其中 s_max 需设定为 100MB 以反映 CDN 对象实际上限。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布α≤1时期望发散是数学定理，截断后期望有限且需积分计算符合定义，100MB作为CDN对象上限在工程上合理。
