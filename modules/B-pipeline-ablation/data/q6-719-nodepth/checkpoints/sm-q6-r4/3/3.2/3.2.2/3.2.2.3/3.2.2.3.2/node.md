# N731: 100Gbps满载运行下的月度电力成本 Power_Cost_100G = P_Load_100G × PUE × Energy_Rate × 720h，假设 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N251

## Claim

100Gbps满载运行下的月度电力成本 Power_Cost_100G = P_Load_100G × PUE × Energy_Rate × 720h，假设 P_Load_100G = 2000W (含交换机/服务器满载散热)，PUE=1.5, Energy_Rate=0.8¥/kWh，则 Power_Cost_100G ≈ 2000 × 1.5 × 0.8 × 720 ≈ ¥17,280/月

## Corrected Claim

100Gbps满载运行下的月度电力成本 Power_Cost_100G = P_Load_100G × PUE × Energy_Rate × 720h，假设 P_Load_100G = 2000W (含交换机/服务器满载散热)，PUE=1.5, Energy_Rate=0.8¥/kWh，则 Power_Cost_100G ≈ 2000 × 1.5 × 0.8 × 720 ≈ ¥17,280/月

## Evidence

先验知识/题面给定，逻辑校验通过：2000W * 1.5 * 0.8 * 720 = 17280，计算无误且量级合理
