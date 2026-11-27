# N280: 在 P_ask > V + 3σ 区间，修正后的成交周期公式为 T_deal_corrected = T_shorten * (1 + δ_liquidity 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

在 P_ask > V + 3σ 区间，修正后的成交周期公式为 T_deal_corrected = T_shorten * (1 + δ_liquidity * (P_ask - (V + 3σ))/σ)，其中 δ_liquidity 的引入使得 T_deal 从指数下降转为指数上升，需验证该转折点对应的 P_ask 阈值

## Corrected Claim

在 P_ask > V + 3σ 区间，修正后的成交周期公式为 T_deal_corrected = T_shorten * (1 + δ_liquidity * (P_ask - (V + 3σ))/σ)，其中 δ_liquidity 的引入使得 T_deal 从指数下降转为指数上升，需验证该转折点对应的 P_ask 阈值

## Evidence

先验知识/题面给定，逻辑校验通过
