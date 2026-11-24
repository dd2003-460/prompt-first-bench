# N262: 公有云弹性伸缩工作点3（高峰谷比）：R_pg=4.0，E_pub=3.0，若 B_avg=26.4 Mbps，则 B_peak=105.6 Mbps，额外带宽成

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

公有云弹性伸缩工作点3（高峰谷比）：R_pg=4.0，E_pub=3.0，若 B_avg=26.4 Mbps，则 B_peak=105.6 Mbps，额外带宽成本增量约为平均带宽成本的300%，且可能触发公有云带宽上限告警

## Corrected Claim

公有云弹性伸缩工作点3（高峰谷比）：R_pg=4.0，E_pub=3.0，若 B_avg=26.4 Mbps，则 B_peak=105.6 Mbps，额外带宽成本增量约为平均带宽成本的300%，且可能触发公有云带宽上限告警

## Evidence

先验知识/题面给定，逻辑校验通过：B_peak = B_avg * R_pg = 26.4 * 4.0 = 105.6 Mbps，计算正确；额外带宽成本增量 = (B_peak - B_avg) / B_avg = 300%，逻辑自洽。
