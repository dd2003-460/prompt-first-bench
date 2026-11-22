# N77: 咨询到达率 λ 的泊松过程建模：λ = λ_base * (1 + α_price * (P_market - P_ask)/P_market)；当价格高于市场

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

咨询到达率 λ 的泊松过程建模：λ = λ_base * (1 + α_price * (P_market - P_ask)/P_market)；当价格高于市场时，λ 显著低于基准值 λ_base

## Corrected Claim

咨询到达率 λ 的泊松过程建模：λ = λ_base * (1 + α_price * (P_market - P_ask)/P_market)；当价格高于市场时，λ 显著低于基准值 λ_base

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合价格敏感度的线性近似模型，当 P_ask > P_market 时，(P_market - P_ask) 为负值，导致 λ < λ_base，逻辑自洽且符合经济直觉。
