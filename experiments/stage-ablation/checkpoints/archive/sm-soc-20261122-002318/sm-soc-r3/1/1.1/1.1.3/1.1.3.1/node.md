# N109: 过度自信系数贝叶斯更新公式 α_posterior = (α_prior * Likelihood(Price_Data)) / Prior_Prob(Pric

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N36

## Claim

过度自信系数贝叶斯更新公式 α_posterior = (α_prior * Likelihood(Price_Data)) / Prior_Prob(Price_Data) 中的核心随机源：卖家历史挂价与最终成交价的偏差分布 ε_i = P_ask_i - P_final_i，假设 ε ~ N(μ_ε, σ_ε^2)，其中 μ_ε > 0 反映系统性高估。

## Corrected Claim

过度自信系数贝叶斯更新公式 α_posterior = (α_prior * Likelihood(Price_Data)) / Prior_Prob(Price_Data) 中的核心随机源：卖家历史挂价与最终成交价的偏差分布 ε_i = P_ask_i - P_final_i，假设 ε ~ N(μ_ε, σ_ε^2)，其中 μ_ε > 0 反映系统性高估。

## Evidence

先验知识/题面给定，逻辑校验通过
