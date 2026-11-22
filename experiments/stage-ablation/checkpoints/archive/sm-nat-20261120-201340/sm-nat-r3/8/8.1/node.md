# N69: LFU 策略下缓存对象集合的判定条件：对象 j 在缓存中当且仅当其全局访问频率 rank_freq(j) ≤ k_LFU，其中 rank_freq 基于长期统计

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

LFU 策略下缓存对象集合的判定条件：对象 j 在缓存中当且仅当其全局访问频率 rank_freq(j) ≤ k_LFU，其中 rank_freq 基于长期统计频率而非最近访问时间，这导致 LFU 对突发冷请求免疫，但存在“频率滞后”问题（新热点需时间积累频率才能进入缓存）。

## Corrected Claim

LFU 策略下缓存对象集合的判定条件：对象 j 在缓存中当且仅当其全局访问频率 rank_freq(j) ≤ k_LFU，其中 rank_freq 基于长期统计频率而非最近访问时间，这导致 LFU 对突发冷请求免疫，但存在“频率滞后”问题（新热点需时间积累频率才能进入缓存）。

## Evidence

先验知识/题面给定，逻辑校验通过
