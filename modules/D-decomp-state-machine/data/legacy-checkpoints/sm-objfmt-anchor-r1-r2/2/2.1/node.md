# N12: TCO 基础模型：TCO_5yr = Purchase_Cost + (Power_Draw_Wattage * Utilization_Factor * El

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

TCO 基础模型：TCO_5yr = Purchase_Cost + (Power_Draw_Wattage * Utilization_Factor * Electricity_Rate_per_kWh * 8760_hrs * 5_yrs) + Cooling_Overhead + Maintenance_Cost。

## Corrected Claim

TCO 基础模型：TCO_5yr = Purchase_Cost + (Power_Draw_Wattage * Utilization_Factor * Electricity_Rate_per_kWh * 8760_hrs * 5_yrs) + Cooling_Overhead + Maintenance_Cost。

## Evidence

父节点级核验未通过：不完备（父节点定义了包含购买成本、电力成本、冷却开销和维护成本的TCO公式，但子节点仅涵盖了维护成本中的残值回收部分，完全缺失了电力成本、冷却开销和购买成本本身的关键分解或定义，导致覆盖严重不全。）
