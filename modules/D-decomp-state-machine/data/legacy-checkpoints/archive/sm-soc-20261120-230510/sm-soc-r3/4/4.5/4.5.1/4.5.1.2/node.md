# N236: 剩余商品最高价值 V_new_best 的估计：V_new_best = P_median * 1.05 * (1 + z_low * σ_low)，其中 z_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

剩余商品最高价值 V_new_best 的估计：V_new_best = P_median * 1.05 * (1 + z_low * σ_low)，其中 z_low 为剩余商品在截断正态分布中的分位数（典型值 z=1.0-1.5），σ_low 为剩余商品估值标准差（典型值 0.08-0.15），需计算降权后剩余集合的分布参数。

## Corrected Claim

剩余商品最高价值 V_new_best 的估计：V_new_best = P_median * 1.05 * (1 + z_low * σ_low)，其中 z_low 为剩余商品在截断正态分布中的分位数（典型值 z=1.0-1.5），σ_low 为剩余商品估值标准差（典型值 0.08-0.15），需计算降权后剩余集合的分布参数。

## Evidence

先验知识/题面给定，逻辑校验通过
