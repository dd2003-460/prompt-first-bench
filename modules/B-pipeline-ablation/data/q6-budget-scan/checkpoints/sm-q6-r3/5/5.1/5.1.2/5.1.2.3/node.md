# N231: 地域分布对有效N_unique_hot的影响：若用户地理分布分散（如全球），不同区域热点对象重叠度低，有效N_unique_hot_global ≈ Σ N_u

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

地域分布对有效N_unique_hot的影响：若用户地理分布分散（如全球），不同区域热点对象重叠度低，有效N_unique_hot_global ≈ Σ N_unique_hot_region_i * (1 - overlap_factor)，其中overlap_factor通常0.2-0.5。对于10个POP点，若重叠度0.3，总缓存需求需按区域独立计算后求和，而非全局去重，导致容量需求增加约1.5-2倍。

## Corrected Claim

地域分布对有效N_unique_hot的影响：若用户地理分布分散（如全球），不同区域热点对象重叠度低，有效N_unique_hot_global ≈ Σ N_unique_hot_region_i * (1 - overlap_factor)，其中overlap_factor通常0.2-0.5。对于10个POP点，若重叠度0.3，总缓存需求需按区域独立计算后求和，而非全局去重，导致容量需求增加约1.5-2倍。

## Evidence

先验知识/题面给定，逻辑校验通过
