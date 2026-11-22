# N237: s_min 的量化推导：基于 10 万对象总数据量约束，若 s_min=1KB，则 Pareto(α=1.1) 的期望大小 E[size] = 1KB * 1.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

s_min 的量化推导：基于 10 万对象总数据量约束，若 s_min=1KB，则 Pareto(α=1.1) 的期望大小 E[size] = 1KB * 1.1/0.1 = 11KB，总数据量 V_total = 100,000 * 11KB = 1.1GB，远小于 128GB 缓存，导致命中率接近 100%，与 N68 的 0.65 矛盾，故 s_min 需重新校准。

## Corrected Claim

s_min 的量化推导：基于 10 万对象总数据量约束，若 s_min=1KB，则 Pareto(α=1.1) 的期望大小 E[size] = 1KB * 1.1/0.1 = 11KB，总数据量 V_total = 100,000 * 11KB = 1.1GB，远小于 128GB 缓存，导致命中率接近 100%，与 N68 的 0.65 矛盾，故 s_min 需重新校准。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布期望公式 E[X] = α/(α-1) * x_min 在 α=1.1, x_min=1KB 时计算为 11KB，总数据量 1.1GB 远小于 128GB 缓存，导致命中率接近 100% 的推导符合基本概率论与缓存原理，且与 N68 的 0.65 命中率矛盾从而反推 s_min 需校准的逻辑链条自洽。
