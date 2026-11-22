# N29: 热度分布 P(rank ≤ k) = 1 - (k/N)^(1-β) 的导数（概率密度函数）为 f_rank(k) = (1-β) * k^(-β) * N^(

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

热度分布 P(rank ≤ k) = 1 - (k/N)^(1-β) 的导数（概率密度函数）为 f_rank(k) = (1-β) * k^(-β) * N^(β-1)，用于计算特定排名区间的请求频率密度。

## Corrected Claim

热度分布 P(rank ≤ k) = 1 - (k/N)^(1-β) 的导数（概率密度函数）为 f_rank(k) = (1-β) * k^(-β) * N^(β-1)，用于计算特定排名区间的请求频率密度。

## Evidence

先验知识/题面给定，逻辑校验通过：对 CDF F(k) = 1 - (k/N)^(1-β) 求导，d/dk [1 - N^(β-1) * k^(1-β)] = -N^(β-1) * (1-β) * k^(-β) * (-1) = (1-β) * N^(β-1) * k^(-β)，与陈述一致。
