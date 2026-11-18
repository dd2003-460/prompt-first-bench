# N27: 缓存对象数量上限 K_max 由最坏情况（最小对象）决定：K_max = C_avail / S_min，其中 S_min = 1 KB (1024 bytes

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

缓存对象数量上限 K_max 由最坏情况（最小对象）决定：K_max = C_avail / S_min，其中 S_min = 1 KB (1024 bytes)，用于确定 LRU 队列的最大长度边界。

## Corrected Claim

缓存对象数量上限 K_max 由最坏情况（最小对象）决定：K_max = C_avail / S_min，其中 S_min = 1 KB (1024 bytes)，用于确定 LRU 队列的最大长度边界。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache maximum object count minimum size
