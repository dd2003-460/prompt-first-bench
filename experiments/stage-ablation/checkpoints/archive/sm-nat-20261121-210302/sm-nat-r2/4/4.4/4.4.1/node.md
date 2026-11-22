# N48: 耦合系数 c 的解析表达式：c = Cov(Size, Popularity) / (σ_S * σ_P * E[Size] * E[Popularity])，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

耦合系数 c 的解析表达式：c = Cov(Size, Popularity) / (σ_S * σ_P * E[Size] * E[Popularity])，其中 Cov(Size, Popularity) = ρ * σ_S * σ_P，需通过 Pareto 分布的矩计算 σ_S 和 σ_P

## Corrected Claim

耦合系数 c 的解析表达式：c = Cov(Size, Popularity) / (σ_S * σ_P * E[Size] * E[Popularity])，其中 Cov(Size, Popularity) = ρ * σ_S * σ_P，需通过 Pareto 分布的矩计算 σ_S 和 σ_P

## Evidence

先验知识/题面给定，逻辑校验通过：该表达式是标准化协方差（相关系数）与均值乘积的代数变形，量纲一致，数学推导自洽。
