# N32: 热度排名 k 的标准化变量 Z_rank = (k - μ_rank) / σ_rank，其中 μ_rank = (N+1)/2，σ_rank = sqrt(N

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

热度排名 k 的标准化变量 Z_rank = (k - μ_rank) / σ_rank，其中 μ_rank = (N+1)/2，σ_rank = sqrt(N(N+1)(2N+1)/6 - μ_rank^2)，用于 Copula 模型中的相关性计算。

## Corrected Claim

热度排名 k 的标准化变量 Z_rank = (k - μ_rank) / σ_rank，其中 μ_rank = (N+1)/2，σ_rank = sqrt(N(N+1)(2N+1)/6 - μ_rank^2)，用于 Copula 模型中的相关性计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式中 μ_rank 为 1 到 N 均匀分布的均值，σ_rank 为对应标准差，标准化变量定义符合统计学常规，用于 Copula 模型合理。
