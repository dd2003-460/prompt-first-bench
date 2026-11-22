# N108: 常数修正项 K_corr = 1 + (α * β) / (α - 1) 的推导基于 Zipf 分布的渐近展开，但在 Pareto 分布下，由于尾部行为不同，该

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

常数修正项 K_corr = 1 + (α * β) / (α - 1) 的推导基于 Zipf 分布的渐近展开，但在 Pareto 分布下，由于尾部行为不同，该公式不适用；需重新推导基于 Pareto 分布的修正项，或标记为 [待核验] 并给出经验范围。

## Corrected Claim

常数修正项 K_corr = 1 + (α * β) / (α - 1) 的推导基于 Zipf 分布的渐近展开，但在 Pareto 分布下，由于尾部行为不同，该公式不适用；需重新推导基于 Pareto 分布的修正项，或标记为 [待核验] 并给出经验范围。

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf分布（离散）与Pareto分布（连续）在尾部行为及求和/积分性质上存在差异，导致基于特定分布推导的修正项不可直接通用，该陈述符合统计学基本原理。

## Search Query

Zipf vs Pareto distribution asymptotic expansion cache hit rate correction factor
