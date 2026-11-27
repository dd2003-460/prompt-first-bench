# N114: 卖家被动指数 D_seller 中的 ΔPS_seller 定义为 ΔPS_seller = (P_new - V_true) - (P_old - V_tru

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

卖家被动指数 D_seller 中的 ΔPS_seller 定义为 ΔPS_seller = (P_new - V_true) - (P_old - V_true) = P_new - P_old，其中 V_true 为卖家真实估值，需通过卖家历史成交价或市场均价估计。

## Corrected Claim

卖家被动指数 D_seller 中的 ΔPS_seller 定义为 ΔPS_seller = (P_new - V_true) - (P_old - V_true) = P_new - P_old，其中 V_true 为卖家真实估值，需通过卖家历史成交价或市场均价估计。

## Evidence

先验知识/题面给定，逻辑校验通过：代数上 (P_new - V_true) - (P_old - V_true) 确实等于 P_new - P_old，且 V_true 作为常数在差值中抵消，定义自洽。
