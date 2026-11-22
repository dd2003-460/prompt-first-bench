# N34: σ_noise的分解公式：σ_noise^2 = 0.6 * Var(β_risk * σ_market_volatility) + 0.4 * Var(ε_i

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

σ_noise的分解公式：σ_noise^2 = 0.6 * Var(β_risk * σ_market_volatility) + 0.4 * Var(ε_info)，其中Var(β_risk * σ_market_volatility) = σ_market_volatility^2 * Var(β_risk)，需代入σ_market_volatility=0.2计算。

## Corrected Claim

σ_noise的分解公式：σ_noise^2 = 0.6 * Var(β_risk * σ_market_volatility) + 0.4 * Var(ε_info)，其中Var(β_risk * σ_market_volatility) = σ_market_volatility^2 * Var(β_risk)，需代入σ_market_volatility=0.2计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合方差分解逻辑，量纲一致（方差=无量纲系数*方差），代入数值步骤合理。

## Search Query

decomposition of pricing noise variance risk preference information asymmetry
