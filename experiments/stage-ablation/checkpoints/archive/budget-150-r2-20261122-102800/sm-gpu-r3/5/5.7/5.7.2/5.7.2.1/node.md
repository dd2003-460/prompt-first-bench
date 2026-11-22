# N320: 电力成本计算公式：Electricity_Cost_3yr = Power_Dissipation_W × Utilization_Factor × 24h ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N127

## Claim

电力成本计算公式：Electricity_Cost_3yr = Power_Dissipation_W × Utilization_Factor × 24h × 365d × 3y × Electricity_Rate_$per_kWh。其中 Utilization_Factor 在本地工作站推理场景下通常取 0.5-0.8（非满载），N127 隐含假设为 1.0（满载），需修正为 0.6 以反映实际负载波动。

## Corrected Claim

电力成本计算公式：Electricity_Cost_3yr = Power_Dissipation_W × Utilization_Factor × 24h × 365d × 3y × Electricity_Rate_$per_kWh。其中 Utilization_Factor 在本地工作站推理场景下通常取 0.5-0.8（非满载），N127 隐含假设为 1.0（满载），需修正为 0.6 以反映实际负载波动。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（W × h × $/kWh = $），利用率系数0.5-0.8符合本地工作站非满载推理场景的工程常识，修正假设合理。
