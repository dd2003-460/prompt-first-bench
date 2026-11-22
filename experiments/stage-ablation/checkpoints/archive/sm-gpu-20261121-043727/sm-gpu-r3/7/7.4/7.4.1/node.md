# N245: TCO 中电力成本占比的精确计算公式：Ratio_Power = (TDP_kW * 8760h * Rate * Load_Factor) / (Hardwa

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N92

## Claim

TCO 中电力成本占比的精确计算公式：Ratio_Power = (TDP_kW * 8760h * Rate * Load_Factor) / (Hardware_Depreciation_Annual + Maintenance_Annual + Power_Annual)，需分别代入 RTX 4090 和 H100 的参数进行验证，而非仅对比硬件成本。

## Corrected Claim

TCO 中电力成本占比的精确计算公式：Ratio_Power = (TDP_kW * 8760h * Rate * Load_Factor) / (Hardware_Depreciation_Annual + Maintenance_Annual + Power_Annual)，需分别代入 RTX 4090 和 H100 的参数进行验证，而非仅对比硬件成本。

## Evidence

先验知识/题面给定，逻辑校验通过
