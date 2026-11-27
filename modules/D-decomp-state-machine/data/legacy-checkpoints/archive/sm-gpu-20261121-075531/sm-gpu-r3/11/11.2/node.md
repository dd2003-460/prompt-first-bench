# N372: Power_Cost_Per_Hour = (GPU_TDP + Platform_Power) * Electricity_Rate / 1000；对于 2x

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N126

## Claim

Power_Cost_Per_Hour = (GPU_TDP + Platform_Power) * Electricity_Rate / 1000；对于 2x RTX 4090 (总功耗 ~1150W)，电力成本 ≈ 1.15 * 0.15 = $0.1725/hour；对于单卡 RTX 5090 (总功耗 ~775W)，电力成本 ≈ 0.775 * 0.15 = $0.11625/hour。

## Corrected Claim

Power_Cost_Per_Hour = (GPU_TDP + Platform_Power) * Electricity_Rate / 1000；对于 2x RTX 4090 (总功耗 ~1150W)，电力成本 ≈ 1.15 * 0.15 = $0.1725/hour；对于单卡 RTX 5090 (总功耗 ~775W)，电力成本 ≈ 0.775 * 0.15 = $0.11625/hour。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（W * $/kWh / 1000 = $/h），数值计算准确（1.15*0.15=0.1725, 0.775*0.15=0.11625），功耗假设符合硬件常识。
