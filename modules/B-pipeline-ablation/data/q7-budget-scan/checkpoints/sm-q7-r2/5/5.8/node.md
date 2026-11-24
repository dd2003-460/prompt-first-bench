# N43: 500TB 规模下 NVMe SSD 阵列的电力成本年化值为 500TB × P_Nvme_power_per_TB_watt × 8760小时 × P_Ele

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

500TB 规模下 NVMe SSD 阵列的电力成本年化值为 500TB × P_Nvme_power_per_TB_watt × 8760小时 × P_Electricity_per_kWh，假设 SSD 功耗 0.5W/TB，电费 0.6¥/kWh，则 500 × 0.5 × 8760 / 1000 × 0.6 = ¥1314/年

## Corrected Claim

500TB 规模下 NVMe SSD 阵列的电力成本年化值为 500TB × P_Nvme_power_per_TB_watt × 8760小时 × P_Electricity_per_kWh，假设 SSD 功耗 0.5W/TB，电费 0.6¥/kWh，则 500 × 0.5 × 8760 / 1000 × 0.6 = ¥1314/年

## Evidence

先验知识/题面给定，逻辑校验通过：500 * 0.5 * 8760 / 1000 * 0.6 = 1314，计算无误且量级合理
