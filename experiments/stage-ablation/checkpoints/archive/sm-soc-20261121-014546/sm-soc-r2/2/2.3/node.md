# N13: 均衡稳定性条件：当前均衡 (P_ask*, T*) 满足 ∂U_seller/∂P_ask = 0 且 ∂U_buyer/∂T = 0，但 ∂²U_seller

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N2

## Claim

均衡稳定性条件：当前均衡 (P_ask*, T*) 满足 ∂U_seller/∂P_ask = 0 且 ∂U_buyer/∂T = 0，但 ∂²U_seller/∂P_ask² < 0 仅在 P_ask ∈ [1.15V, 1.25V] 区间成立，超出此区间均衡不稳定，卖家有动机偏离。

## Corrected Claim

均衡稳定性条件：当前均衡 (P_ask*, T*) 满足 ∂U_seller/∂P_ask = 0 且 ∂U_buyer/∂T = 0，但 ∂²U_seller/∂P_ask² < 0 仅在 P_ask ∈ [1.15V, 1.25V] 区间成立，超出此区间均衡不稳定，卖家有动机偏离。

## Evidence

先验知识/题面给定，逻辑校验通过：一阶条件（偏导为0）与二阶条件（二阶导小于0）共同构成局部极大值（稳定均衡）的标准数学定义，区间限制符合局部稳定性逻辑。

## Search Query

Nash equilibrium stability condition second-hand pricing interval
