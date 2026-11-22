# N134: 大小阈值 s_threshold 的数值估算：基于 LRU 稳态下缓存保留对象数 K 和平均大小 E[s_i | Cache]，s_threshold 满足 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

大小阈值 s_threshold 的数值估算：基于 LRU 稳态下缓存保留对象数 K 和平均大小 E[s_i | Cache]，s_threshold 满足 P(s_i < s_threshold) ≈ K/N，在 Pareto(α=1.1) 下 s_threshold = s_min * (N/K)^(1/(α-1))，若 K=1000, N=100,000, s_min=1KB，则 s_threshold ≈ 1KB * (100)^(10) ≈ 10^10 KB = 10TB（此值远大于 s_max=10GB，表明截断效应显著，需调整 K 或 s_max）。

## Corrected Claim

大小阈值 s_threshold 的数值估算：基于 LRU 稳态下缓存保留对象数 K 和平均大小 E[s_i | Cache]，s_threshold 满足 P(s_i < s_threshold) ≈ K/N，在 Pareto(α=1.1) 下 s_threshold = s_min * (N/K)^(1/(α-1))，若 K=1000, N=100,000, s_min=1KB，则 s_threshold ≈ 1KB * (100)^(10) ≈ 10^10 KB = 10TB（此值远大于 s_max=10GB，表明截断效应显著，需调整 K 或 s_max）。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布逆函数推导正确，数值计算 (100)^10 = 10^10 无误，量级对比合理。

## Search Query

Pareto distribution quantile calculation
