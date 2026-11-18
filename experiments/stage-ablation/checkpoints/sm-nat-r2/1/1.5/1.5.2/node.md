# N37: 在二元正态 Copula 下，给定对象热度排名 r_i，其大小 S_i 的条件分布均值 E[S_i | r_i] = x_min * exp(μ_S + ρ_c

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

在二元正态 Copula 下，给定对象热度排名 r_i，其大小 S_i 的条件分布均值 E[S_i | r_i] = x_min * exp(μ_S + ρ_c * σ_S * Φ^{-1}(F_H(r_i)))，其中 Φ^{-1} 是标准正态逆 CDF，F_H(r_i) 是热度的累积分布函数值。

## Corrected Claim

在二元正态 Copula 下，给定对象热度排名 r_i，其大小 S_i 的条件分布均值 E[S_i | r_i] = x_min * exp(μ_S + ρ_c * σ_S * Φ^{-1}(F_H(r_i)))，其中 Φ^{-1} 是标准正态逆 CDF，F_H(r_i) 是热度的累积分布函数值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

conditional expectation of lognormal distribution given rank in bivariate normal copula
