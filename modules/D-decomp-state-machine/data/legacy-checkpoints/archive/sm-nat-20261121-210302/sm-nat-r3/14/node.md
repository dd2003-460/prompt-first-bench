# N221: 在 ρ=-0.3 的负相关约束下，LFU 相比 LRU 的字节命中率提升上限 ΔH_max 近似为 (S_avg_LRU_evict / S_avg_LFU_h

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 ρ=-0.3 的负相关约束下，LFU 相比 LRU 的字节命中率提升上限 ΔH_max 近似为 (S_avg_LRU_evict / S_avg_LFU_hot - 1) * MissRate_LRU，其中 S_avg_LRU_evict 接近全局均值 E[S]，而 S_avg_LFU_hot 显著小于 E[S]，需通过 'LFU vs LRU byte hit rate improvement correlation' 查证典型增益范围。

## Corrected Claim

在 ρ=-0.3 的负相关约束下，LFU 相比 LRU 的字节命中率提升上限 ΔH_max 近似为 (S_avg_LRU_evict / S_avg_LFU_hot - 1) * MissRate_LRU，其中 S_avg_LRU_evict 接近全局均值 E[S]，而 S_avg_LFU_hot 显著小于 E[S]，需通过 'LFU vs LRU byte hit rate improvement correlation' 查证典型增益范围。

## Evidence

检索失败: no sources from any channel (all 5 failed)
