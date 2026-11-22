# N24: Pareto(α=1.1) 分布未截断的期望大小 E[S] 发散（因为 α≤1），必须引入物理上限 S_max 截断，截断后 E[S] = (1.1/(0.1)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

Pareto(α=1.1) 分布未截断的期望大小 E[S] 发散（因为 α≤1），必须引入物理上限 S_max 截断，截断后 E[S] = (1.1/(0.1)) * X_min * (1 - (X_min/S_max)^0.1)。

## Corrected Claim

Pareto(α=1.1) 分布未截断的期望大小 E[S] 发散（因为 α≤1），必须引入物理上限 S_max 截断，截断后 E[S] = (1.1/(0.1)) * X_min * (1 - (X_min/S_max)^0.1)。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布α≤1时期望发散，截断后期望公式推导正确
