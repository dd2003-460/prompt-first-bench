# N30: 截断 Pareto 分布的期望值解析公式：E[S] = (α * x_min^{α-1} * (B^α - x_min^α)) / ((α-1) * (B^{α

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

截断 Pareto 分布的期望值解析公式：E[S] = (α * x_min^{α-1} * (B^α - x_min^α)) / ((α-1) * (B^{α-1} - x_min^{α-1}))，代入 α=1.1 后需数值求解 B 以满足 E[S]=1MB

## Corrected Claim

截断 Pareto 分布的期望值解析公式：E[S] = (α * x_min^{α-1} * (B^α - x_min^α)) / ((α-1) * (B^{α-1} - x_min^{α-1}))，代入 α=1.1 后需数值求解 B 以满足 E[S]=1MB

## Evidence

先验知识/题面给定，逻辑校验通过
