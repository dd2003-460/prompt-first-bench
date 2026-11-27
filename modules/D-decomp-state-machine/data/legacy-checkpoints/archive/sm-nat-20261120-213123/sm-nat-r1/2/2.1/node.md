# N11: 对象大小分布 S ~ Pareto(α=1.1)，其期望 E[S] 和方差 Var[S] 仅在 α>1 时有限，具体数值取决于最小对象大小 s_min（需设定 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

对象大小分布 S ~ Pareto(α=1.1)，其期望 E[S] 和方差 Var[S] 仅在 α>1 时有限，具体数值取决于最小对象大小 s_min（需设定 s_min 以计算归一化容量）。

## Corrected Claim

对象大小分布 S ~ Pareto(α=1.1)，其期望 E[S] 和方差 Var[S] 仅在 α>1 时有限，具体数值取决于最小对象大小 s_min（需设定 s_min 以计算归一化容量）。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的矩存在性条件（E[S]有限需α>1，Var[S]有限需α>2）及参数依赖性符合数学定义。

## Search Query

Pareto distribution mean variance alpha 1.1
