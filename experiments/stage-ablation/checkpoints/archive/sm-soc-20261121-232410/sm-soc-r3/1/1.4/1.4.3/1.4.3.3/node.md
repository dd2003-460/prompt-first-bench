# N124: 下游投影2：市场波动率耦合项 C_volatility，定义为 β_risk * σ_market_volatility 的乘积，当 σ_market_vola

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N42

## Claim

下游投影2：市场波动率耦合项 C_volatility，定义为 β_risk * σ_market_volatility 的乘积，当 σ_market_volatility=0.15 且 β_risk=3.0 时，C_volatility = 0.45，构成基础定价偏离的50%（假设总偏离为0.9）。

## Corrected Claim

下游投影2：市场波动率耦合项 C_volatility，定义为 β_risk * σ_market_volatility 的乘积，当 σ_market_volatility=0.15 且 β_risk=3.0 时，C_volatility = 0.45，构成基础定价偏离的50%（假设总偏离为0.9）。

## Evidence

先验知识/题面给定，逻辑校验通过：0.15 * 3.0 = 0.45，且 0.45 / 0.9 = 50%，数值计算与比例关系均自洽。

## Search Query

market volatility coupling with seller risk preference pricing formula
