# N38: 负相关修正因子 correction_factor 的量化定义：correction_factor = 1 - (ρ * σ_size * σ_rank) / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

负相关修正因子 correction_factor 的量化定义：correction_factor = 1 - (ρ * σ_size * σ_rank) / (μ_size * μ_rank)，用于修正 C_effective 公式中 ρ 对有效容量的影响，需基于 Pareto 分布计算 σ_size 和 σ_rank。

## Corrected Claim

负相关修正因子 correction_factor 的量化定义：correction_factor = 1 - (ρ * σ_size * σ_rank) / (μ_size * μ_rank)，用于修正 C_effective 公式中 ρ 对有效容量的影响，需基于 Pareto 分布计算 σ_size 和 σ_rank。

## Evidence

先验知识/题面给定，逻辑校验通过
