# N191: 建立条件期望积分表达式：E[S|Top K] = [∫_{h_min}^{h_max} ∫_{s_min}^{s_max} s * f(s|h) ds dh] 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

建立条件期望积分表达式：E[S|Top K] = [∫_{h_min}^{h_max} ∫_{s_min}^{s_max} s * f(s|h) ds dh] / P(H ∈ [h_min, h_max])，其中 f(s|h) 由 N99 的联合密度除以边缘密度 f_H(h) 得到。

## Corrected Claim

建立条件期望积分表达式：E[S|Top K] = [∫_{h_min}^{h_max} ∫_{s_min}^{s_max} s * f(s|h) ds dh] / P(H ∈ [h_min, h_max])，其中 f(s|h) 由 N99 的联合密度除以边缘密度 f_H(h) 得到。

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的定义及条件密度 f(s|h) = f(s,h)/f_H(h) 的推导符合概率论基本公理，积分区间与分母归一化逻辑自洽。
