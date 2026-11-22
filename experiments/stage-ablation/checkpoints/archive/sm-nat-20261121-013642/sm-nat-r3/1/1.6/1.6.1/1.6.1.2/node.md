# N140: LFU 缓存集合的‘突发盲区’量化：由于 LFU 计数老化滞后（半衰期 T_half=1 day），突发访问的大对象在 T_burst < T_half 期间无

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

LFU 缓存集合的‘突发盲区’量化：由于 LFU 计数老化滞后（半衰期 T_half=1 day），突发访问的大对象在 T_burst < T_half 期间无法进入缓存，其丢失的字节流量占比 ΔB_burst = (Σ_{i∈Burst} r_i * s_i) / R_bytes_total，其中 Burst 为突发期间新增的高频对象集合。

## Corrected Claim

LFU 缓存集合的‘突发盲区’量化：由于 LFU 计数老化滞后（半衰期 T_half=1 day），突发访问的大对象在 T_burst < T_half 期间无法进入缓存，其丢失的字节流量占比 ΔB_burst = (Σ_{i∈Burst} r_i * s_i) / R_bytes_total，其中 Burst 为突发期间新增的高频对象集合。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU burst traffic loss cache latency
