# N46: LFU 缓存集合构成：LFU 保留频率最高的 K_lfu 个对象，K_lfu 由 Σ_{i=1}^{K_lfu} s_i ≤ 128GB 决定，由于 LFU 不

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LFU 缓存集合构成：LFU 保留频率最高的 K_lfu 个对象，K_lfu 由 Σ_{i=1}^{K_lfu} s_i ≤ 128GB 决定，由于 LFU 不受时间局部性影响，其缓存集合更稳定，但可能忽略突发访问的大对象。

## Corrected Claim

LFU 缓存集合构成：LFU 保留频率最高的 K_lfu 个对象，K_lfu 由 Σ_{i=1}^{K_lfu} s_i ≤ 128GB 决定，由于 LFU 不受时间局部性影响，其缓存集合更稳定，但可能忽略突发访问的大对象。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU cache set composition frequency based replacement
