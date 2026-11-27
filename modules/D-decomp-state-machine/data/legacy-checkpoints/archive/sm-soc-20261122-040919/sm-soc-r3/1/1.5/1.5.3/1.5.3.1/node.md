# N182: 共享随机源：市场均价 P_market_avg 的估计误差分布，定义为 N(μ_avg, σ²_avg)，其中 μ_avg 为同类商品近期成交均价，σ²_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N47

## Claim

共享随机源：市场均价 P_market_avg 的估计误差分布，定义为 N(μ_avg, σ²_avg)，其中 μ_avg 为同类商品近期成交均价，σ²_avg 为价格离散度。该随机源同时影响 exp 项的分母和基准概率 P(consult|base) 的校准。

## Corrected Claim

共享随机源：市场均价 P_market_avg 的估计误差分布，定义为 N(μ_avg, σ²_avg)，其中 μ_avg 为同类商品近期成交均价，σ²_avg 为价格离散度。该随机源同时影响 exp 项的分母和基准概率 P(consult|base) 的校准。

## Evidence

先验知识/题面给定，逻辑校验通过
