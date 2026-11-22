# N16: 更新导致的缓存失效概率 P_inval = 1 - (1 - u)^T，其中 u=0.01 为日更新率，T 为对象在 LRU 缓存中的平均驻留时间（小时）；需基

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

更新导致的缓存失效概率 P_inval = 1 - (1 - u)^T，其中 u=0.01 为日更新率，T 为对象在 LRU 缓存中的平均驻留时间（小时）；需基于 Pareto(β=0.9) 热度分布计算 T 的分布及均值

## Corrected Claim

更新导致的缓存失效概率 P_inval = 1 - (1 - u)^T，其中 u=0.01 为日更新率，T 为对象在 LRU 缓存中的平均驻留时间（小时）；需基于 Pareto(β=0.9) 热度分布计算 T 的分布及均值

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P_inval = 1 - (1 - u)^T 符合独立事件概率推导，量纲与逻辑自洽。
