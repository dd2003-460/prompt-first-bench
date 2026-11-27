# N41: 缓存污染惩罚项 P_pollution 的分母 ∑_{i=1}^{k_max} S_i 的精确计算：该和为前 k_max 个最大对象的总大小，由于热门对象较小，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

缓存污染惩罚项 P_pollution 的分母 ∑_{i=1}^{k_max} S_i 的精确计算：该和为前 k_max 个最大对象的总大小，由于热门对象较小，k_max 由热度排名决定，需结合 Pareto 大小分布和热度分布联合计算，量化为 ∑_{i=1}^{k_max} S_i ≈ k_max * E[S|rank≤k_max]。

## Corrected Claim

缓存污染惩罚项 P_pollution 的分母 ∑_{i=1}^{k_max} S_i 的精确计算：该和为前 k_max 个最大对象的总大小，由于热门对象较小，k_max 由热度排名决定，需结合 Pareto 大小分布和热度分布联合计算，量化为 ∑_{i=1}^{k_max} S_i ≈ k_max * E[S|rank≤k_max]。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式是条件期望的数学恒等式（总和等于项数乘以条件均值），量纲一致，逻辑自洽。
