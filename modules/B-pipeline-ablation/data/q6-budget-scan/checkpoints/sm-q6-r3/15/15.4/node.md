# N368: P99 约束对策略切换的限制条件：若新增自建流量导致 P99_self > T，则强制使用公有云；P99_self 的约束条件为 t_cache_self + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

P99 约束对策略切换的限制条件：若新增自建流量导致 P99_self > T，则强制使用公有云；P99_self 的约束条件为 t_cache_self + p_miss_self * t_origin_self ≤ T，其中 p_miss_self 需满足 p_miss_self ≤ (T - t_cache_self) / t_origin_self

## Corrected Claim

P99 约束对策略切换的限制条件：若新增自建流量导致 P99_self > T，则强制使用公有云；P99_self 的约束条件为 t_cache_self + p_miss_self * t_origin_self ≤ T，其中 p_miss_self 需满足 p_miss_self ≤ (T - t_cache_self) / t_origin_self

## Evidence

先验知识/题面给定，逻辑校验通过：P99延迟约束通常由缓存命中路径和未命中回源路径的加权平均或最坏情况决定，此处采用最坏情况或保守估计（未命中时延迟为 t_origin_self），推导出的 p_miss_self 上限符合代数逻辑，量纲一致。
