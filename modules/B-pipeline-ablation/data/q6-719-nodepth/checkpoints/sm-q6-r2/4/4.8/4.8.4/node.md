# N133: 混合策略的 P99 延迟 P99_mix 不是简单的加权最大值，而是基于分位数计算的加权分位数，公式为 P99_mix = F^{-1}(0.99) where

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

混合策略的 P99 延迟 P99_mix 不是简单的加权最大值，而是基于分位数计算的加权分位数，公式为 P99_mix = F^{-1}(0.99) where F(x) = P_core * F_core(x) + (1-P_core) * F_tail(x)，F_core 和 F_tail 分别为核心和长尾区域的延迟分布函数。

## Corrected Claim

混合策略的 P99 延迟 P99_mix 不是简单的加权最大值，而是基于分位数计算的加权分位数，公式为 P99_mix = F^{-1}(0.99) where F(x) = P_core * F_core(x) + (1-P_core) * F_tail(x)，F_core 和 F_tail 分别为核心和长尾区域的延迟分布函数。

## Evidence

先验知识/题面给定，逻辑校验通过：混合分布的分位数定义即为逆累积分布函数，公式推导符合概率论基本原理。

## Search Query

hybrid CDN P99 latency weighted quantile calculation
