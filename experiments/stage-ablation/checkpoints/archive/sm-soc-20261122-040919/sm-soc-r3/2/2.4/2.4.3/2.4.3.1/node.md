# N232: 共享随机源定义：平台佣金最大化目标函数中的成交量 N_deals 受市场总需求随机性 ε_D 影响，N_deals = N_base * (1 + ε_D)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N63

## Claim

共享随机源定义：平台佣金最大化目标函数中的成交量 N_deals 受市场总需求随机性 ε_D 影响，N_deals = N_base * (1 + ε_D)，其中 ε_D ~ N(0, σ²_D)，σ²_D 由宏观经济波动、季节性因素和平台流量波动共同决定，且 σ²_D = σ²_macro + σ²_seasonal + σ²_traffic。

## Corrected Claim

共享随机源定义：平台佣金最大化目标函数中的成交量 N_deals 受市场总需求随机性 ε_D 影响，N_deals = N_base * (1 + ε_D)，其中 ε_D ~ N(0, σ²_D)，σ²_D 由宏观经济波动、季节性因素和平台流量波动共同决定，且 σ²_D = σ²_macro + σ²_seasonal + σ²_traffic。

## Evidence

先验知识/题面给定，逻辑校验通过：该定义符合随机变量线性组合的方差可加性原理（独立分量方差相加），量纲与逻辑自洽。

## Search Query

stochastic demand model for online marketplace transaction volume
