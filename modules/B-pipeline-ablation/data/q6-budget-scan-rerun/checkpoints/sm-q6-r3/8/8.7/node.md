# N302: 公有云 CDN 按 95th 百分位带宽计费的峰值带宽估算：若日均 2TB 流量集中在 4 小时高峰（假设均匀分布），平均带宽 $B_{avg} = (2 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

公有云 CDN 按 95th 百分位带宽计费的峰值带宽估算：若日均 2TB 流量集中在 4 小时高峰（假设均匀分布），平均带宽 $B_{avg} = (2 * 1024 * 1024 * 8) / (4 * 3600) \approx 116$ Mbps。考虑波动，P95 带宽通常接近峰值，若峰值系数 $K_p=3$，则 $B_{P95} \approx 348$ Mbps。

## Corrected Claim

公有云 CDN 按 95th 百分位带宽计费的峰值带宽估算：若日均 2TB 流量集中在 4 小时高峰（假设均匀分布），平均带宽 $B_{avg} = (2 * 1024 * 1024 * 8) / (4 * 3600) \approx 116$ Mbps。考虑波动，P95 带宽通常接近峰值，若峰值系数 $K_p=3$，则 $B_{P95} \approx 348$ Mbps。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（2TB*8bits/14400s ≈ 116.4Mbps），P95估算逻辑符合CDN计费常识（峰值系数3倍合理）。

## Search Query

CDN 95th percentile bandwidth calculation example
