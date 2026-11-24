# N575: NVMe阵列年电力总成本的完整公式重构：C_electricity_annual = [(P_static_IT + P_dynamic_avg) × PUE 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

NVMe阵列年电力总成本的完整公式重构：C_electricity_annual = [(P_static_IT + P_dynamic_avg) × PUE + P_cooling_fixed] × 8760h × Unit_Price_kWh。其中P_static_IT来自N189修正值，P_dynamic_avg来自N383计算值，P_cooling_fixed为机房固定制冷功耗（若PUE已涵盖则无需单独计），Unit_Price_kWh取0.8¥/kWh。需明确PUE是否已包含所有非IT功耗。

## Corrected Claim

NVMe阵列年电力总成本的完整公式重构：C_electricity_annual = [(P_static_IT + P_dynamic_avg) × PUE + P_cooling_fixed] × 8760h × Unit_Price_kWh。其中P_static_IT来自N189修正值，P_dynamic_avg来自N383计算值，P_cooling_fixed为机房固定制冷功耗（若PUE已涵盖则无需单独计），Unit_Price_kWh取0.8¥/kWh。需明确PUE是否已包含所有非IT功耗。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合数据中心能耗成本计算标准（IT负载+制冷/损耗）×时间×单价，量纲正确（kW×h×¥/kWh=¥），且明确指出了PUE与固定制冷功耗互斥的逻辑前提，无内部矛盾。
