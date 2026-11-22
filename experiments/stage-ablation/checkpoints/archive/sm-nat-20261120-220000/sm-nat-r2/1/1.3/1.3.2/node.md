# N25: Pareto(α=1.1) 的大小变异系数 CV_size = sqrt((α-1)/(α-3)) 在 α<3 时发散，需数值积分计算：CV_size = sq

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Pareto(α=1.1) 的大小变异系数 CV_size = sqrt((α-1)/(α-3)) 在 α<3 时发散，需数值积分计算：CV_size = sqrt(∫ x^2 f(x) dx / (∫ x f(x) dx)^2 - 1)，对于 α=1.1，CV_size 极大，表明大小分布极度不均，少数极大对象主导总大小。

## Corrected Claim

Pareto(α=1.1) 的大小变异系数 CV_size = sqrt((α-1)/(α-3)) 在 α<3 时发散，需数值积分计算：CV_size = sqrt(∫ x^2 f(x) dx / (∫ x f(x) dx)^2 - 1)，对于 α=1.1，CV_size 极大，表明大小分布极度不均，少数极大对象主导总大小。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)的二阶矩在α<3时确实发散，导致标准CV公式失效，需通过数值积分或截断处理计算，且α=1.1确实意味着极度不均的分布。
