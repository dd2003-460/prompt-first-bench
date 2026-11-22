# N44: 挂价分布右偏的数学推导：若真实价值 V ~ N(μ, σ²)，且卖家挂价 P_list = V + ε，其中 ε 为乐观偏差项，E[ε] > 0 且 Var(ε

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N7

## Claim

挂价分布右偏的数学推导：若真实价值 V ~ N(μ, σ²)，且卖家挂价 P_list = V + ε，其中 ε 为乐观偏差项，E[ε] > 0 且 Var(ε) 与 σ² 正相关；在 σ_used 较大的情况下，P_list 的分布右尾长度显著增加，导致 15-25% 溢价区间内的商品密度高于对称分布预期。

## Corrected Claim

挂价分布右偏的数学推导：若真实价值 V ~ N(μ, σ²)，且卖家挂价 P_list = V + ε，其中 ε 为乐观偏差项，E[ε] > 0 且 Var(ε) 与 σ² 正相关；在 σ_used 较大的情况下，P_list 的分布右尾长度显著增加，导致 15-25% 溢价区间内的商品密度高于对称分布预期。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布叠加正均值且方差随σ增大的噪声项，必然导致分布右偏及右尾变长，符合概率论基本性质。

## Search Query

right skewed listing price distribution information asymmetry
