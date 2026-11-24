# N236: 单 POP 月度运维成本 Ops_Per_POP = (SRE_Staff_Cost_Monthly / Total_Pops) + (Tool_Cost_Mo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

单 POP 月度运维成本 Ops_Per_POP = (SRE_Staff_Cost_Monthly / Total_Pops) + (Tool_Cost_Monthly / Total_Pops) + (Monitoring_Maintenance_Cost / Total_Pops)，其中 SRE_Staff_Cost_Monthly 为总 SRE 人力成本（2人 × ¥25k/月 = ¥50k），Tool_Cost_Monthly 为监控工具链成本（¥3k/月），Monitoring_Maintenance_Cost 为日常维护与故障处理成本（估算 ¥5k-10k/月），需按 5 个核心 POP 分摊。

## Corrected Claim

单 POP 月度运维成本 Ops_Per_POP = (SRE_Staff_Cost_Monthly / Total_Pops) + (Tool_Cost_Monthly / Total_Pops) + (Monitoring_Maintenance_Cost / Total_Pops)，其中 SRE_Staff_Cost_Monthly 为总 SRE 人力成本（2人 × ¥25k/月 = ¥50k），Tool_Cost_Monthly 为监控工具链成本（¥3k/月），Monitoring_Maintenance_Cost 为日常维护与故障处理成本（估算 ¥5k-10k/月），需按 5 个核心 POP 分摊。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node operations and maintenance cost SRE staff monitoring tool monthly cost
