# N112: 共享随机源：LRU 队列中第 i 个对象被替换前的累积访问次数 D_i 服从几何分布，其期望 E[D_i] = 1 / p_i，其中 p_i 是对象 i 在任意

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

共享随机源：LRU 队列中第 i 个对象被替换前的累积访问次数 D_i 服从几何分布，其期望 E[D_i] = 1 / p_i，其中 p_i 是对象 i 在任意时刻被新对象挤出的概率，p_i 由缓存中所有对象的相对访问频率 λ_j/λ_total 决定。

## Corrected Claim

共享随机源：LRU 队列中第 i 个对象被替换前的累积访问次数 D_i 服从几何分布，其期望 E[D_i] = 1 / p_i，其中 p_i 是对象 i 在任意时刻被新对象挤出的概率，p_i 由缓存中所有对象的相对访问频率 λ_j/λ_total 决定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache replacement probability geometric distribution stack distance
