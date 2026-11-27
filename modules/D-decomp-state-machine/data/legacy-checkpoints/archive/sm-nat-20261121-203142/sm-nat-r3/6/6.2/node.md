# N214: Pareto(α=1.1) 分布的累积分布函数 F_S(s) = 1 - (x_min/s)^1.1，其在 s=x_min 处的值为 0，导致 u_S=0，这是

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

Pareto(α=1.1) 分布的累积分布函数 F_S(s) = 1 - (x_min/s)^1.1，其在 s=x_min 处的值为 0，导致 u_S=0，这是 Gaussian Copula 边界行为的直接原因

## Corrected Claim

Pareto(α=1.1) 分布的累积分布函数 F_S(s) = 1 - (x_min/s)^1.1，其在 s=x_min 处的值为 0，导致 u_S=0，这是 Gaussian Copula 边界行为的直接原因

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF定义正确，边界值推导符合数学逻辑，Copula边界行为解释合理
