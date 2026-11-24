# N182: 回源带宽峰值 B_peak_origin (Mbps) 的计算：B_peak_origin = B_avg * K_peak * H_miss，其中 H_mis

- **status**: pending
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

父节点级核验未通过：不完备（子节点仅描述了对象大小参数，未覆盖父节点公式中的关键变量 K_peak（峰值系数）和 H_miss（缓存未命中率），导致推导逻辑不完整。）

## Search Query

CDN origin server bandwidth requirement cache miss rate
