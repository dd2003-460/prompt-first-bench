# N260: 公有云弹性伸缩工作点1（低峰谷比）：R_pg=2.0，E_pub=1.0，若 B_avg=26.4 Mbps，则 B_peak=52.8 Mbps，额外带宽成本

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

公有云弹性伸缩工作点1（低峰谷比）：R_pg=2.0，E_pub=1.0，若 B_avg=26.4 Mbps，则 B_peak=52.8 Mbps，额外带宽成本增量约为平均带宽成本的100%

## Corrected Claim

公有云弹性伸缩工作点1（低峰谷比）：R_pg=2.0，E_pub=1.0，若 B_avg=26.4 Mbps，则 B_peak=52.8 Mbps，额外带宽成本增量约为平均带宽成本的100%

## Evidence

先验知识/题面给定，逻辑校验通过：B_peak = B_avg * R_pg = 26.4 * 2.0 = 52.8 Mbps，额外带宽成本增量 = (B_peak - B_avg) / B_avg = 100%，计算自洽。
