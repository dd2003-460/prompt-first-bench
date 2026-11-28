# N96: 能耗电费 E_opex 的计算公式为 E_opex = P_avg (W) × 8760 (h/year) × 5 (years) × R_elec ($/kW

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

能耗电费 E_opex 的计算公式为 E_opex = P_avg (W) × 8760 (h/year) × 5 (years) × R_elec ($/kWh) / 1000，其中 P_avg 需根据负载利用率 (Utilization Rate, U) 调整为 P_max × U，R_elec 取当地平均电价（如 $0.15/kWh）。

## Corrected Claim

能耗电费 E_opex 的计算公式为 E_opex = P_avg (W) × 8760 (h/year) × 5 (years) × R_elec ($/kWh) / 1000，其中 P_avg 需根据负载利用率 (Utilization Rate, U) 调整为 P_max × U，R_elec 取当地平均电价（如 $0.15/kWh）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式中功率(W)×时间(h)得到能量(Wh)，除以1000转换为kWh，再乘以电价($/kWh)得到成本($)，量纲一致；8760小时/年符合标准定义；P_avg = P_max × U 符合负载利用率的基本定义。
