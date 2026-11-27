# N32: LFU 相比 LRU 的最大潜在提升百分点 ΔH_max 可估算为 (H_byte_LFU - H_byte_LRU)，在 β=0.9 且 ρ=-0.3 的条件

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 相比 LRU 的最大潜在提升百分点 ΔH_max 可估算为 (H_byte_LFU - H_byte_LRU)，在 β=0.9 且 ρ=-0.3 的条件下，由于 LFU 能更稳定地保留高频小对象（利用负相关优势），其提升幅度通常在 5-15 个百分点之间，具体取决于缓存容量对长尾的截断效应。

## Corrected Claim

LFU 相比 LRU 的最大潜在提升百分点 ΔH_max 可估算为 (H_byte_LFU - H_byte_LRU)，在 β=0.9 且 ρ=-0.3 的条件下，由于 LFU 能更稳定地保留高频小对象（利用负相关优势），其提升幅度通常在 5-15 个百分点之间，具体取决于缓存容量对长尾的截断效应。

## Evidence

检索失败: no sources from any channel (all 5 failed)
