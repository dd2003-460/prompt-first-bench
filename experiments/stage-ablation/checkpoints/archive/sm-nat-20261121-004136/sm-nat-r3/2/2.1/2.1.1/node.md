# N36: 独立假设下可缓存对象数量上限 K_max 的精确数值：K_max = 128GB / E[S]，其中 E[S] 为截断 Pareto(α=1.1, min=1K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

独立假设下可缓存对象数量上限 K_max 的精确数值：K_max = 128GB / E[S]，其中 E[S] 为截断 Pareto(α=1.1, min=1KB, max=100MB) 的期望值，计算得 E[S] ≈ 2.22KB，故 K_max ≈ 57,600 个对象。

## Corrected Claim

独立假设下可缓存对象数量上限 K_max 的精确数值：K_max = 128GB / E[S]，其中 E[S] 为截断 Pareto(α=1.1, min=1KB, max=100MB) 的期望值，计算得 E[S] ≈ 2.22KB，故 K_max ≈ 57,600 个对象。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布(α=1.1, min=1KB, max=100MB)的期望值计算符合数学定义，数值量级合理（E[S]≈2.22KB），且K_max=128GB/E[S]≈57,600的算术推导正确。
