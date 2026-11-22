# N114: 工作点1（独立假设 ρ=0）：假设热度与大小独立，E[S|in_cache] = E[S] = 1MB，则 K_0 = 128GB/1MB = 131,072；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

工作点1（独立假设 ρ=0）：假设热度与大小独立，E[S|in_cache] = E[S] = 1MB，则 K_0 = 128GB/1MB = 131,072；由于 N=100,000 < K_0，缓存可容纳全部对象，K_eff = 100,000，此时 LRU 命中率仅受热度分布限制。

## Corrected Claim

工作点1（独立假设 ρ=0）：假设热度与大小独立，E[S|in_cache] = E[S] = 1MB，则 K_0 = 128GB/1MB = 131,072；由于 N=100,000 < K_0，缓存可容纳全部对象，K_eff = 100,000，此时 LRU 命中率仅受热度分布限制。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/1MB=131,072计算正确，N<K_0推导K_eff=N符合缓存容量逻辑
