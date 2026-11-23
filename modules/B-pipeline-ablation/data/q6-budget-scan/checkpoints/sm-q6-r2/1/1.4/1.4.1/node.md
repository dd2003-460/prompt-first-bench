# N41: DNS解析与切换延迟 t_dns = t_lookup + t_cache_ttl，其中 t_lookup 为递归查询耗时（典型 5-20ms），t_cache

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

DNS解析与切换延迟 t_dns = t_lookup + t_cache_ttl，其中 t_lookup 为递归查询耗时（典型 5-20ms），t_cache_ttl 为本地DNS缓存剩余时间（0-300s）；该值构成混合策略路由切换延迟 Δt_switch 的基础组成部分。

## Corrected Claim

DNS解析与切换延迟 t_dns = t_lookup + t_cache_ttl，其中 t_lookup 为递归查询耗时（典型 5-20ms），t_cache_ttl 为本地DNS缓存剩余时间（0-300s）；该值构成混合策略路由切换延迟 Δt_switch 的基础组成部分。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

DNS lookup latency average ms
