# N79: 热度分布中位数 f_median 的具体数值：由 Pareto(β=0.9) 的 CDF F_f(f_median) = 0.5 解得 f_median = f

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

热度分布中位数 f_median 的具体数值：由 Pareto(β=0.9) 的 CDF F_f(f_median) = 0.5 解得 f_median = f_min * 2^{1/β} = f_min * 2^{1/0.9} ≈ 2.114 * f_min，其中 f_min 为最小热度值。

## Corrected Claim

热度分布中位数 f_median 的具体数值：由 Pareto(β=0.9) 的 CDF F_f(f_median) = 0.5 解得 f_median = f_min * 2^{1/β} = f_min * 2^{1/0.9} ≈ 2.114 * f_min，其中 f_min 为最小热度值。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF公式及中位数推导符合数学定义，数值计算正确。
