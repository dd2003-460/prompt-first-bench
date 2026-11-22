# N142: 在考虑对象大小截断 x_max=10GB 的工作点下，E[S] 需通过截断 Pareto 分布的数值积分计算，公式为 E[S] = (α * x_min) / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

在考虑对象大小截断 x_max=10GB 的工作点下，E[S] 需通过截断 Pareto 分布的数值积分计算，公式为 E[S] = (α * x_min) / (α - 1) * (1 - (x_min/x_max)^(α-1)) / (1 - (x_min/x_max)^α)，具体数值需代入 α=1.1, x_min=1KB, x_max=10GB 计算。

## Corrected Claim

在考虑对象大小截断 x_max=10GB 的工作点下，E[S] 需通过截断 Pareto 分布的数值积分计算，公式为 E[S] = (α * x_min) / (α - 1) * (1 - (x_min/x_max)^(α-1)) / (1 - (x_min/x_max)^α)，具体数值需代入 α=1.1, x_min=1KB, x_max=10GB 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布的期望公式推导正确，量纲一致，参数代入逻辑自洽。
