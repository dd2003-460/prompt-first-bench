# N50: 对象平均大小 S_obj 的精确计算：S_obj = μ_S = ∫_{S_min}^{S_max} s * f_Pareto(s; α=1.1, S_min=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

对象平均大小 S_obj 的精确计算：S_obj = μ_S = ∫_{S_min}^{S_max} s * f_Pareto(s; α=1.1, S_min=1KB) ds，利用截断 Pareto 分布均值公式 μ_S = (α * S_min) / (α - 1) * [1 - (S_min/S_max)^(α-1)]，代入 S_min=1KB, S_max=100MB 计算得具体数值（KB）

## Corrected Claim

对象平均大小 S_obj 的精确计算：S_obj = μ_S = ∫_{S_min}^{S_max} s * f_Pareto(s; α=1.1, S_min=1KB) ds，利用截断 Pareto 分布均值公式 μ_S = (α * S_min) / (α - 1) * [1 - (S_min/S_max)^(α-1)]，代入 S_min=1KB, S_max=100MB 计算得具体数值（KB）

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布均值公式正确，量纲一致，数值量级合理（α=1.1时均值约为S_min的10倍量级，即10KB左右，符合直觉）

## Search Query

truncated Pareto distribution mean formula alpha=1.1
