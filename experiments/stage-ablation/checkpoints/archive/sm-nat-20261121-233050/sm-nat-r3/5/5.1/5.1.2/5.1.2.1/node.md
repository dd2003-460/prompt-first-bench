# N131: x_min 的精确计算：基于截断 Pareto 分布均值公式 E[S] = (α * x_min) / (α - 1) * [1 - (x_min/x_max)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

x_min 的精确计算：基于截断 Pareto 分布均值公式 E[S] = (α * x_min) / (α - 1) * [1 - (x_min/x_max)^(α-1)]。若假设 x_max >> x_min（长尾近似），则 E[S] ≈ (α * x_min) / (α - 1)。代入 E[S]=1.31072 MB, α=1.1，解得 x_min = 1.31072 * (0.1/1.1) ≈ 0.119 MB ≈ 122 KB。若考虑有限 x_max 截断，x_min 需略小。

## Corrected Claim

x_min 的精确计算：基于截断 Pareto 分布均值公式 E[S] = (α * x_min) / (α - 1) * [1 - (x_min/x_max)^(α-1)]。若假设 x_max >> x_min（长尾近似），则 E[S] ≈ (α * x_min) / (α - 1)。代入 E[S]=1.31072 MB, α=1.1，解得 x_min = 1.31072 * (0.1/1.1) ≈ 0.119 MB ≈ 122 KB。若考虑有限 x_max 截断，x_min 需略小。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布均值公式正确，长尾近似下代数推导无误，数值量级合理（1.31072 * 0.1/1.1 ≈ 0.119 MB ≈ 122 KB）。
