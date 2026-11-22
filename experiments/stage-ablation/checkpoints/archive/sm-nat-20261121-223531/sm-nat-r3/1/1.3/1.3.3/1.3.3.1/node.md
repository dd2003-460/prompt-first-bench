# N109: 蒙特卡洛模拟的随机数生成参数配置：对象大小 S_i 服从截断 Pareto(α=1.1, s_min=1KB, s_max=100MB)，热度 H_i 服从 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33, N34, N36

## Claim

蒙特卡洛模拟的随机数生成参数配置：对象大小 S_i 服从截断 Pareto(α=1.1, s_min=1KB, s_max=100MB)，热度 H_i 服从 Pareto(β=0.9, h_min=1)，相关系数 ρ=-0.3 通过 Cholesky 分解对数正态近似或 Copula 函数实现，样本量 N=100,000，随机种子固定为 42 以保证可复现性。

## Corrected Claim

蒙特卡洛模拟的随机数生成参数配置：对象大小 S_i 服从截断 Pareto(α=1.1, s_min=1KB, s_max=100MB)，热度 H_i 服从 Pareto(β=0.9, h_min=1)，相关系数 ρ=-0.3 通过 Cholesky 分解对数正态近似或 Copula 函数实现，样本量 N=100,000，随机种子固定为 42 以保证可复现性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Monte Carlo simulation correlated Pareto distribution Cholesky decomposition
