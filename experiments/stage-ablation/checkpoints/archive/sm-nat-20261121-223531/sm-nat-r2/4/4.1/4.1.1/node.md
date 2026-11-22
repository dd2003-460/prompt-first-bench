# N52: 更新导致的无效缓存占用比例 = (1 - e^{-λ_upd * T_res_avg}) * (更新对象在缓存中的字节占比)，其中 T_res_avg 为更新对

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

更新导致的无效缓存占用比例 = (1 - e^{-λ_upd * T_res_avg}) * (更新对象在缓存中的字节占比)，其中 T_res_avg 为更新对象在缓存中的平均驻留时间，λ_upd=1%/天，更新对象字节占比需通过 Pareto 分布计算。

## Corrected Claim

更新导致的无效缓存占用比例 = (1 - e^{-λ_upd * T_res_avg}) * (更新对象在缓存中的字节占比)，其中 T_res_avg 为更新对象在缓存中的平均驻留时间，λ_upd=1%/天，更新对象字节占比需通过 Pareto 分布计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache invalidation ratio update rate average residence time
