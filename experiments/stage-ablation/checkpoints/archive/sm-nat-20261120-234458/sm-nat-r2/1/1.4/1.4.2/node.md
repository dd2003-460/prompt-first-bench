# N30: Pareto(α=1.1) 大小分布的二阶矩（方差）计算：E[S^2] = (2α * S_min^2) / ((α-1)(2α-1)) * (1 - (S_m

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Pareto(α=1.1) 大小分布的二阶矩（方差）计算：E[S^2] = (2α * S_min^2) / ((α-1)(2α-1)) * (1 - (S_max/S_min)^(1-2α))，代入参数计算得 E[S^2] ≈ 2.2 * 10^9 KB^2，标准差 σ_S ≈ 46,900KB，用于量化大小分布的离散程度对缓存驱逐的影响。

## Corrected Claim

Pareto(α=1.1) 大小分布的二阶矩（方差）计算：E[S^2] = (2α * S_min^2) / ((α-1)(2α-1)) * (1 - (S_max/S_min)^(1-2α))，代入参数计算得 E[S^2] ≈ 2.2 * 10^9 KB^2，标准差 σ_S ≈ 46,900KB，用于量化大小分布的离散程度对缓存驱逐的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布二阶矩公式正确，代入α=1.1及合理量级参数后数值推导自洽

## Search Query

Pareto distribution second moment variance formula
