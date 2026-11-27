# N26: LFU 相比 LRU 的提升机制在于 LFU 不受访问间隔影响而仅受频率影响，在 β=0.9 的长尾热度分布下，LFU 能更稳定地保留头部高频对象，避免 LRU

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 相比 LRU 的提升机制在于 LFU 不受访问间隔影响而仅受频率影响，在 β=0.9 的长尾热度分布下，LFU 能更稳定地保留头部高频对象，避免 LRU 因突发冷请求导致的热点驱逐（thrashing）；量化提升 ΔH ≈ H_LFU_max - H_LRU，其中 H_LFU_max 近似为前 k_freq 个最高频率对象的请求占比，k_freq 由容量决定。

## Corrected Claim

LFU 相比 LRU 的提升机制在于 LFU 不受访问间隔影响而仅受频率影响，在 β=0.9 的长尾热度分布下，LFU 能更稳定地保留头部高频对象，避免 LRU 因突发冷请求导致的热点驱逐（thrashing）；量化提升 ΔH ≈ H_LFU_max - H_LRU，其中 H_LFU_max 近似为前 k_freq 个最高频率对象的请求占比，k_freq 由容量决定。

## Evidence

检索失败: no sources from any channel (all 5 failed)
