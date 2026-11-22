# N213: Clayton Copula 参数 θ=2.03 下联合分布的条件期望 E[S|P] 的数值积分公式：E[S|P] = ∫ S * f(S|P) dS，其中 f

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

Clayton Copula 参数 θ=2.03 下联合分布的条件期望 E[S|P] 的数值积分公式：E[S|P] = ∫ S * f(S|P) dS，其中 f(S|P) 由 Clayton 密度函数与边际 Pareto 分布联合确定，需通过 Monte Carlo 或 Gauss-Legendre 积分计算

## Corrected Claim

Clayton Copula 参数 θ=2.03 下联合分布的条件期望 E[S|P] 的数值积分公式：E[S|P] = ∫ S * f(S|P) dS，其中 f(S|P) 由 Clayton 密度函数与边际 Pareto 分布联合确定，需通过 Monte Carlo 或 Gauss-Legendre 积分计算

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的定义公式正确，Clayton Copula 与 Pareto 边际分布的组合在精算与金融领域是标准建模方法，数值积分方法（Monte Carlo/Gauss-Legendre）描述准确。
