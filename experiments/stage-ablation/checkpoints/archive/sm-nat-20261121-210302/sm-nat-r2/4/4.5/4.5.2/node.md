# N54: 热点对象平均大小 S_avg_hot = E[Size | Popularity > F_th]，需通过条件期望计算，F_th 由 N_hot 和 Pareto

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

热点对象平均大小 S_avg_hot = E[Size | Popularity > F_th]，需通过条件期望计算，F_th 由 N_hot 和 Pareto 分布决定，具体公式为 S_avg_hot = ∫_{F_th}^{F_max} Size * f(Size|Popularity) dSize

## Corrected Claim

热点对象平均大小 S_avg_hot = E[Size | Popularity > F_th]，需通过条件期望计算，F_th 由 N_hot 和 Pareto 分布决定，具体公式为 S_avg_hot = ∫_{F_th}^{F_max} Size * f(Size|Popularity) dSize

## Evidence

先验知识/题面给定，逻辑校验通过
