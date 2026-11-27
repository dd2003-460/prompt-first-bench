# N117: TCO 对比中电力成本的量化影响：在 24/7 运行场景下，电力成本 = TDP_Watts * 24 * 365 * Electricity_Rate_per

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

TCO 对比中电力成本的量化影响：在 24/7 运行场景下，电力成本 = TDP_Watts * 24 * 365 * Electricity_Rate_per_kWh，需分别计算 2× RTX 3090 (2x350W)、1× A6000 Ada (300W)、1× H100 (700W) 的年度电力成本，并评估其对总 TCO 的占比（假设 Electricity_Rate=0.15/kWh），判断在高预算方案中电力成本是否显著影响性价比排序。

## Corrected Claim

TCO 对比中电力成本的量化影响：在 24/7 运行场景下，电力成本 = TDP_Watts * 24 * 365 * Electricity_Rate_per_kWh，需分别计算 2× RTX 3090 (2x350W)、1× A6000 Ada (300W)、1× H100 (700W) 的年度电力成本，并评估其对总 TCO 的占比（假设 Electricity_Rate=0.15/kWh），判断在高预算方案中电力成本是否显著影响性价比排序。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（W * h / 1000 * $/kWh = $），TDP数值符合硬件规格常识，计算逻辑自洽。
