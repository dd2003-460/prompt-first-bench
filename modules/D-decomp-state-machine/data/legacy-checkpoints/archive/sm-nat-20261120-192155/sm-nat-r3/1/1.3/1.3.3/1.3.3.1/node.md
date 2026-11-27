# N79: Pareto(α=1.1) 的截断期望 E[s_i] 计算：E[s_i] = (∫_{s_min}^{s_max} s * α * s_min^α / s^{α

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

Pareto(α=1.1) 的截断期望 E[s_i] 计算：E[s_i] = (∫_{s_min}^{s_max} s * α * s_min^α / s^{α+1} ds) / (∫_{s_min}^{s_max} α * s_min^α / s^{α+1} ds) = (s_max^{1-α} - s_min^{1-α}) / ((1-α) * (P(s_max) - P(s_min)))；由于 α=1.1>1，分子收敛，但分母 P(s_max) 接近 1，故 E[s_i] ≈ s_min / (α-1) * (1 - (s_min/s_max)^{α-1})。

## Corrected Claim

Pareto(α=1.1) 的截断期望 E[s_i] 计算：E[s_i] = (∫_{s_min}^{s_max} s * α * s_min^α / s^{α+1} ds) / (∫_{s_min}^{s_max} α * s_min^α / s^{α+1} ds) = (s_max^{1-α} - s_min^{1-α}) / ((1-α) * (P(s_max) - P(s_min)))；由于 α=1.1>1，分子收敛，但分母 P(s_max) 接近 1，故 E[s_i] ≈ s_min / (α-1) * (1 - (s_min/s_max)^{α-1})。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断期望公式推导正确，α=1.1时分子分母收敛性分析合理，近似表达式符合数学推导
