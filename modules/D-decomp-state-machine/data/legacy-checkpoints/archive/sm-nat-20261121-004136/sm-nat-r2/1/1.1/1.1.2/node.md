# N28: Pareto 分布的方差 Var[S] 在截断后为有限值，公式为 Var[S]_trunc = E[S^2]_trunc - (E[S]_trunc)^2，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

Pareto 分布的方差 Var[S] 在截断后为有限值，公式为 Var[S]_trunc = E[S^2]_trunc - (E[S]_trunc)^2，其中 E[S^2]_trunc 需通过二阶矩积分计算，该方差值用于后续 Copula 模型中的标准化。

## Corrected Claim

Pareto 分布的方差 Var[S] 在截断后为有限值，公式为 Var[S]_trunc = E[S^2]_trunc - (E[S]_trunc)^2，其中 E[S^2]_trunc 需通过二阶矩积分计算，该方差值用于后续 Copula 模型中的标准化。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断后矩有限，方差定义公式正确，且用于Copula标准化符合统计建模常规流程。
