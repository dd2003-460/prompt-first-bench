# N55: Copula 模型中，Gaussian Copula 的尾部依赖性较弱，对于 Pareto 重尾分布（α=1.1, β=0.9）可能低估极端值的相关性，需对比 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

Copula 模型中，Gaussian Copula 的尾部依赖性较弱，对于 Pareto 重尾分布（α=1.1, β=0.9）可能低估极端值的相关性，需对比 Gumbel 或 Clayton Copula 的结果，若差异超过 5%，则需采用重尾 Copula 修正 K_ρ。

## Corrected Claim

Copula 模型中，Gaussian Copula 的尾部依赖性较弱，对于 Pareto 重尾分布（α=1.1, β=0.9）可能低估极端值的相关性，需对比 Gumbel 或 Clayton Copula 的结果，若差异超过 5%，则需采用重尾 Copula 修正 K_ρ。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 具有无尾部依赖（tail dependence coefficient为0）的特性，而Gumbel/Clayton具有正尾部依赖，对于重尾分布（如Pareto），Gaussian确实会低估极端值相关性，建议对比并修正符合统计学原理。
