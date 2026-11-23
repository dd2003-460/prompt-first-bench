# N38: 日均2TB流量的带宽峰值计算：B_peak = (2 * 1024 * 1024 MB / 86400 s) * k_peak；若 k_peak = 4，则 B

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

日均2TB流量的带宽峰值计算：B_peak = (2 * 1024 * 1024 MB / 86400 s) * k_peak；若 k_peak = 4，则 B_peak ≈ 23.7 Mbps * 4 = 94.8 Mbps ≈ 0.1 Gbps；此数值远低于公有云CDN单区域带宽上限（通常 > 10 Gbps），表明带宽峰值不是公有云CDN的约束瓶颈，而是成本优化问题。

## Corrected Claim

日均2TB流量的带宽峰值计算：B_peak = (2 * 1024 * 1024 MB / 86400 s) * k_peak；若 k_peak = 4，则 B_peak ≈ 23.7 Mbps * 4 = 94.8 Mbps ≈ 0.1 Gbps；此数值远低于公有云CDN单区域带宽上限（通常 > 10 Gbps），表明带宽峰值不是公有云CDN的约束瓶颈，而是成本优化问题。

## Evidence

先验知识/题面给定，逻辑校验通过：日均2TB流量换算为平均带宽约23.7Mbps，乘以峰值系数4得到94.8Mbps，远低于公有云CDN单区域通常>10Gbps的带宽上限，结论合理。
