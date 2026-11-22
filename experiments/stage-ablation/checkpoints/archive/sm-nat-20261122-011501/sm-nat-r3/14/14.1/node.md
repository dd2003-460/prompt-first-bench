# N190: 缓存内更新对象命中失效的精确概率 P_hit_inval：每天 1000 个对象更新（1% * 100,000）。这些更新对象落在 LRU 驻留集合（Top K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

缓存内更新对象命中失效的精确概率 P_hit_inval：每天 1000 个对象更新（1% * 100,000）。这些更新对象落在 LRU 驻留集合（Top K_LRU）中的概率为 P_update_in_cache = K_LRU / N_objects ≈ 15,000 / 100,000 = 15%（假设更新对象均匀分布在所有对象中，无热度偏向）。因此每天约有 1000 * 0.15 = 150 个对象在缓存中发生版本更新。

## Corrected Claim

缓存内更新对象命中失效的精确概率 P_hit_inval：每天 1000 个对象更新（1% * 100,000）。这些更新对象落在 LRU 驻留集合（Top K_LRU）中的概率为 P_update_in_cache = K_LRU / N_objects ≈ 15,000 / 100,000 = 15%（假设更新对象均匀分布在所有对象中，无热度偏向）。因此每天约有 1000 * 0.15 = 150 个对象在缓存中发生版本更新。

## Evidence

先验知识/题面给定，逻辑校验通过：基于均匀分布假设，概率计算（15%）及期望值推导（150）在数学上自洽且量级合理。
