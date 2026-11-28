# N84: 能源成本 (Energy_Cost) 计算公式为 Power_Watts * Hours * Electricity_Price，RTX 4090 (450W)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

能源成本 (Energy_Cost) 计算公式为 Power_Watts * Hours * Electricity_Price，RTX 4090 (450W) 每小时能耗成本 (电价 $0.1/kWh) 约为 $0.045，A100 80GB (400W) 约为 $0.04。

## Corrected Claim

能源成本 (Energy_Cost) 计算公式为 Power_Watts * Hours * Electricity_Price，RTX 4090 (450W) 每小时能耗成本 (电价 $0.1/kWh) 约为 $0.045，A100 80GB (400W) 约为 $0.04。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Power(W) * Time(h) * Price($/kWh) 量纲正确；450W=0.45kW, 0.45*0.1=$0.045; 400W=0.4kW, 0.4*0.1=$0.04，计算无误。
