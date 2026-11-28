# N71: Cost_per_Month 的展开公式为 (Purchase_Cost / Useful_Life_Months) + (Power_Dissipation_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

Cost_per_Month 的展开公式为 (Purchase_Cost / Useful_Life_Months) + (Power_Dissipation_Watts * 0.5 * 730_hours * Electricity_Rate_USD_per_kWh / 1000)，其中 Useful_Life_Months 假设为 60 个月，Electricity_Rate 取 $0.12/kWh 作为基准。

## Corrected Claim

Cost_per_Month 的展开公式为 (Purchase_Cost / Useful_Life_Months) + (Power_Dissipation_Watts * 0.5 * 730_hours * Electricity_Rate_USD_per_kWh / 1000)，其中 Useful_Life_Months 假设为 60 个月，Electricity_Rate 取 $0.12/kWh 作为基准。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合总拥有成本（TCO）中折旧+能耗的标准计算逻辑，量纲单位换算（Watt*hours/1000=kWh）正确，假设参数（60个月寿命、$0.12/kWh电价）在工程估算中属于合理且常见的基准值。
