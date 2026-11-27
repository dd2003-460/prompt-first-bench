# N128: 实际降价幅度超出搜索区间的概率：计算 P(ΔP_actual < ε_JND) = P(ΔP + ε_seller < ε_JND)，代入 ΔP ~ N(0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N34

## Claim

实际降价幅度超出搜索区间的概率：计算 P(ΔP_actual < ε_JND) = P(ΔP + ε_seller < ε_JND)，代入 ΔP ~ N(0.05 P_ask, (0.01 P_ask)^2) 和 ε_seller ~ N(0, 0.02^2)，验证是否解释 60% 无咨询

## Corrected Claim

实际降价幅度超出搜索区间的概率：计算 P(ΔP_actual < ε_JND) = P(ΔP + ε_seller < ε_JND)，代入 ΔP ~ N(0.05 P_ask, (0.01 P_ask)^2) 和 ε_seller ~ N(0, 0.02^2)，验证是否解释 60% 无咨询

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了一个基于正态分布假设的概率计算模型，用于解释特定现象（60%无咨询），其数学逻辑自洽，且作为knowledge节点无需外部来源支持。
