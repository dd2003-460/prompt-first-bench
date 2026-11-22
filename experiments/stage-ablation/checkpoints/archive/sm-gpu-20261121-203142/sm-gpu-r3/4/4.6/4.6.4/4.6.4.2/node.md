# N313: 电力成本 (Electricity_Cost) 的每小时量化公式为：Cost_elec_hour = (TDP_gpu + TDP_system) * 1.1 

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

电力成本 (Electricity_Cost) 的每小时量化公式为：Cost_elec_hour = (TDP_gpu + TDP_system) * 1.1 (PSU效率) * 0.10 (USD/kWh) / 1000；对于单卡 RTX 4090 (450W GPU + 100W System = 550W)，每小时电力成本约为 $0.0605；对于 2x RTX 4090 (900W GPU + 250W System = 1150W)，每小时电力成本约为 $0.1265；对于 A100 80GB (400W GPU + 150W System = 550W)，每小时电力成本约为 $0.0605。

## Corrected Claim

电力成本 (Electricity_Cost) 的每小时量化公式为：Cost_elec_hour = (TDP_gpu + TDP_system) * 1.1 (PSU效率) * 0.10 (USD/kWh) / 1000；对于单卡 RTX 4090 (450W GPU + 100W System = 550W)，每小时电力成本约为 $0.0605；对于 2x RTX 4090 (900W GPU + 250W System = 1150W)，每小时电力成本约为 $0.1265；对于 A100 80GB (400W GPU + 150W System = 550W)，每小时电力成本约为 $0.0605。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（W * 效率 * $/kWh / 1000 = $/h），数值计算准确（550W -> $0.0605, 1150W -> $0.1265），符合物理与经济直觉。
