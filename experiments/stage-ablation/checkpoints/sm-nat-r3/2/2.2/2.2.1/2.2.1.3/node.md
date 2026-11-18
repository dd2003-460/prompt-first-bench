# N114: 边界条件修正：当对象 i 的访问频率 λ_i 低于缓存驱逐阈值 λ_evict 时，W_i 不再由几何分布决定，而是由缓存容量 C 和当前队列中对象的总大小决定

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

边界条件修正：当对象 i 的访问频率 λ_i 低于缓存驱逐阈值 λ_evict 时，W_i 不再由几何分布决定，而是由缓存容量 C 和当前队列中对象的总大小决定，需引入截断项 min(E[D_i]/λ_i, T_max_queue)。

## Corrected Claim

边界条件修正：当对象 i 的访问频率 λ_i 低于缓存驱逐阈值 λ_evict 时，W_i 不再由几何分布决定，而是由缓存容量 C 和当前队列中对象的总大小决定，需引入截断项 min(E[D_i]/λ_i, T_max_queue)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache eviction threshold for low frequency objects
