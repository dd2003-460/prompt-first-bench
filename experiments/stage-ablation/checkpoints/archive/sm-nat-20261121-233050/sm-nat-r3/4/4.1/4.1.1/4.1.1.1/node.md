# N106: Pareto(α=1.1) 分布在 α < 2 时方差发散，导致样本均值 E[S] 对 x_min 极度敏感；若 x_min 偏差 10%，E[S] 偏差将超过

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Pareto(α=1.1) 分布在 α < 2 时方差发散，导致样本均值 E[S] 对 x_min 极度敏感；若 x_min 偏差 10%，E[S] 偏差将超过 10%，从而改变 C_total 与 M/C 的比值，需通过截断点 x_max 或总容量约束反推 x_min 以消除歧义。

## Corrected Claim

Pareto(α=1.1) 分布在 α < 2 时方差发散，导致样本均值 E[S] 对 x_min 极度敏感；若 x_min 偏差 10%，E[S] 偏差将超过 10%，从而改变 C_total 与 M/C 的比值，需通过截断点 x_max 或总容量约束反推 x_min 以消除歧义。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布α<2时方差确实发散，样本均值对截断参数敏感符合统计规律

## Search Query

Pareto distribution alpha < 2 variance divergence sensitivity of mean to xmin
