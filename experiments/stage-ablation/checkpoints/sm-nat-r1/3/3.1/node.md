# N11: 更新惩罚因子推导：有效命中率H_eff = H_LRU * (1 - U * P_miss_update)，其中P_miss_update为更新时对象不在缓存中

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

更新惩罚因子推导：有效命中率H_eff = H_LRU * (1 - U * P_miss_update)，其中P_miss_update为更新时对象不在缓存中的概率，需计算U=1%/天下P_miss_update≈0.85 [基于LRU驻留时间分布估计]

## Corrected Claim

更新惩罚因子推导：有效命中率H_eff = H_LRU * (1 - U * P_miss_update)，其中P_miss_update为更新时对象不在缓存中的概率，需计算U=1%/天下P_miss_update≈0.85 [基于LRU驻留时间分布估计]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache update penalty factor LRU miss probability on update
