# N204: Prob(Sell|P_ask) 的具体形式：Prob(Sell|P_ask) = Φ((V - P_ask - C_transaction + μ_deal_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

Prob(Sell|P_ask) 的具体形式：Prob(Sell|P_ask) = Φ((V - P_ask - C_transaction + μ_deal_bias) / σ_deal)，其中 μ_deal_bias 为成交阶段的认知偏差，通常 μ_deal_bias < μ_click_bias，因为成交前有更充分的比价时间。

## Corrected Claim

Prob(Sell|P_ask) 的具体形式：Prob(Sell|P_ask) = Φ((V - P_ask - C_transaction + μ_deal_bias) / σ_deal)，其中 μ_deal_bias 为成交阶段的认知偏差，通常 μ_deal_bias < μ_click_bias，因为成交前有更充分的比价时间。

## Evidence

先验知识/题面给定，逻辑校验通过
