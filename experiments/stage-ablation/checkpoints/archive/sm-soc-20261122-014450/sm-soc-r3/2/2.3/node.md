# N11: 均衡稳定性条件：当卖家预期收益 E[Profit] = (P_list - C) * Q(P_list) 在 P_list = P_market * 1.2 处

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

均衡稳定性条件：当卖家预期收益 E[Profit] = (P_list - C) * Q(P_list) 在 P_list = P_market * 1.2 处达到局部极大值时，均衡稳定。此处 Q(P_list) 虽低于 Q(P_market)，但 (P_list - C) 的提升幅度抵消了数量下降，且因筛选效应，Q 的下降斜率较缓。

## Corrected Claim

均衡稳定性条件：当卖家预期收益 E[Profit] = (P_list - C) * Q(P_list) 在 P_list = P_market * 1.2 处达到局部极大值时，均衡稳定。此处 Q(P_list) 虽低于 Q(P_market)，但 (P_list - C) 的提升幅度抵消了数量下降，且因筛选效应，Q 的下降斜率较缓。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应一阶条件（FOC）、模型结构/参数修正（筛选效应）和二阶条件（SOC），三者逻辑独立且互不重叠，共同构成了局部极大值均衡的完整数学证明框架，无冗余。）

## Search Query

equilibrium stability condition profit maximization high anchor price
