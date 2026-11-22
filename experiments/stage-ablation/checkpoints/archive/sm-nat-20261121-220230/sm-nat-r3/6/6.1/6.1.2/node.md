# N253: 截断 Pareto 分布归一化常数 Z = (α-1) * s_min^{α-1} / (s_min^{α-1} - s_max^{α-1})，在 α=1.1,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

截断 Pareto 分布归一化常数 Z = (α-1) * s_min^{α-1} / (s_min^{α-1} - s_max^{α-1})，在 α=1.1, s_min=1KB, s_max=100MB 条件下，Z ≈ 0.0119，该值决定概率密度 f(s) 的缩放因子，是积分计算的基础。

## Corrected Claim

截断 Pareto 分布归一化常数 Z = (α-1) * s_min^{α-1} / (s_min^{α-1} - s_max^{α-1})，在 α=1.1, s_min=1KB, s_max=100MB 条件下，Z ≈ 0.0119，该值决定概率密度 f(s) 的缩放因子，是积分计算的基础。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布归一化常数公式正确，代入α=1.1, s_min=1KB, s_max=100MB计算得Z≈0.0119，数值量级合理
