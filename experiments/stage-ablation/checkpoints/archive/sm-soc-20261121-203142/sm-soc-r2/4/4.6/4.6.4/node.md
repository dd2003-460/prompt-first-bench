# N75: 买家价格敏感度绝对值 |∂U_buyer/∂P| 的一阶导数表达式为 Q * (1 + P_deal * ∂Q/∂P / (V - P_deal))，需代入 N

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

买家价格敏感度绝对值 |∂U_buyer/∂P| 的一阶导数表达式为 Q * (1 + P_deal * ∂Q/∂P / (V - P_deal))，需代入 N26 中的 k_v 及 N6 中的 T_search 边界条件进行数值估算。

## Corrected Claim

买家价格敏感度绝对值 |∂U_buyer/∂P| 的一阶导数表达式为 Q * (1 + P_deal * ∂Q/∂P / (V - P_deal))，需代入 N26 中的 k_v 及 N6 中的 T_search 边界条件进行数值估算。

## Evidence

先验知识/题面给定，逻辑校验通过
