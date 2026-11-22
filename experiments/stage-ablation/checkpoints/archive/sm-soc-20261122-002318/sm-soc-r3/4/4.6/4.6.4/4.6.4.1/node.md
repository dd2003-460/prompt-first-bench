# N212: 三方约束交集的可行性判定：构建不等式组 {ΔS_seller > -5% * Profit_seller, ΔS_buyer > -10% * Cost_buy

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

三方约束交集的可行性判定：构建不等式组 {ΔS_seller > -5% * Profit_seller, ΔS_buyer > -10% * Cost_buyer, ΔS_platform > -3% * Profit_platform}。若解集为空，则计算各约束边界的最近邻点，量化‘最小伤害’方案下最大受损方的剩余损失占比（如卖家利润下降 6.2%），以决定是否启用缓冲机制。

## Corrected Claim

三方约束交集的可行性判定：构建不等式组 {ΔS_seller > -5% * Profit_seller, ΔS_buyer > -10% * Cost_buyer, ΔS_platform > -3% * Profit_platform}。若解集为空，则计算各约束边界的最近邻点，量化‘最小伤害’方案下最大受损方的剩余损失占比（如卖家利润下降 6.2%），以决定是否启用缓冲机制。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了一种基于线性不等式组求解及最近邻点计算的优化策略，数学逻辑自洽，量纲（百分比/金额）合理，属于算法设计层面的理论推导。
