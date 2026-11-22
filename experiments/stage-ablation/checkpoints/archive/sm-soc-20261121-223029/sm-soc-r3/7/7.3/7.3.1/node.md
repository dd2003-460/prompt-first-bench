# N341: 支付意愿分布参数估计：假设买家支付意愿 W ~ N(μ_W, σ_W^2)，P(W > P_ask) = 1 - Φ((P_ask - μ_W) / σ_W)；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N114

## Claim

支付意愿分布参数估计：假设买家支付意愿 W ~ N(μ_W, σ_W^2)，P(W > P_ask) = 1 - Φ((P_ask - μ_W) / σ_W)；需基于平台历史成交均价 P_deal 估计 μ_W ≈ P_deal * 1.1 且 σ_W ≈ P_deal * 0.2，以计算不同 δ 值下的 P(W > P_ask) 具体数值。

## Corrected Claim

支付意愿分布参数估计：假设买家支付意愿 W ~ N(μ_W, σ_W^2)，P(W > P_ask) = 1 - Φ((P_ask - μ_W) / σ_W)；需基于平台历史成交均价 P_deal 估计 μ_W ≈ P_deal * 1.1 且 σ_W ≈ P_deal * 0.2，以计算不同 δ 值下的 P(W > P_ask) 具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

willingness to pay distribution estimation CDF normal distribution price data
