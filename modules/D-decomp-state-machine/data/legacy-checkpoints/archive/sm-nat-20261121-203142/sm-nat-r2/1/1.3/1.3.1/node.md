# N31: Gaussian Copula 下，给定边缘分布 F_S, F_R 和 Pearson 相关系数 ρ=-0.3，联合 CDF 为 C(u,v) = Φ_2(u,

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Gaussian Copula 下，给定边缘分布 F_S, F_R 和 Pearson 相关系数 ρ=-0.3，联合 CDF 为 C(u,v) = Φ_2(u, v; ρ)，其中 Φ_2 是二元标准正态 CDF，该结构允许直接计算联合概率密度 f(S,R) = f_S(S) * f_R(R) * c(F_S(S), F_R(R))

## Corrected Claim

Gaussian Copula 下，给定边缘分布 F_S, F_R 和 Pearson 相关系数 ρ=-0.3，联合 CDF 为 C(u,v) = Φ_2(u, v; ρ)，其中 Φ_2 是二元标准正态 CDF，该结构允许直接计算联合概率密度 f(S,R) = f_S(S) * f_R(R) * c(F_S(S), F_R(R))

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 的定义即为二元标准正态 CDF，且 Sklar 定理保证了联合密度可分解为边缘密度与 Copula 密度的乘积，公式结构正确。

## Search Query

Gaussian Copula joint distribution formula Pearson correlation
