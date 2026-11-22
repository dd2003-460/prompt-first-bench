# N17: LFU相对LRU的理论最大提升上限：在无限时间窗口且无更新的静态工作负载下，LFU字节命中率 H_lfu = 1 - (Σ_{i: L_i > C} λ_i L

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LFU相对LRU的理论最大提升上限：在无限时间窗口且无更新的静态工作负载下，LFU字节命中率 H_lfu = 1 - (Σ_{i: L_i > C} λ_i L_i) / R_total，其提升幅度 Δ_max = H_lfu - H_lru 取决于LRU未能缓存的尾部大对象的总字节流量占比。

## Corrected Claim

LFU相对LRU的理论最大提升上限：在无限时间窗口且无更新的静态工作负载下，LFU字节命中率 H_lfu = 1 - (Σ_{i: L_i > C} λ_i L_i) / R_total，其提升幅度 Δ_max = H_lfu - H_lru 取决于LRU未能缓存的尾部大对象的总字节流量占比。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU cache hit rate theoretical bound static workload
