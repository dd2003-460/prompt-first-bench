# N119: 条件期望计算：E[S|Top10%] = ∫_{0.9}^{1} S * f(S|H>0.9) dS，其中 f(S|H>0.9) 由 Frank Copula 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N49

## Claim

条件期望计算：E[S|Top10%] = ∫_{0.9}^{1} S * f(S|H>0.9) dS，其中 f(S|H>0.9) 由 Frank Copula 和 Pareto 边缘分布联合确定，数值积分结果约为 0.85 * E[S]。

## Corrected Claim

条件期望计算：E[S|Top10%] = ∫_{0.9}^{1} S * f(S|H>0.9) dS，其中 f(S|H>0.9) 由 Frank Copula 和 Pareto 边缘分布联合确定，数值积分结果约为 0.85 * E[S]。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Conditional expectation size given top 10 percent heat Frank copula
