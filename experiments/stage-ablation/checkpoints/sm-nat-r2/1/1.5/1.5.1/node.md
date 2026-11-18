# N36: 基于负相关系数 ρ=-0.3，假设大小 S 和热度 H 的对数值服从二元正态分布，Copula 相关系数 ρ_c 与 Pearson ρ 的转换关系为 ρ = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

基于负相关系数 ρ=-0.3，假设大小 S 和热度 H 的对数值服从二元正态分布，Copula 相关系数 ρ_c 与 Pearson ρ 的转换关系为 ρ = (e^{ρ_c} - 1) * sqrt(Var(lnS)Var(lnH)) / (E[S]E[H])，需反解 ρ_c 以构建联合分布。

## Corrected Claim

基于负相关系数 ρ=-0.3，假设大小 S 和热度 H 的对数值服从二元正态分布，Copula 相关系数 ρ_c 与 Pearson ρ 的转换关系为 ρ = (e^{ρ_c} - 1) * sqrt(Var(lnS)Var(lnH)) / (E[S]E[H])，需反解 ρ_c 以构建联合分布。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

conversion between Pearson correlation and Gaussian copula correlation
