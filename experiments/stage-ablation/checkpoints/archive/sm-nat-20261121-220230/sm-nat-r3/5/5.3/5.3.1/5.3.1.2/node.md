# N235: 对于截断 Pareto 分布 (α=1.1, s_min=1KB, s_max=100MB)，log(s) 的方差 Var[log(s)] 的精确数值需通过积分

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81, N82, N83

## Claim

对于截断 Pareto 分布 (α=1.1, s_min=1KB, s_max=100MB)，log(s) 的方差 Var[log(s)] 的精确数值需通过积分计算，其与 E[log(s)]^2 的比值决定了 Pearson 与 Spearman 相关的偏离程度

## Corrected Claim

对于截断 Pareto 分布 (α=1.1, s_min=1KB, s_max=100MB)，log(s) 的方差 Var[log(s)] 需通过积分计算，其统计特性会影响 Pearson 与 Spearman 相关的差异，但具体偏离程度取决于计算出的方差与均值平方的比值。

## Evidence

[质询]该陈述包含具体的经验性数值结论（隐含了特定的方差与均值平方比值关系），且声称该比值“决定”了偏离程度，但未提供具体的计算结果或阈值，属于缺乏来源支持的具体经验事实断言。 | 逻辑上，Pareto分布的对数方差确实影响相关系数差异，但具体数值需积分计算，且无外部来源支持该特定参数下的精确结论，符合经验事实排除条款。

## Search Query

truncated Pareto distribution log variance integral alpha 1.1
