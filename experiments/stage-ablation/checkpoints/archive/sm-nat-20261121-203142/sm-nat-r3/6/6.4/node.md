# N216: Gaussian Copula 密度 c(u,v;ρ) 在边界 (0,1) 处的极限值：lim_{u→0, v→1} c(u,v;ρ) = 0，因为标准正态联合

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

Gaussian Copula 密度 c(u,v;ρ) 在边界 (0,1) 处的极限值：lim_{u→0, v→1} c(u,v;ρ) = 0，因为标准正态联合密度在无穷远处趋于 0，这表明在 Pareto 支撑集的边界角点处联合密度为 0，而非峰值

## Corrected Claim

Gaussian Copula 密度 c(u,v;ρ) 在边界 (0,1) 处的极限值：lim_{u→0, v→1} c(u,v;ρ) = 0，因为标准正态联合密度在无穷远处趋于 0，这表明在 Pareto 支撑集的边界角点处联合密度为 0，而非峰值

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 密度函数在边界 (0,1) 处确实趋于 0，符合正态分布尾部性质。
