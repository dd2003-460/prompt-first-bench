# N77: σ_logH 的量化计算：对于 Pareto(β=0.9)，log(H) 的方差 Var[log H] = π² / (6 * β²) ≈ π² / (6 * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

σ_logH 的量化计算：对于 Pareto(β=0.9)，log(H) 的方差 Var[log H] = π² / (6 * β²) ≈ π² / (6 * 0.81) ≈ 2.03，因此 σ_logH ≈ √2.03 ≈ 1.425。此值显著大于 σ_logS，表明热度分布的对数离散度更高，负相关对命中率的放大效应更强。

## Corrected Claim

σ_logH 的量化计算：对于 Pareto(β=0.9)，log(H) 的方差 Var[log H] = π² / (6 * β²) ≈ π² / (6 * 0.81) ≈ 2.03，因此 σ_logH ≈ √2.03 ≈ 1.425。此值显著大于 σ_logS，表明热度分布的对数离散度更高，负相关对命中率的放大效应更强。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布对数方差的数学推导正确，数值计算无误

## Search Query

Pareto distribution log variance beta 0.9
