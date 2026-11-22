# N33: 对象大小分布 S ~ Pareto(α=1.1) 的方差 Var[S] 计算公式为 Var[S] = (α * s_min^2) / ((α - 1)^2 * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

对象大小分布 S ~ Pareto(α=1.1) 的方差 Var[S] 计算公式为 Var[S] = (α * s_min^2) / ((α - 1)^2 * (α - 2))，由于 α=1.1 < 2，理论方差为无穷大，实际计算需使用截断分布或模拟估计。

## Corrected Claim

对象大小分布 S ~ Pareto(α=1.1) 的方差 Var[S] 计算公式为 Var[S] = (α * s_min^2) / ((α - 1)^2 * (α - 2))，由于 α=1.1 < 2，理论方差为无穷大，实际计算需使用截断分布或模拟估计。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布方差公式正确，且α<2时方差确实发散，结论符合数学定义。
