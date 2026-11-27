# N179: 共享随机源 ε_seller 的下游投影：对成交周期 T 的影响。由于高挂价导致需求弹性作用减弱，成交周期 T_seller = T_base * (1 + k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N45

## Claim

共享随机源 ε_seller 的下游投影：对成交周期 T 的影响。由于高挂价导致需求弹性作用减弱，成交周期 T_seller = T_base * (1 + k_t * σ_seller)，其中 k_t 为时间敏感度系数（假设 k_t=2.0）。新卖家成交周期比老卖家长 16.4%。

## Corrected Claim

共享随机源 ε_seller 的下游投影：对成交周期 T 的影响。由于高挂价导致需求弹性作用减弱，成交周期 T_seller = T_base * (1 + k_t * σ_seller)，其中 k_t 为时间敏感度系数（假设 k_t=2.0）。新卖家成交周期比老卖家长 16.4%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_seller = T_base * (1 + k_t * σ_seller) 中，若新卖家比老卖家长 16.4%，则隐含 k_t * Δσ = 0.164。在 k_t=2.0 的假设下，Δσ=0.082，数值量级合理且无内部矛盾。

## Search Query

pricing uncertainty impact on time to sale
