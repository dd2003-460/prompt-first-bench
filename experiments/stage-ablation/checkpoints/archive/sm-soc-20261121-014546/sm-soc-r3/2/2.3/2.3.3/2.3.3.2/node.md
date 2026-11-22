# N210: 二阶导数 ∂²U_seller/∂P_ask² 的解析式：在指数需求模型下，SOC 条件等价于 2p'(P) + P*p''(P) < 0，其中 p''(P) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N62

## Claim

二阶导数 ∂²U_seller/∂P_ask² 的解析式：在指数需求模型下，SOC 条件等价于 2p'(P) + P*p''(P) < 0，其中 p''(P) = γ_p² * p(P)，该不等式定义了价格区间 [P_low, P_high] 的边界。

## Corrected Claim

二阶导数 ∂²U_seller/∂P_ask² 的解析式：在指数需求模型下，SOC 条件等价于 2p'(P) + P*p''(P) < 0，其中 p''(P) = γ_p² * p(P)，该不等式定义了价格区间 [P_low, P_high] 的边界。

## Evidence

先验知识/题面给定，逻辑校验通过：在指数需求模型 p(P)=Ae^{-γP} 下，p'(P)=-γp(P), p''(P)=γ²p(P)，代入 SOC 条件 2p'+Pp'' 得 p(P)(-2γ+Pγ²)<0，即 P<2/γ，逻辑自洽且符合微积分推导。
