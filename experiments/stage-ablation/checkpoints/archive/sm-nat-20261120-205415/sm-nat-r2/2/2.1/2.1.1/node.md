# N40: LRU 缓存可容纳的对象数量 K 由缓存容量 C 和缓存内对象的平均大小 E[S|in_cache] 决定，即 K = C / E[S|in_cache]；由于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

LRU 缓存可容纳的对象数量 K 由缓存容量 C 和缓存内对象的平均大小 E[S|in_cache] 决定，即 K = C / E[S|in_cache]；由于热门对象较小（ρ=-0.3），E[S|in_cache] 小于全局平均 E[S]=1MB，导致 K > 128,072。

## Corrected Claim

LRU 缓存可容纳的对象数量 K 由缓存容量 C 和缓存内对象的平均大小 E[S|in_cache] 决定，即 K = C / E[S|in_cache]；由于热门对象较小（ρ=-0.3），E[S|in_cache] 小于全局平均 E[S]=1MB，导致 K > 128,072。

## Evidence

先验知识/题面给定，逻辑校验通过：K=C/E[S|in_cache] 定义正确；若 ρ=-0.3 表示大小与热度负相关，则缓存内对象平均大小小于全局平均，进而 K 大于基于全局平均计算的基准值，逻辑自洽。

## Search Query

LRU cache object count average size in cache
