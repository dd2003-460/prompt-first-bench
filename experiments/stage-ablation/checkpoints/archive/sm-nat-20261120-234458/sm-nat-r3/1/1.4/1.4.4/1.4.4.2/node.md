# N101: Pareto(α=1.1) 大小分布的一阶矩（平均大小）μ_S = (α * S_min) / (α - 1) = (1.1 * 1KB) / 0.1 = 11

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Pareto(α=1.1) 大小分布的一阶矩（平均大小）μ_S = (α * S_min) / (α - 1) = (1.1 * 1KB) / 0.1 = 11KB，这是未截断的理论均值；若考虑 S_max 截断，需使用截断均值公式修正，但主导项仍由 S_min 决定。

## Corrected Claim

Pareto(α=1.1) 大小分布的一阶矩（平均大小）μ_S = (α * S_min) / (α - 1) = (1.1 * 1KB) / 0.1 = 11KB，这是未截断的理论均值；若考虑 S_max 截断，需使用截断均值公式修正，但主导项仍由 S_min 决定。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布一阶矩公式正确，数值计算无误，截断修正说明合理

## Search Query

Pareto distribution mean alpha 1.1
