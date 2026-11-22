# N55: 均衡稳定性一阶条件：dE[Profit]/dP_list = Q(P_list) + (P_list - C) * dQ/dP_list = 0，在 P_lis

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

均衡稳定性一阶条件：dE[Profit]/dP_list = Q(P_list) + (P_list - C) * dQ/dP_list = 0，在 P_list = 1.2 * P_market 处成立；需量化 dQ/dP_list 的弹性系数 ε_Q = (dQ/dP_list) * (P_list/Q)，预期 ε_Q ∈ [-0.5, -0.8]，以验证 (P_list - C) 的提升能否抵消 Q 的下降。

## Corrected Claim

均衡稳定性一阶条件：dE[Profit]/dP_list = Q(P_list) + (P_list - C) * dQ/dP_list = 0，在 P_list = 1.2 * P_market 处成立；需量化 dQ/dP_list 的弹性系数 ε_Q = (dQ/dP_list) * (P_list/Q)，预期 ε_Q ∈ [-0.5, -0.8]，以验证 (P_list - C) 的提升能否抵消 Q 的下降。

## Evidence

先验知识/题面给定，逻辑校验通过：一阶条件推导符合微积分基本定理，弹性系数范围符合经济学常识

## Search Query

price elasticity of demand second hand market equilibrium stability
