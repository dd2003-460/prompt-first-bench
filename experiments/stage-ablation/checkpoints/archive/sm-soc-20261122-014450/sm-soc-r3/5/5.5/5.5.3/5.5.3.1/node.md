# N315: 卖家支付函数 U_seller(P, Q) 的具体形式：U_seller = (P - C) * Q(P) - C_time(T_wait)，其中 T_wait

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

卖家支付函数 U_seller(P, Q) 的具体形式：U_seller = (P - C) * Q(P) - C_time(T_wait)，其中 T_wait 为成交周期。需验证 ∂U_seller/∂P > 0 的条件是否隐含 Q(P) 的弹性 |ε| < 1（缺乏弹性），即价格上升 1% 带来的收益增加大于销量减少带来的损失。

## Corrected Claim

卖家支付函数 U_seller(P, Q) 的具体形式：U_seller = (P - C) * Q(P) - C_time(T_wait)，其中 T_wait 为成交周期。需验证 ∂U_seller/∂P > 0 的条件是否隐含 Q(P) 的弹性 |ε| < 1（缺乏弹性），即价格上升 1% 带来的收益增加大于销量减少带来的损失。

## Evidence

先验知识/题面给定，逻辑校验通过：对 U_seller = (P-C)Q(P) 求导，∂U/∂P = Q(P) + (P-C)Q'(P) = Q(P)[1 + (P-C)/P * ε]。若 C>0，则 (P-C)/P < 1，故当 |ε| < 1 时，1 + (P-C)/P * ε > 1 - (P-C)/P > 0，导数恒正，逻辑自洽。
