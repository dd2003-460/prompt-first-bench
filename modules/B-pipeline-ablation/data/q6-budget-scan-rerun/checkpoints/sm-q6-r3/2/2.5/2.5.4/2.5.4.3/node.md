# N247: 低密度/低功耗工作点：N_servers=1台, Server_Power=300W/台, PUE=1.5 (老旧或小型机房), Electricity_Pri

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

低密度/低功耗工作点：N_servers=1台, Server_Power=300W/台, PUE=1.5 (老旧或小型机房), Electricity_Price=¥0.6/kWh → Power_Cost_Monthly = 1 * 300 * 24 * 30 * 1.5 * 0.6 / 1000 = ¥20.16/月

## Corrected Claim

低密度/低功耗工作点：N_servers=1台, Server_Power=300W/台, PUE=1.5 (老旧或小型机房), Electricity_Price=¥0.6/kWh → Power_Cost_Monthly = 1 * 300 * 24 * 30 * 1.5 * 0.6 / 1000 = ¥20.16/月

## Evidence

先验知识/题面给定，逻辑校验通过：计算公式 1 * 300W * 24h * 30d * 1.5 PUE * 0.6¥/kWh / 1000 = 20.16¥，数值量级与逻辑均正确。
