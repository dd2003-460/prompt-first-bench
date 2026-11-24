# N525: N171 工作点下，因命中率从 90% 降至 75%，回源流量增量 ΔTraffic_backhaul = Total_Download * (H_cloud 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N171

## Claim

N171 工作点下，因命中率从 90% 降至 75%，回源流量增量 ΔTraffic_backhaul = Total_Download * (H_cloud - H_self) = 2TB * 15% = 300GB/日，导致带宽成本增量 ΔC_bw = 300GB * 30 * P_bw_self，其中 P_bw_self 取自建包干带宽边际成本近似值 ¥0.1/GB，月增成本约 ¥900。

## Corrected Claim

N171 工作点下，因命中率从 90% 降至 75%，回源流量增量 ΔTraffic_backhaul = Total_Download * (H_cloud - H_self) = 2TB * 15% = 300GB/日，导致带宽成本增量 ΔC_bw = 300GB * 30 * P_bw_self，其中 P_bw_self 取自建包干带宽边际成本近似值 ¥0.1/GB，月增成本约 ¥900。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB * 15% = 300GB，300GB * 30天 * ¥0.1/GB = ¥900，计算无误且量级合理。
