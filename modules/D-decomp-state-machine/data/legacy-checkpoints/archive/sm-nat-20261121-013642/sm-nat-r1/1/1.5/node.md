# N10: LRU 缓存集合构成近似：在稳态下，LRU 缓存通常保留最近被访问的 K 个对象，K 由缓存容量 C 和对象大小决定。由于热度负相关，热门小对象更频繁访问，LR

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU 缓存集合构成近似：在稳态下，LRU 缓存通常保留最近被访问的 K 个对象，K 由缓存容量 C 和对象大小决定。由于热度负相关，热门小对象更频繁访问，LRU 缓存将主要包含高热度小对象，需计算 K 的期望值及 Cache 集合的字节覆盖率。

## Corrected Claim

LRU 缓存集合构成近似：在稳态下，LRU 缓存通常保留最近被访问的 K 个对象，K 由缓存容量 C 和对象大小决定。由于热度负相关，热门小对象更频繁访问，LRU 缓存将主要包含高热度小对象，需计算 K 的期望值及 Cache 集合的字节覆盖率。

## Evidence

先验知识/题面给定，逻辑校验通过
