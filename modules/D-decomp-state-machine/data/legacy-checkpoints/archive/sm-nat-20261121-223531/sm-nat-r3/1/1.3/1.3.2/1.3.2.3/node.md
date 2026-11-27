# N108: 条件分布 F_S(s|H=h) 的截断均值 E[S|H=h] 计算：E[S|H=h] = (α_cond - 1) * s_min / (α_cond - 2)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

条件分布 F_S(s|H=h) 的截断均值 E[S|H=h] 计算：E[S|H=h] = (α_cond - 1) * s_min / (α_cond - 2) * (1 - (s_min/s_max)^(2-α_cond))，当α_cond=1.209时，2-α_cond=0.791，该积分收敛，可计算具体数值。

## Corrected Claim

条件分布 F_S(s|H=h) 的截断均值 E[S|H=h] 计算：E[S|H=h] = (α_cond - 1) * s_min / (α_cond - 2) * (1 - (s_min/s_max)^(2-α_cond))，当α_cond=1.209时，2-α_cond=0.791，该积分收敛，可计算具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：帕累托分布截断均值的数学推导正确，且α=1.209>1保证积分收敛，量纲与数值逻辑自洽。
