# N38: 共享随机源投影（卖家定价）：卖家实际挂价 P_ask = V_true + k·ε_seller + δ_anchoring，其中 ε_seller ~ N(0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N7

## Claim

共享随机源投影（卖家定价）：卖家实际挂价 P_ask = V_true + k·ε_seller + δ_anchoring，其中 ε_seller ~ N(0, σ²) 为共享随机源，δ_anchoring 为锚定偏差（通常为正，量级约 0.05V），导致 P_ask 的分布均值为 V_true + k·0 + δ_anchoring，标准差为 k·σ。

## Corrected Claim

共享随机源投影（卖家定价）：卖家实际挂价 P_ask = V_true + k·ε_seller + δ_anchoring，其中 ε_seller ~ N(0, σ²) 为共享随机源，δ_anchoring 为锚定偏差（通常为正，量级约 0.05V），导致 P_ask 的分布均值为 V_true + k·0 + δ_anchoring，标准差为 k·σ。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布线性变换性质，均值和标准差推导正确

## Search Query

anchoring bias second hand pricing distribution
