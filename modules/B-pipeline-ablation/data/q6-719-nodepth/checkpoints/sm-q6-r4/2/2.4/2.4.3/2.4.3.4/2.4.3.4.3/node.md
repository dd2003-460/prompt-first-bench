# N685: 工作点3（高冗余/高人工）：SRE_Staff_Cost_Monthly = 2人 × ¥25k + 外包应急¥10k = ¥60k；Tool_Cost = ¥

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N236, N237, N238

## Claim

工作点3（高冗余/高人工）：SRE_Staff_Cost_Monthly = 2人 × ¥25k + 外包应急¥10k = ¥60k；Tool_Cost = ¥5k（商业版监控）；Monitoring_Maint = ¥10k（高故障率假设）；Total_Pops=5；Ops_Per_POP = (60000+5000+10000)/5 = ¥15.0k/月/POP

## Corrected Claim

工作点3（高冗余/高人工）：SRE_Staff_Cost_Monthly = 2人 × ¥25k + 外包应急¥10k = ¥60k；Tool_Cost = ¥5k（商业版监控）；Monitoring_Maint = ¥10k（高故障率假设）；Total_Pops=5；Ops_Per_POP = (60000+5000+10000)/5 = ¥15.0k/月/POP

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (60000+5000+10000)/5 = 15000 正确，量纲与数值量级符合SRE成本估算常识。
