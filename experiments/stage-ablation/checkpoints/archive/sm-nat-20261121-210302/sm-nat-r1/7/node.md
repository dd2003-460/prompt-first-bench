# N21: LFU 相比 LRU 的提升上限受限于‘频率-大小’错配：当 β=0.9 且 ρ=-0.3 时，LFU 保留的热点对象平均大小 S_LFU_hot 显著小于 L

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 相比 LRU 的提升上限受限于‘频率-大小’错配：当 β=0.9 且 ρ=-0.3 时，LFU 保留的热点对象平均大小 S_LFU_hot 显著小于 LRU 驱逐的平均大小 S_LRU_evict，提升百分点 Δ% ≈ (S_LRU_evict - S_LFU_hot)/S_LRU_evict * MissRate_LRU。

## Corrected Claim

LFU 相比 LRU 的提升上限受限于‘频率-大小’错配：当 β=0.9 且 ρ=-0.3 时，LFU 保留的热点对象平均大小 S_LFU_hot 显著小于 LRU 驱逐的平均大小 S_LRU_evict，提升百分点 Δ% ≈ (S_LRU_evict - S_LFU_hot)/S_LRU_evict * MissRate_LRU。

## Evidence

检索失败: no sources from any channel (all 5 failed)
