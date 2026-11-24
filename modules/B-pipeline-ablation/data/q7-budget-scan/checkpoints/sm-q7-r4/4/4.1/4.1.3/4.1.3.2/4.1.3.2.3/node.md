# N792: 历史故障校准公式：Sensitivity_Coeff_adjusted = Sensitivity_Coeff_base * (1 + λ * |Revenue

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N291

## Claim

历史故障校准公式：Sensitivity_Coeff_adjusted = Sensitivity_Coeff_base * (1 + λ * |Revenue_Loss_Historical - Revenue_Loss_Model| / Revenue_Loss_Model)，其中 λ 为置信衰减因子（取 0.5），用于修正理论值与实际观测偏差。

## Corrected Claim

历史故障校准公式：Sensitivity_Coeff_adjusted = Sensitivity_Coeff_base * (1 + λ * |Revenue_Loss_Historical - Revenue_Loss_Model| / Revenue_Loss_Model)，其中 λ 为置信衰减因子（取 0.5），用于修正理论值与实际观测偏差。

## Evidence

先验知识/题面给定，逻辑校验通过
