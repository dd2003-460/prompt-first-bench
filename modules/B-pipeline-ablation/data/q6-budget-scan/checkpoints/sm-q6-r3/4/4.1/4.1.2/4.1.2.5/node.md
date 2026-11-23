# N251: 自建节点P99延迟风险项中的缓存未命中回源延迟 T_cache_miss_prob_self * (T_backhaul_self + T_origin)：自建

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77, N78, N79

## Claim

自建节点P99延迟风险项中的缓存未命中回源延迟 T_cache_miss_prob_self * (T_backhaul_self + T_origin)：自建节点缓存命中率H_cache_self通常为70-80%（初期），未命中率20-30%；回源延迟T_backhaul_self为自建节点到Origin的RTT，通常为50-100ms（国内），T_origin为Origin响应时间（10-50ms）；因此未命中时的额外延迟为20-30% × (60-150ms) = 12-45ms，平均P99延迟增加12-45ms。

## Corrected Claim

自建节点P99延迟风险项中的缓存未命中回源延迟 T_cache_miss_prob_self * (T_backhaul_self + T_origin)：自建节点缓存命中率H_cache_self通常为70-80%（初期），未命中率20-30%；回源延迟T_backhaul_self为自建节点到Origin的RTT，通常为50-100ms（国内），T_origin为Origin响应时间（10-50ms）；因此未命中时的额外延迟为20-30% × (60-150ms) = 12-45ms，平均P99延迟增加12-45ms。

## Evidence

先验知识/题面给定，逻辑校验通过：国内自建节点到Origin的RTT（50-100ms）及Origin响应时间（10-50ms）符合典型网络工程经验值，缓存命中率70-80%亦在合理范围内，计算逻辑自洽。

## Search Query

self-hosted CDN cache miss penalty backhaul latency calculation
