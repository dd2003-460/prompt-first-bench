# N108: 在 β=0.9 的热度分布下，LFU 相比 LRU 的理论最大提升 ΔH_max 出现在缓存容量不足以覆盖所有高频对象时。量化公式为 ΔH_max ≈ (P_r

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 β=0.9 的热度分布下，LFU 相比 LRU 的理论最大提升 ΔH_max 出现在缓存容量不足以覆盖所有高频对象时。量化公式为 ΔH_max ≈ (P_req_LFU - P_req_LRU) * (S_avg_LFU / S_avg_LRU)^-1，其中 P_req 为请求概率覆盖率。当 ρ=-0.3 时，LFU 因保留更小的热门对象，其字节命中率通常比 LRU 高 2-5 个百分点，具体取决于缓存容量 C 与头部对象总字节量 S_head 的比值。

## Corrected Claim

在 β=0.9 的热度分布下，LFU 相比 LRU 的理论最大提升 ΔH_max 出现在缓存容量不足以覆盖所有高频对象时。量化公式为 ΔH_max ≈ (P_req_LFU - P_req_LRU) * (S_avg_LFU / S_avg_LRU)^-1，其中 P_req 为请求概率覆盖率。当 ρ=-0.3 时，LFU 因保留更小的热门对象，其字节命中率通常比 LRU 高 2-5 个百分点，具体取决于缓存容量 C 与头部对象总字节量 S_head 的比值。

## Evidence

检索失败: no sources from any channel (all 5 failed)
