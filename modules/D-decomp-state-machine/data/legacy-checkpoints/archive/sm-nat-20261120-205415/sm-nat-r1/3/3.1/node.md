# N13: LFU 最大增益 = (LFU 字节命中率 - LRU 字节命中率) * 100%；LFU 通过频率排序缓存对象，不受时间局部性影响，在 Pareto 热度分布

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 最大增益 = (LFU 字节命中率 - LRU 字节命中率) * 100%；LFU 通过频率排序缓存对象，不受时间局部性影响，在 Pareto 热度分布下，LFU 缓存对象与 LRU 不同，增益源于避免缓存低频大对象

## Corrected Claim

LFU 最大增益 = (LFU 字节命中率 - LRU 字节命中率) * 100%；LFU 通过频率排序缓存对象，不受时间局部性影响，在 Pareto 热度分布下，LFU 缓存对象与 LRU 不同，增益源于避免缓存低频大对象

## Evidence

先验知识/题面给定，逻辑校验通过
