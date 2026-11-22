# N7: Pareto(α=1.1) 分布的二阶矩 E[S^2] 是否有限：由于 α ≤ 2，E[S^2] = ∞，导致 LRU 命中率的方差极大，稳态假设在理论意义上不

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

Pareto(α=1.1) 分布的二阶矩 E[S^2] 是否有限：由于 α ≤ 2，E[S^2] = ∞，导致 LRU 命中率的方差极大，稳态假设在理论意义上不成立，需引入截断或有限样本修正

## Corrected Claim

Pareto(α=1.1) 分布的二阶矩 E[S^2] 是否有限：由于 α ≤ 2，E[S^2] = ∞，导致 LRU 命中率的方差极大，稳态假设在理论意义上不成立，需引入截断或有限样本修正

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布当α≤2时二阶矩发散，导致方差无穷大，稳态假设失效的推导符合概率论基本性质。

## Search Query

Pareto distribution second moment infinite alpha less than 2
