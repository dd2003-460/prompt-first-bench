# N215: 混合架构年电力成本 C_power_hybrid = (P_ssd_watts * V_ssd_TB + P_hdd_watts * V_hdd_TB) * P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

混合架构年电力成本 C_power_hybrid = (P_ssd_watts * V_ssd_TB + P_hdd_watts * V_hdd_TB) * PUE * Price_electricity * Hours; 代入 P_ssd=0.7W/TB, P_hdd=0.4W/TB, PUE=1.4, Price=0.8, Hours=8760, 计算得出具体金额

## Corrected Claim

混合架构年电力成本 C_power_hybrid = (P_ssd_watts * V_ssd_TB + P_hdd_watts * V_hdd_TB) * PUE * Price_electricity * Hours; 代入 P_ssd=0.7W/TB, P_hdd=0.4W/TB, PUE=1.4, Price=0.8, Hours=8760, 计算得出具体金额

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid SSD HDD power consumption calculation per TB
