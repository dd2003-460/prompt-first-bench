# N111: Likelihood(Price_Data) 的具体形式：基于正态分布假设，Likelihood(ε) ∝ exp(-ε^2 / (2σ_ε^2))，需计算当观

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N36

## Claim

Likelihood(Price_Data) 的具体形式：基于正态分布假设，Likelihood(ε) ∝ exp(-ε^2 / (2σ_ε^2))，需计算当观测到新偏差 ε_new 时，后验 α_posterior 相对于先验 α_prior 的更新倍数，量化新数据对过度自信系数的修正强度。

## Corrected Claim

Likelihood(Price_Data) 的具体形式：基于正态分布假设，Likelihood(ε) ∝ exp(-ε^2 / (2σ_ε^2))，需计算当观测到新偏差 ε_new 时，后验 α_posterior 相对于先验 α_prior 的更新倍数，量化新数据对过度自信系数的修正强度。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布似然函数形式正确，贝叶斯更新逻辑自洽
