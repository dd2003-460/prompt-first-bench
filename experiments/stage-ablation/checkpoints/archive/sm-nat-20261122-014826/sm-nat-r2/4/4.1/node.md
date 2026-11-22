# N15: 版本失效导致的缓存污染比例（Stale Fraction）计算：在更新率 u=1%/天、对象平均驻留时间 T_res 服从指数分布或基于 LRU 堆栈深度分布的

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

版本失效导致的缓存污染比例（Stale Fraction）计算：在更新率 u=1%/天、对象平均驻留时间 T_res 服从指数分布或基于 LRU 堆栈深度分布的条件下，稳态下缓存中陈旧对象的比例 P_stale = 1 - exp(-u * T_avg_residency)，其中 T_avg_residency 需结合 LRU 稳态字节命中率（约 0.85-0.95）反推，估算值约为 0.005-0.015（即 0.5%-1.5%）。

## Corrected Claim

版本失效导致的缓存污染比例（Stale Fraction）计算：在更新率 u=1%/天、对象平均驻留时间 T_res 服从指数分布或基于 LRU 堆栈深度分布的条件下，稳态下缓存中陈旧对象的比例 P_stale = 1 - exp(-u * T_avg_residency)，其中 T_avg_residency 需结合 LRU 稳态字节命中率（约 0.85-0.95）反推，估算值约为 0.005-0.015（即 0.5%-1.5%）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P_stale = 1 - exp(-u * T_avg) 符合指数分布下陈旧概率的数学定义；代入 u=0.01/day 及典型驻留时间（约 0.5-1.5 天，对应高命中率场景），计算结果 0.005-0.015 量级合理且自洽。

## Search Query

LRU cache stale object fraction update rate exponential decay formula
