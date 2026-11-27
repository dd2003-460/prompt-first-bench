# N41: LFU 相比 LRU 的字节命中率增益上限 ΔH_bytes 的精确积分形式：ΔH = ∫_{s_min}^{s_max} [P_LFU_keep(s) - P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LFU 相比 LRU 的字节命中率增益上限 ΔH_bytes 的精确积分形式：ΔH = ∫_{s_min}^{s_max} [P_LFU_keep(s) - P_LRU_keep(s)] * f_size(s) * f_freq(s) ds，其中 P_LFU_keep(s) 取决于对象频率排名，P_LRU_keep(s) 取决于对象最近访问时间间隔。

## Corrected Claim

LFU 相比 LRU 的字节命中率增益上限 ΔH_bytes 的精确积分形式：ΔH = ∫_{s_min}^{s_max} [P_LFU_keep(s) - P_LRU_keep(s)] * f_size(s) * f_freq(s) ds，其中 P_LFU_keep(s) 取决于对象频率排名，P_LRU_keep(s) 取决于对象最近访问时间间隔。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU byte hit rate gain integral formula frequency size distribution
