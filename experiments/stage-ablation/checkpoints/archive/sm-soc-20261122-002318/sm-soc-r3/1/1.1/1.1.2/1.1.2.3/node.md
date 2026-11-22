# N107: Liquidity_index 的下游投影 1：对 λ_effective 的均值影响，E[λ_effective] = λ_base * (1 + β_liq

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Liquidity_index 的下游投影 1：对 λ_effective 的均值影响，E[λ_effective] = λ_base * (1 + β_liquidity * (1 - E[Liquidity_index]))，其中 E[Liquidity_index] = exp(μ_L + σ_L^2/2)，需计算低流动性场景（L < 10）下 λ_effective 的放大倍数。

## Corrected Claim

Liquidity_index 的下游投影 1：对 λ_effective 的均值影响，E[λ_effective] = λ_base * (1 + β_liquidity * (1 - E[Liquidity_index]))，其中 E[Liquidity_index] = exp(μ_L + σ_L^2/2)，需计算低流动性场景（L < 10）下 λ_effective 的放大倍数。

## Evidence

先验知识/题面给定，逻辑校验通过
