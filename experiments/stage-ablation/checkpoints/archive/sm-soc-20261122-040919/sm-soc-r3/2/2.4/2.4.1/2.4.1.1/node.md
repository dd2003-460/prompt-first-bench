# N226: 共享随机源定义：流量分配随机扰动项 ε_p 的方差 Var(ε_p) 等于 A/B 测试分桶随机性方差 σ²_AB 与探索机制（如 UCB 或 Thompson

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N61

## Claim

共享随机源定义：流量分配随机扰动项 ε_p 的方差 Var(ε_p) 等于 A/B 测试分桶随机性方差 σ²_AB 与探索机制（如 UCB 或 Thompson Sampling）方差 σ²_exploration 之和，即 Var(ε_p) = σ²_AB + σ²_exploration，其中 σ²_AB 由分桶比例 p_bucket 决定，σ²_exploration 由探索系数 β 决定。

## Corrected Claim

共享随机源定义：流量分配随机扰动项 ε_p 的方差 Var(ε_p) 等于 A/B 测试分桶随机性方差 σ²_AB 与探索机制（如 UCB 或 Thompson Sampling）方差 σ²_exploration 之和，即 Var(ε_p) = σ²_AB + σ²_exploration，其中 σ²_AB 由分桶比例 p_bucket 决定，σ²_exploration 由探索系数 β 决定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

recommendation system A/B testing variance exploration mechanism variance
