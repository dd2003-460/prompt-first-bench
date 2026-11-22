# N37: 128GB缓存实际可容纳的对象数量上限 N_cap 由总内存 M 和缓存内对象的平均大小 E[S|in_cache] 决定：N_cap = M / E[S|in

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

128GB缓存实际可容纳的对象数量上限 N_cap 由总内存 M 和缓存内对象的平均大小 E[S|in_cache] 决定：N_cap = M / E[S|in_cache]；由于LRU优先保留热门对象，且热门对象较小（ρ=-0.3），E[S|in_cache] 显著小于全局平均 E[S]，需通过积分 ∫(s * f_size(s) * f_pop(s))ds / ∫(f_size(s) * f_pop(s))ds 在缓存命中范围内计算。

## Corrected Claim

128GB缓存实际可容纳的对象数量上限 N_cap 由总内存 M 和缓存内对象的平均大小 E[S|in_cache] 决定：N_cap = M / E[S|in_cache]；由于LRU优先保留热门对象，且热门对象较小（ρ=-0.3），E[S|in_cache] 显著小于全局平均 E[S]，需通过积分 ∫(s * f_size(s) * f_pop(s))ds / ∫(f_size(s) * f_pop(s))ds 在缓存命中范围内计算。

## Evidence

父节点级核验失败（LLM 错误）：Expecting ',' delimiter: line 9 column 111 (char 882)
