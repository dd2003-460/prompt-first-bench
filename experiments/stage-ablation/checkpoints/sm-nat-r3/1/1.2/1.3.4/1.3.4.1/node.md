# N94: 在 x_min=100 Bytes 假设下，Pareto(α=1.1) 分布的均值 E[S] = 1.1 * 100 = 110 Bytes，导致基于均值的缓存

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

在 x_min=100 Bytes 假设下，Pareto(α=1.1) 分布的均值 E[S] = 1.1 * 100 = 110 Bytes，导致基于均值的缓存对象数 K_avg = 1.374e11 / 110 ≈ 1.25e9，远超 N=1e5，意味着缓存可容纳全部对象。

## Corrected Claim

在 x_min=100 Bytes 假设下，Pareto(α=1.1) 分布的均值 E[S] = 1.1 * 100 = 110 Bytes，导致基于均值的缓存对象数 K_avg = 1.374e11 / 110 ≈ 1.25e9，远超 N=1e5，意味着缓存可容纳全部对象。

## Evidence

先验知识/题面给定，逻辑校验通过
