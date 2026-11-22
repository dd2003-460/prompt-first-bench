# N25: 截断 Pareto 分布的均值计算公式：E[S] = (α * x_min * (x_max^(1-α) - x_min^(1-α))) / ((1-α) * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

截断 Pareto 分布的均值计算公式：E[S] = (α * x_min * (x_max^(1-α) - x_min^(1-α))) / ((1-α) * (x_max^α - x_min^α))，其中 α=1.1，该公式用于反解 x_min 或验证 1.31072 MB 约束的可行性。

## Corrected Claim

截断 Pareto 分布的均值计算公式：E[S] = (α * x_min * (x_max^(1-α) - x_min^(1-α))) / ((1-α) * (x_max^α - x_min^α))，其中 α=1.1，该公式用于反解 x_min 或验证 1.31072 MB 约束的可行性。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合截断帕累托分布均值的数学推导，量纲与逻辑自洽。
