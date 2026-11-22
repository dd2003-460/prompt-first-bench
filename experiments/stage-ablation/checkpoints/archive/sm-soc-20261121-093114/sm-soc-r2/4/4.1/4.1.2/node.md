# N53: 挂价修正的动态响应：卖家挂价修正率 ΔP_listing 取决于卖家对信息透明度的敏感度 η_seller，量化为 ΔP_listing = η_seller 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N17

## Claim

挂价修正的动态响应：卖家挂价修正率 ΔP_listing 取决于卖家对信息透明度的敏感度 η_seller，量化为 ΔP_listing = η_seller * (P_ask_initial - P_market_median)，其中 P_market_median 为展示区间的中位数，η_seller 需根据卖家历史调整行为估计。

## Corrected Claim

挂价修正的动态响应：卖家挂价修正率 ΔP_listing 取决于卖家对信息透明度的敏感度 η_seller，量化为 ΔP_listing = η_seller * (P_ask_initial - P_market_median)，其中 P_market_median 为展示区间的中位数，η_seller 需根据卖家历史调整行为估计。

## Evidence

先验知识/题面给定，逻辑校验通过
