# N96: 蒙特卡洛模拟联合分布 P(S_i, R_i) 的具体参数设置：使用 N=10^5 个样本，S_i ~ Pareto(α=1.1, x_min=1KB, x_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

蒙特卡洛模拟联合分布 P(S_i, R_i) 的具体参数设置：使用 N=10^5 个样本，S_i ~ Pareto(α=1.1, x_min=1KB, x_max=100MB)，R_i ~ Pareto(β=0.9, x_min=1)，通过 Gaussian Copula 引入 ρ=-0.3 的相关性，需给出模拟代码伪代码或关键步骤以确保可复现性。

## Corrected Claim

蒙特卡洛模拟联合分布 P(S_i, R_i) 的具体参数设置：使用 N=10^5 个样本，S_i ~ Pareto(α=1.1, x_min=1KB, x_max=100MB)，R_i ~ Pareto(β=0.9, x_min=1)，通过 Gaussian Copula 引入 ρ=-0.3 的相关性，需给出模拟代码伪代码或关键步骤以确保可复现性。

## Evidence

先验知识/题面给定，逻辑校验通过
