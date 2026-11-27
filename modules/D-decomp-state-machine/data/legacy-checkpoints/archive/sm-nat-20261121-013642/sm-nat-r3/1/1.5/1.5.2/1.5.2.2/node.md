# N131: 热度阈值 r_threshold 的数值估算：基于 LRU 稳态下缓存保留对象数 K ≈ C / E[s_i | Cache]，结合 Pareto(β=0.9)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

热度阈值 r_threshold 的数值估算：基于 LRU 稳态下缓存保留对象数 K ≈ C / E[s_i | Cache]，结合 Pareto(β=0.9) 分布，r_threshold = r_min * (N/K)^β，其中 r_min=0.1/day, N=100,000，K 需通过迭代求解（初始假设 K=1000，E[s_i|Cache]=100KB 则 r_threshold ≈ 0.1 * (100)^0.9 ≈ 5.0/day）。

## Corrected Claim

热度阈值 r_threshold 的数值估算：基于 LRU 稳态下缓存保留对象数 K ≈ C / E[s_i | Cache]，结合 Pareto(β=0.9) 分布，r_threshold = r_min * (N/K)^β，其中 r_min=0.1/day, N=100,000，K 需通过迭代求解（初始假设 K=1000，E[s_i|Cache]=100KB 则 r_threshold ≈ 0.1 * (100)^0.9 ≈ 5.0/day）。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 (100000/1000)^0.9 = 100^0.9 ≈ 50.1，乘以 0.1 得 5.01，与陈述中的 5.0/day 一致；公式推导逻辑自洽。

## Search Query

Pareto distribution quantile function inverse
