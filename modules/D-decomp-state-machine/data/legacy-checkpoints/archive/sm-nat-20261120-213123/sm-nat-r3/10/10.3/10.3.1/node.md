# N177: 修正因子 K(ρ) 的精确计算需基于二元对数正态分布的条件期望：K(ρ) = E[S|H∈Top_k] / E[S|H∈Random]，其中 S = exp(μ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

修正因子 K(ρ) 的精确计算需基于二元对数正态分布的条件期望：K(ρ) = E[S|H∈Top_k] / E[S|H∈Random]，其中 S = exp(μ_S + σ_S Z_S), H = exp(μ_H + σ_H Z_H)，Z_S, Z_H 为相关系数 ρ 的标准正态变量。需计算积分 E[exp(μ_S + σ_S Z_S) | Z_H > z_k]，z_k = Φ^{-1}(1 - k/N)。

## Corrected Claim

修正因子 K(ρ) 的精确计算需基于二元对数正态分布的条件期望：K(ρ) = E[S|H∈Top_k] / E[S|H∈Random]，其中 S = exp(μ_S + σ_S Z_S), H = exp(μ_H + σ_H Z_H)，Z_S, Z_H 为相关系数 ρ 的标准正态变量。需计算积分 E[exp(μ_S + σ_S Z_S) | Z_H > z_k]，z_k = Φ^{-1}(1 - k/N)。

## Evidence

先验知识/题面给定，逻辑校验通过
