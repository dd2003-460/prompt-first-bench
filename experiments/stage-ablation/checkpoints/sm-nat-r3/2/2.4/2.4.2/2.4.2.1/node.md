# N159: Pareto(α=1.1, x_min=1KB, x_max=∞) 分布的期望值 E[S] 在数学上发散（因为 α < 1），因此 N55 中的分母 E[S] 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

Pareto(α=1.1, x_min=1KB, x_max=∞) 分布的期望值 E[S] 在数学上发散（因为 α < 1），因此 N55 中的分母 E[S] 无定义，必须引入截断 x_max 或改用中位数/众数作为容量规划基准。

## Corrected Claim

Pareto(α=1.1, x_min=1KB, x_max=∞) 分布的期望值 E[S] 在数学上发散（因为 α < 1），因此 N55 中的分母 E[S] 无定义，必须引入截断 x_max 或改用中位数/众数作为容量规划基准。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖：Pareto分布的期望值公式为 E[S] = (α * x_min) / (α - 1)，当 α ≤ 1 时该积分发散，故 α=1.1 时 E[S] 确实无定义（发散），陈述符合数学第一性原理。

## Search Query

Pareto distribution alpha 1.1 expected value divergence
