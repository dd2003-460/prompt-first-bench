# N175: 全局P99延迟的混合分布模型：整体P99不是加权平均，而是全局延迟分布的第99百分位。设 F_city(x) 和 F_remote(x) 分别为城市和偏远地区的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

全局P99延迟的混合分布模型：整体P99不是加权平均，而是全局延迟分布的第99百分位。设 F_city(x) 和 F_remote(x) 分别为城市和偏远地区的延迟分布函数，整体分布 F_total(x) = 0.8 * F_city(x) + 0.2 * F_remote(x)。P99_total 是满足 F_total(P99) = 0.99 的 x 值。由于 P99 位于尾部，主要受高延迟子群（偏远地区未命中）影响。需解方程 0.8 * F_city(P99) + 0.2 * F_remote(P99) = 0.99。

## Corrected Claim

全局P99延迟的混合分布模型：整体P99不是加权平均，而是全局延迟分布的第99百分位。设 F_city(x) 和 F_remote(x) 分别为城市和偏远地区的延迟分布函数，整体分布 F_total(x) = 0.8 * F_city(x) + 0.2 * F_remote(x)。P99_total 是满足 F_total(P99) = 0.99 的 x 值。由于 P99 位于尾部，主要受高延迟子群（偏远地区未命中）影响。需解方程 0.8 * F_city(P99) + 0.2 * F_remote(P99) = 0.99。

## Evidence

先验知识/题面给定，逻辑校验通过：混合分布的CDF定义及分位数求解逻辑符合概率论基本原理

## Search Query

percentile of weighted mixture of distributions
