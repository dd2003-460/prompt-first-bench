# N15: 动态更新导致的缓存失效概率 P_invalid 由更新率 u=1%/天、对象平均存活时间 T_life 和 LRU 驱逐延迟决定，具体表达式为 P_invali

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

动态更新导致的缓存失效概率 P_invalid 由更新率 u=1%/天、对象平均存活时间 T_life 和 LRU 驱逐延迟决定，具体表达式为 P_invalid ≈ 1 - exp(-u * T_life / T_LRU_avg)，其中 T_LRU_avg 是对象在 LRU 队列中的平均驻留时间，需通过工作负载的访问间隔分布计算。

## Corrected Claim

动态更新导致的缓存失效概率 P_invalid 由更新率 u=1%/天、对象平均存活时间 T_life 和 LRU 驱逐延迟决定，具体表达式为 P_invalid ≈ 1 - exp(-u * T_life / T_LRU_avg)，其中 T_LRU_avg 是对象在 LRU 队列中的平均驻留时间，需通过工作负载的访问间隔分布计算。

## Evidence

先验知识/题面给定，逻辑校验通过
