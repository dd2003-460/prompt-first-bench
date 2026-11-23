# N143: 本地DNS缓存剩余时间 t_cache_ttl 对混合策略路由切换延迟 Δt_switch 的影响：若 t_cache_ttl > 0，切换延迟为 0（命中缓存

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

本地DNS缓存剩余时间 t_cache_ttl 对混合策略路由切换延迟 Δt_switch 的影响：若 t_cache_ttl > 0，切换延迟为 0（命中缓存）；若 t_cache_ttl = 0，切换延迟为 t_lookup。混合策略中DNS切换频率 f_switch 与 t_cache_ttl 的关系为 f_switch = 1/TTL_dns，其中 TTL_dns 为DNS记录TTL值（典型 300-3600s）。

## Corrected Claim

本地DNS缓存剩余时间 t_cache_ttl 对混合策略路由切换延迟 Δt_switch 的影响：若 t_cache_ttl > 0，切换延迟为 0（命中缓存）；若 t_cache_ttl = 0，切换延迟为 t_lookup。混合策略中DNS切换频率 f_switch 与 t_cache_ttl 的关系为 f_switch = 1/TTL_dns，其中 TTL_dns 为DNS记录TTL值（典型 300-3600s）。

## Evidence

先验知识/题面给定，逻辑校验通过
