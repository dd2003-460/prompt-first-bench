# N105: 损失厌恶系数上下文修正公式 λ_effective = λ_base * (1 + β_liquidity * (1 - Liquidity_index)) 中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N35

## Claim

损失厌恶系数上下文修正公式 λ_effective = λ_base * (1 + β_liquidity * (1 - Liquidity_index)) 中的核心随机源：市场流动性指标 Liquidity_index，定义为 L = (N_active_buyers * Avg_Daily_Views) / Total_Listings，服从对数正态分布 ln(L) ~ N(μ_L, σ_L^2)。

## Corrected Claim

损失厌恶系数上下文修正公式 λ_effective = λ_base * (1 + β_liquidity * (1 - Liquidity_index)) 中的核心随机源：市场流动性指标 Liquidity_index，定义为 L = (N_active_buyers * Avg_Daily_Views) / Total_Listings，服从对数正态分布 ln(L) ~ N(μ_L, σ_L^2)。

## Evidence

先验知识/题面给定，逻辑校验通过
