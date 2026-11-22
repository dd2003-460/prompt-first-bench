# N80: 条件期望 E[S|f > f_median] 的积分表达式：E[S|f > f_median] = ∫_{f_median}^{f_max} S * P(S|f

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

条件期望 E[S|f > f_median] 的积分表达式：E[S|f > f_median] = ∫_{f_median}^{f_max} S * P(S|f) df / P(f > f_median)，其中 P(S|f) 由 Gaussian Copula 联合密度除以边缘密度得到，需数值积分计算。

## Corrected Claim

条件期望 E[S|f > f_median] 的积分表达式：E[S|f > f_median] = ∫_{f_median}^{f_max} S * P(S|f) df / P(f > f_median)，其中 P(S|f) 由 Gaussian Copula 联合密度除以边缘密度得到，需数值积分计算。

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的定义及基于联合密度与边缘密度的条件概率推导符合概率论基本公理，数值积分表述合理。
