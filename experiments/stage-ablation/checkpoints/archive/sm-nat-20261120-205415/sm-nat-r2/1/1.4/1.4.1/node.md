# N38: Pareto(α=1.1) 分布中，单对象大小 S 的期望 E[S] 仅当 α>1 时收敛，其解析式为 E[S] = (α * x_min) / (α - 1)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Pareto(α=1.1) 分布中，单对象大小 S 的期望 E[S] 仅当 α>1 时收敛，其解析式为 E[S] = (α * x_min) / (α - 1)；若 E[S]=1MB，则最小对象大小 x_min = (α - 1) * E[S] / α = 0.0909 MB。

## Corrected Claim

Pareto(α=1.1) 分布中，单对象大小 S 的期望 E[S] 仅当 α>1 时收敛，其解析式为 E[S] = (α * x_min) / (α - 1)；若 E[S]=1MB，则最小对象大小 x_min = (α - 1) * E[S] / α = 0.0909 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布期望公式 E[S] = α*x_min/(α-1) 在 α>1 时成立，代入 α=1.1 和 E[S]=1MB 计算得 x_min = 0.0909MB，数值与逻辑均正确。

## Search Query

Pareto distribution mean formula alpha x_min
