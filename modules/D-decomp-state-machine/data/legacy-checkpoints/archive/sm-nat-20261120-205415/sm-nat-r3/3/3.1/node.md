# N13: LFU 最大增益 = (LFU 字节命中率 - LRU 字节命中率) * 100%；LFU 通过频率排序缓存对象，不受时间局部性影响，在 Pareto 热度分布

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 最大增益 = (LFU 字节命中率 - LRU 字节命中率) * 100%；LFU 通过频率排序缓存对象，不受时间局部性影响，在 Pareto 热度分布下，LFU 缓存对象与 LRU 不同，增益源于避免缓存低频大对象

## Corrected Claim

LFU 最大增益 = (LFU 字节命中率 - LRU 字节命中率) * 100%；LFU 通过频率排序缓存对象，不受时间局部性影响，在 Pareto 热度分布下，LFU 缓存对象与 LRU 不同，增益源于避免缓存低频大对象

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了父节点中'LFU字节命中率'和'LRU字节命中率'两个变量的定义，但完全缺失了父节点核心概念'最大增益'的计算公式（即两者差值乘以100%），也未包含关于'Pareto热度分布'、'时间局部性影响'或'低频大对象'等定性机制的解释。因此，子节点未能完整分解父节点的所有关键方面。）
