# N315: 在 H_hours=8760, E_price=$0.10/kWh 条件下，RTX 4090 (TDP 350W) 的年电力成本 C_power = 0.35 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N111

## Claim

在 H_hours=8760, E_price=$0.10/kWh 条件下，RTX 4090 (TDP 350W) 的年电力成本 C_power = 0.35 kW * 8760 h * $0.10/kWh = $306.60，3年总电力成本为 $919.80（修正N111中$488的估算误差，原估算可能基于平均负载或不同TDP）

## Corrected Claim

在 H_hours=8760, E_price=$0.10/kWh 条件下，RTX 4090 (TDP 350W) 的年电力成本 C_power = 0.35 kW * 8760 h * $0.10/kWh = $306.60，3年总电力成本为 $919.80（修正N111中$488的估算误差，原估算可能基于平均负载或不同TDP）

## Evidence

先验知识/题面给定，逻辑校验通过：0.35 kW * 8760 h * $0.10/kWh = $306.60，3年成本 $919.80，计算无误且量级合理。
