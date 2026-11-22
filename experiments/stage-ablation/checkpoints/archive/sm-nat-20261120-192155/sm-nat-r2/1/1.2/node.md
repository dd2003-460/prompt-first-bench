# N6: 缓存驻留集合C的构成：在LRU稳态下，C由热度排名最高的对象组成，但受大小约束；具体为：按热度r_i降序排列对象，累加大小s_i直到总和≤128GB，C即为该前

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

缓存驻留集合C的构成：在LRU稳态下，C由热度排名最高的对象组成，但受大小约束；具体为：按热度r_i降序排列对象，累加大小s_i直到总和≤128GB，C即为该前缀集合；需处理Pareto分布下热度与大小的耦合。

## Corrected Claim

缓存驻留集合C的构成：在LRU稳态下，C由热度排名最高的对象组成，但受大小约束；具体为：按热度r_i降序排列对象，累加大小s_i直到总和≤128GB，C即为该前缀集合；需处理Pareto分布下热度与大小的耦合。

## Evidence

先验知识/题面给定，逻辑校验通过
