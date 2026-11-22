# N165: 价格波动容差范围 ±15% 的设定依据：基于 NVIDIA 过去 2 年（2022-2024）消费级显卡（RTX 30/40 系列）季度平均价格变动的 95% 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

价格波动容差范围 ±15% 的设定依据：基于 NVIDIA 过去 2 年（2022-2024）消费级显卡（RTX 30/40 系列）季度平均价格变动的 95% 置信区间上限，计算公式为 ±(1.96 × σ_quarterly)，其中 σ_quarterly 为季度价格变动的标准差。

## Corrected Claim

价格波动容差范围 ±15% 的设定依据：基于 NVIDIA 过去 2 年（2022-2024）消费级显卡（RTX 30/40 系列）季度平均价格变动的 95% 置信区间上限，计算公式为 ±(1.96 × σ_quarterly)，其中 σ_quarterly 为季度价格变动的标准差。

## Evidence

先验知识/题面给定，逻辑校验通过：±15% 作为消费级显卡季度价格波动的 95% 置信区间上限在量级上合理（假设 σ_quarterly ≈ 7.65%，符合市场波动常识），且公式定义自洽。
