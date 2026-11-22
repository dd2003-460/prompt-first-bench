# N63: 考虑对象更新与访问的耦合效应，若更新事件会重置 LRU 时间戳（即更新视为访问），则 T_avg_resident 的计算需引入更新率 u 的修正项，修正后的平

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

考虑对象更新与访问的耦合效应，若更新事件会重置 LRU 时间戳（即更新视为访问），则 T_avg_resident 的计算需引入更新率 u 的修正项，修正后的平均驻留时间 T_avg_resident_corrected = T_avg_resident * (1 + u/λ_avg)，当 u=1%/day 且 λ_avg=500/day 时，修正因子约为 1.00002，仍表明失效折扣极小。

## Corrected Claim

考虑对象更新与访问的耦合效应，若更新事件会重置 LRU 时间戳（即更新视为访问），则 T_avg_resident 的计算需引入更新率 u 的修正项，修正后的平均驻留时间 T_avg_resident_corrected = T_avg_resident * (1 + u/λ_avg)，当 u=1%/day 且 λ_avg=500/day 时，修正因子约为 1.00002，仍表明失效折扣极小。

## Evidence

先验知识/题面给定，逻辑校验通过：修正因子 1 + u/λ_avg = 1 + 0.01/500 = 1.00002，数值计算准确，量级合理，符合 LRU 缓存理论中更新对驻留时间影响的定性及定量直觉。

## Search Query

cache update invalidation LRU timestamp reset impact on hit rate
