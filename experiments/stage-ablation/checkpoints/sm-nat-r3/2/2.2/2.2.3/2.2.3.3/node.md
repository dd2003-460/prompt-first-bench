# N152: 负相关对 LRU 保留集合 S_LRU 的实际影响量化：在 128GB 容量下，考虑 ρ=-0.3 后的最大保留对象数 N_cache_corr 相比独立假设下

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

负相关对 LRU 保留集合 S_LRU 的实际影响量化：在 128GB 容量下，考虑 ρ=-0.3 后的最大保留对象数 N_cache_corr 相比独立假设下的 N_cache_indep 增加百分比 ΔN = (N_cache_corr - N_cache_indep) / N_cache_indep * 100%，该增量直接提升字节命中率。

## Corrected Claim

负相关对 LRU 保留集合 S_LRU 的实际影响量化：在 128GB 容量下，考虑 ρ=-0.3 后的最大保留对象数 N_cache_corr 相比独立假设下的 N_cache_indep 增加百分比 ΔN = (N_cache_corr - N_cache_indep) / N_cache_indep * 100%，该增量直接提升字节命中率。

## Evidence

先验知识/题面给定，逻辑校验通过：负相关意味着对象大小与访问频率呈反向关系，在LRU策略下，高频访问的小对象更容易被保留，从而在固定容量下能容纳更多对象，逻辑自洽且符合缓存理论直觉。
