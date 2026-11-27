# N70: LRU 策略下因突发冷请求导致热点驱逐（Thrashing）的量化损失项 ΔH_thrash：在 β=0.9 的 Pareto 热度分布下，若瞬时冷请求比例突增

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

LRU 策略下因突发冷请求导致热点驱逐（Thrashing）的量化损失项 ΔH_thrash：在 β=0.9 的 Pareto 热度分布下，若瞬时冷请求比例突增 p_cold，LRU 驱逐的热点对象数量 k_evict ≈ p_cold · k_LRU，导致的命中率瞬时下降 ΔH_thrash ≈ (Σ_{i∈evicted} r_i · s_i) / Total_Byte_Traffic，该值在稳态下平均为 0 但方差贡献显著，需通过模拟或方差分析估算。

## Corrected Claim

LRU 策略下因突发冷请求导致热点驱逐（Thrashing）的量化损失项 ΔH_thrash：在 β=0.9 的 Pareto 热度分布下，若瞬时冷请求比例突增 p_cold，LRU 驱逐的热点对象数量 k_evict ≈ p_cold · k_LRU，导致的命中率瞬时下降 ΔH_thrash ≈ (Σ_{i∈evicted} r_i · s_i) / Total_Byte_Traffic，该值在稳态下平均为 0 但方差贡献显著，需通过模拟或方差分析估算。

## Evidence

先验知识/题面给定，逻辑校验通过
