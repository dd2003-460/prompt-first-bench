# N103: 联合分布的条件期望 E[S|Q=q] 在 ρ_s = -0.3 下无法通过解析式直接计算，需假设一个具体的联合分布族（如 Frank 或 Clayton  co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

联合分布的条件期望 E[S|Q=q] 在 ρ_s = -0.3 下无法通过解析式直接计算，需假设一个具体的联合分布族（如 Frank 或 Clayton  copula）并数值积分；若假设独立性作为下界，则 E[S|Q=q] = μ_S，负相关仅改变条件分布的形状而不改变边缘分布。

## Corrected Claim

联合分布的条件期望 E[S|Q=q] 在 ρ_s = -0.3 下无法通过解析式直接计算，需假设一个具体的联合分布族（如 Frank 或 Clayton  copula）并数值积分；若假设独立性作为下界，则 E[S|Q=q] = μ_S，负相关仅改变条件分布的形状而不改变边缘分布。

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的定义依赖于联合分布，仅知边缘分布和协方差（或相关系数）不足以唯一确定条件期望，必须指定联合分布族（如Copula）才能计算；独立性假设下条件期望等于边缘均值是概率论基本性质。

## Search Query

copula function joint distribution Pareto variables conditional expectation
