# N246: 计算未截断 Pareto(α=1.1) 的理论期望 E[S]：使用公式 E[S] = (α * s_min) / (α - 1)，代入 s_min=1KB，得出

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

计算未截断 Pareto(α=1.1) 的理论期望 E[S]：使用公式 E[S] = (α * s_min) / (α - 1)，代入 s_min=1KB，得出 E[S]_theoretical = 11KB。

## Corrected Claim

计算未截断 Pareto(α=1.1) 的理论期望 E[S]：使用公式 E[S] = (α * s_min) / (α - 1)，代入 s_min=1KB，得出 E[S]_theoretical = 11KB。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布期望公式 E[S] = α*s_min/(α-1) 正确，代入 α=1.1, s_min=1KB 计算得 1.1/0.1 * 1KB = 11KB，数值与量纲均合理。
