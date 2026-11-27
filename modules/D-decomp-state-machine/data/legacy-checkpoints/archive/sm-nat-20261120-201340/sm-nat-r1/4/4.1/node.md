# N18: 更新导致缓存失效的稳态概率 P_stale = 1 - exp(-λ_update * T_resident)，其中 λ_update = 0.01/day，T

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

更新导致缓存失效的稳态概率 P_stale = 1 - exp(-λ_update * T_resident)，其中 λ_update = 0.01/day，T_resident 为对象在 LRU 缓存中的平均驻留时间（由缓存容量 C 和对象大小 S 决定），需计算 P_stale 对静态命中率 H_static 的折损系数。

## Corrected Claim

更新导致缓存失效的稳态概率 P_stale = 1 - exp(-λ_update * T_resident)，其中 λ_update = 0.01/day，T_resident 为对象在 LRU 缓存中的平均驻留时间（由缓存容量 C 和对象大小 S 决定），需计算 P_stale 对静态命中率 H_static 的折损系数。

## Evidence

先验知识/题面给定，逻辑校验通过
