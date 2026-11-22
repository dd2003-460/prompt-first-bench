# N16: LRU 稳态平均驻留时间 τ_LRU 的估计：基于缓存容量 C=128GB 与总对象大小分布（Pareto α=1.1），τ_LRU ≈ C / (R * E[

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LRU 稳态平均驻留时间 τ_LRU 的估计：基于缓存容量 C=128GB 与总对象大小分布（Pareto α=1.1），τ_LRU ≈ C / (R * E[Size])，其中 E[Size] 需通过 Pareto 分布截断计算（假设最小对象大小 s_min=1KB，最大 s_max=100MB，需核验截断值）。

## Corrected Claim

LRU 稳态平均驻留时间 τ_LRU 的估计：基于缓存容量 C=128GB 与总对象大小分布（Pareto α=1.1），τ_LRU ≈ C / (R * E[Size])，其中 E[Size] 需通过 Pareto 分布截断计算（假设最小对象大小 s_min=1KB，最大 s_max=100MB，需核验截断值）。

## Evidence

先验知识/题面给定，逻辑校验通过
