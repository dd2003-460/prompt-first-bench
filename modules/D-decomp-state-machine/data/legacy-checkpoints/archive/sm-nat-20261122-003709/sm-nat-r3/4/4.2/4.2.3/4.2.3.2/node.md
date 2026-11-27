# N186: 计算排名区间 [90001, 100000] 尾部对象的平均大小 E[S|Tail]，基于Pareto(α=1.1)分布，该值显著高于全局平均 E[S]，具体数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

计算排名区间 [90001, 100000] 尾部对象的平均大小 E[S|Tail]，基于Pareto(α=1.1)分布，该值显著高于全局平均 E[S]，具体数值为 ∫_{s_min}^{s_max} s * f(s) ds 在尾部截断下的条件期望。

## Corrected Claim

计算排名区间 [90001, 100000] 尾部对象的平均大小 E[S|Tail]，基于Pareto(α=1.1)分布，该值显著高于全局平均 E[S]，具体数值为 ∫_{s_min}^{s_max} s * f(s) ds 在尾部截断下的条件期望。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布具有重尾特性，尾部截断的条件期望必然显著高于全局平均，数学推导自洽。
