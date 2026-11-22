# N225: 修正请求间隔分布假设：对于 Pareto(β=0.9) 热度分布，单个对象的请求间隔服从指数分布（Var/E^2=1）仅在稳态且无时间局部性时成立；若存在时间局

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

修正请求间隔分布假设：对于 Pareto(β=0.9) 热度分布，单个对象的请求间隔服从指数分布（Var/E^2=1）仅在稳态且无时间局部性时成立；若存在时间局部性（如突发流量），需使用 Cox 过程，此时 Var(T_i)/E[T_i]^2 > 1，需引入过度离散参数 k 修正 ε_lru = c * k。

## Corrected Claim

修正请求间隔分布假设：对于 Pareto(β=0.9) 热度分布，单个对象的请求间隔服从指数分布（Var/E^2=1）仅在稳态且无时间局部性时成立；若存在时间局部性（如突发流量），需使用 Cox 过程，此时 Var(T_i)/E[T_i]^2 > 1，需引入过度离散参数 k 修正 ε_lru = c * k。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布对应泊松过程（CV²=1），时间局部性导致请求聚集，符合Cox过程特征（CV²>1），引入过度离散参数修正LRU误差符合排队论与缓存理论直觉。

## Search Query

coefficient of variation request inter-arrival time Zipf workload cache simulation
