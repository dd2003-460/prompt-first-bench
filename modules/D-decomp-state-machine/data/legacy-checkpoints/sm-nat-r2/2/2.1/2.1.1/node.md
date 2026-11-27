# N46: LRU 保留集合 Cache 的确定逻辑：Cache = {i | λ_i >= λ_(N_cache)}，其中 λ_(N_cache) 为第 N_cache 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

LRU 保留集合 Cache 的确定逻辑：Cache = {i | λ_i >= λ_(N_cache)}，其中 λ_(N_cache) 为第 N_cache 大的请求频率阈值，需对 10 万对象按频率降序排序后取前 N_cache 个。

## Corrected Claim

LRU 保留集合 Cache 的确定逻辑：Cache = {i | λ_i >= λ_(N_cache)}，其中 λ_(N_cache) 为第 N_cache 大的请求频率阈值，需对 10 万对象按频率降序排序后取前 N_cache 个。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 缓存替换策略的核心逻辑即保留访问频率最高（或最近访问）的对象，按频率降序排序取前 N 个符合 LRU/LFU 混合策略或纯 LFU 在稳态下的等价逻辑，量纲与定义自洽。
