# N53: 更新对象在缓存中的平均驻留时间 T_res_avg 的计算公式为 T_res_avg = ∫_0^∞ t * f_T(t) dt，其中 f_T(t) 为更新对象

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

更新对象在缓存中的平均驻留时间 T_res_avg 的计算公式为 T_res_avg = ∫_0^∞ t * f_T(t) dt，其中 f_T(t) 为更新对象在 LRU 缓存中的驻留时间分布，受热度分布和更新率共同影响，具体数值需通过模拟确定。

## Corrected Claim

更新对象在缓存中的平均驻留时间 T_res_avg 的计算公式为 T_res_avg = ∫_0^∞ t * f_T(t) dt，其中 f_T(t) 为更新对象在 LRU 缓存中的驻留时间分布，受热度分布和更新率共同影响，具体数值需通过模拟确定。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合期望值定义，驻留时间受热度与更新率影响符合LRU缓存基本原理。

## Search Query

average residence time of updated objects in LRU cache
