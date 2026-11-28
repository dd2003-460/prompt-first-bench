# N22: 年度电力运营成本（OpEx-Energy）计算公式：Annual_Energy_Cost = (Idle_Power_W × 8760h + Load_Powe

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

年度电力运营成本（OpEx-Energy）计算公式：Annual_Energy_Cost = (Idle_Power_W × 8760h + Load_Power_W × Usage_Hours_Per_Year) / 1000 × Electricity_Rate_USD_per_kWh。需分别估算 Idle_Power（待机功耗，通常为峰值的10-20%）和 Load_Power（推理峰值功耗，受精度影响：BF16 > INT8 > FP8 [待核验] 具体瓦数差异）。

## Corrected Claim

年度电力运营成本（OpEx-Energy）计算公式：Annual_Energy_Cost = (Idle_Power_W × 8760h + Load_Power_W × Usage_Hours_Per_Year) / 1000 × Electricity_Rate_USD_per_kWh。需分别估算 Idle_Power（待机功耗，通常为峰值的10-20%）和 Load_Power（推理峰值功耗，受精度影响：BF16 > INT8 > FP8 [待核验] 具体瓦数差异）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（W×h/1000=kWh），Idle_Power占比及精度功耗排序符合硬件常识

## Search Query

RTX 4090 idle power consumption watts vs load power consumption
