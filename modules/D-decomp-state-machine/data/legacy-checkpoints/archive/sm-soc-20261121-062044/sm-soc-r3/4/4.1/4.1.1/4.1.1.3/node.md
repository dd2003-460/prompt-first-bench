# N193: 似然函数 P(D|H) 的参数化：假设 D (挂价溢价率, 成交周期) 服从多元正态分布 N(μ_H, Σ_H)，其中 μ_H 为假设 H 下的均值向量，Σ_H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

似然函数 P(D|H) 的参数化：假设 D (挂价溢价率, 成交周期) 服从多元正态分布 N(μ_H, Σ_H)，其中 μ_H 为假设 H 下的均值向量，Σ_H 为协方差矩阵；需通过 MLE 估计 μ_H 和 Σ_H，若 Σ_H 奇异则需加正则化项 λI。

## Corrected Claim

似然函数 P(D|H) 的参数化：假设 D (挂价溢价率, 成交周期) 服从多元正态分布 N(μ_H, Σ_H)，其中 μ_H 为假设 H 下的均值向量，Σ_H 为协方差矩阵；需通过 MLE 估计 μ_H 和 Σ_H，若 Σ_H 奇异则需加正则化项 λI。

## Evidence

先验知识/题面给定，逻辑校验通过
