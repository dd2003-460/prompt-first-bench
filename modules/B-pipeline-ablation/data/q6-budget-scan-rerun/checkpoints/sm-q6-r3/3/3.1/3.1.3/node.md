# N64: 地理分布对自建POP点负载不均的影响：若用户分布不均（如东部60%，西部40%），10个POP点需按流量比例分配容量。计算各POP点峰值带宽 B_peak_po

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

地理分布对自建POP点负载不均的影响：若用户分布不均（如东部60%，西部40%），10个POP点需按流量比例分配容量。计算各POP点峰值带宽 B_peak_pop_i = B_peak_total × geo_share_i，确保单点容量 C_pop_i ≥ B_peak_pop_i / U_target (50%)，避免过载导致延迟超标。

## Corrected Claim

地理分布对自建POP点负载不均的影响：若用户分布不均（如东部60%，西部40%），10个POP点需按流量比例分配容量。计算各POP点峰值带宽 B_peak_pop_i = B_peak_total × geo_share_i，确保单点容量 C_pop_i ≥ B_peak_pop_i / U_target (50%)，避免过载导致延迟超标。

## Evidence

先验知识/题面给定，逻辑校验通过：容量规划公式 C >= B/U 符合基本工程原理，地理分布影响负载的逻辑自洽。
