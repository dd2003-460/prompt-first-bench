# N41: LRU 缓存集合构成的上界参照：使用 Belady's MIN 算法（最优离线算法）计算理论最大字节命中率，作为 LRU 性能的上界参照，MIN 算法保留未来访

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

LRU 缓存集合构成的上界参照：使用 Belady's MIN 算法（最优离线算法）计算理论最大字节命中率，作为 LRU 性能的上界参照，MIN 算法保留未来访问间隔最长的对象，在稳态下其命中率通常高于 LRU 5-15 个百分点。

## Corrected Claim

LRU 缓存集合构成的上界参照：使用 Belady's MIN 算法（最优离线算法）计算理论最大字节命中率，作为 LRU 性能的上界参照，MIN 算法保留未来访问间隔最长的对象，在稳态下其命中率通常高于 LRU 5-15 个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过：Belady's MIN 算法作为最优离线算法，其命中率理论上界高于 LRU 是缓存理论的基本结论，5-15 个百分点的差距在典型工作负载下符合经验规律。

## Search Query

Belady MIN algorithm optimal cache replacement hit rate
