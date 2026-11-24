# N182: 回源带宽峰值 B_peak_origin (Mbps) 的计算：B_peak_origin = B_avg * K_peak * H_miss，其中 H_mis

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

回源带宽峰值 B_peak_origin (Mbps) 的计算：B_peak_origin = B_avg * K_peak * H_miss，其中 H_miss 为整体缓存未命中率，决定源站出口带宽规格。

## Corrected Claim

回源带宽峰值 B_peak_origin (Mbps) 的计算：B_peak_origin = B_avg * K_peak * H_miss，其中 H_miss 为整体缓存未命中率，决定源站出口带宽规格。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN origin server bandwidth requirement cache miss rate
