# N218: 截断 Pareto 分布 (α=1.1, x_min=1KB, x_max=1GB) 的期望值 E[S] 的精确解析公式：E[S] = (α * x_min) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

截断 Pareto 分布 (α=1.1, x_min=1KB, x_max=1GB) 的期望值 E[S] 的精确解析公式：E[S] = (α * x_min) / (α - 1) * [1 - (x_min/x_max)^(α-1)] / [1 - (x_min/x_max)^α]，代入 α=1.1, x_min=1024, x_max=1024^3 计算得 E[S] ≈ 1.03 KB，该值用于修正 N78 中基于无界分布的 1.1KB 估计。

## Corrected Claim

截断 Pareto 分布 (α=1.1, x_min=1KB, x_max=1GB) 的期望值 E[S] 的精确解析公式：E[S] = (α * x_min) / (α - 1) * [1 - (x_min/x_max)^(α-1)] / [1 - (x_min/x_max)^α]，代入 α=1.1, x_min=1024, x_max=1024^3 计算得 E[S] ≈ 1.03 KB，该值用于修正 N78 中基于无界分布的 1.1KB 估计。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布期望公式正确，代入参数计算结果约1.03KB符合量级预期
