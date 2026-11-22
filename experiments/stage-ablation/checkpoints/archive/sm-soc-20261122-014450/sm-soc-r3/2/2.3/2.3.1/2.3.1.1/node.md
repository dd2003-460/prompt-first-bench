# N181: 基于N11的均衡稳定性条件，一阶导数 dE[Profit]/dP_list = 0 可重构为需求弹性阈值条件：ε_Q = -1 / (P_list - C)/P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

基于N11的均衡稳定性条件，一阶导数 dE[Profit]/dP_list = 0 可重构为需求弹性阈值条件：ε_Q = -1 / (P_list - C)/P_list。在 P_list = 1.2 * P_market 且假设成本 C ≈ 0.6 * P_market 时，计算 (P_list - C)/P_list = (1.2 - 0.6) * P_market / (1.2 * P_market) = 0.5，从而推导出维持均衡所需的精确弹性值 ε_Q* = -2.0。

## Corrected Claim

基于N11的均衡稳定性条件，一阶导数 dE[Profit]/dP_list = 0 可重构为需求弹性阈值条件：ε_Q = -1 / (P_list - C)/P_list。在 P_list = 1.2 * P_market 且假设成本 C ≈ 0.6 * P_market 时，计算 (P_list - C)/P_list = (1.2 - 0.6) * P_market / (1.2 * P_market) = 0.5，从而推导出维持均衡所需的精确弹性值 ε_Q* = -2.0。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导 (1.2-0.6)/1.2 = 0.5 及 ε = -1/0.5 = -2.0 计算正确，符合经济学一阶条件逻辑。
