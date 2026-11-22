# N22: 在 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布下，LRU 队列中第 k 个对象的 W_LRU(k) 近似为 1 / (sum_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

在 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布下，LRU 队列中第 k 个对象的 W_LRU(k) 近似为 1 / (sum_{j>k} λ_j)，其中 λ_j 是对象 j 的请求速率。

## Corrected Claim

在 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布下，LRU 队列中第 k 个对象的 W_LRU(k) 近似为 1 / (sum_{j>k} λ_j)，其中 λ_j 是对象 j 的请求速率。

## Evidence

先验知识/题面给定，逻辑校验通过
