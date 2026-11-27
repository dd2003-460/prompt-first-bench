# N40: LRU 缓存可容纳的对象数量 K 由缓存容量 C 和缓存内对象的平均大小 E[S|in_cache] 决定，即 K = C / E[S|in_cache]；由于

- **status**: pending
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

父节点级核验未通过：有冗余（三个子节点本质上是同一公式 K = C / E[S|in_cache] 在不同相关系数 ρ 下的具体数值实例，属于参数扫描而非正交的逻辑分支。它们共同证明了在当前参数下 K_eff 始终等于 N，因此结构上存在冗余。）

## Search Query

LRU cache object count average size in cache
