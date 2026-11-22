# N85: 挂价上限 P_ask_max 的混合分布权重：若 ε 分布为 N(0, σ_noise²) 与 U(0, ε_max) 的混合，混合比例 ω 应反映卖家中‘理性

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

挂价上限 P_ask_max 的混合分布权重：若 ε 分布为 N(0, σ_noise²) 与 U(0, ε_max) 的混合，混合比例 ω 应反映卖家中‘理性定价者’与‘投机定价者’的比例；若 ω > 0.5，则 P_ask_max 的期望值将显著高于正态假设下的 P_reserve*(1+0.5*σ_noise)，需通过分布拟合（如 KS 检验）确定 ω。

## Corrected Claim

挂价上限 P_ask_max 的混合分布权重：若 ε 分布为 N(0, σ_noise²) 与 U(0, ε_max) 的混合，混合比例 ω 应反映卖家中‘理性定价者’与‘投机定价者’的比例；若 ω > 0.5，则 P_ask_max 的期望值将显著高于正态假设下的 P_reserve*(1+0.5*σ_noise)，需通过分布拟合（如 KS 检验）确定 ω。

## Evidence

先验知识/题面给定，逻辑校验通过：混合分布的期望值计算符合线性性质，正态分布均值为0，均匀分布均值为ε_max/2，混合权重ω>0.5时引入的正向偏移确实会显著高于纯正态假设下的期望值，且KS检验是确定分布参数的标准统计方法，逻辑自洽。

## Search Query

mixed distribution fitting used goods asking prices rational vs speculative sellers
