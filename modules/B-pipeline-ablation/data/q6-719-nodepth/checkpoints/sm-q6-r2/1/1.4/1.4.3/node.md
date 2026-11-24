# N62: 混合策略的P99延迟 P99_mix 不是简单的加权平均，而是由核心区域流量占比 P_core 和长尾区域流量占比 P_tail = 1 - P_core 决定

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

混合策略的P99延迟 P99_mix 不是简单的加权平均，而是由核心区域流量占比 P_core 和长尾区域流量占比 P_tail = 1 - P_core 决定的分布分位数计算：P99_mix = F^{-1}_{mix}(0.99)，其中 F_{mix} 是核心与长尾延迟分布的混合分布函数。若 P_core >= 0.99，则 P99_mix ≈ P99_core；若 P_core < 0.99，则 P99_mix 受 P99_tail 影响显著。

## Corrected Claim

混合策略的P99延迟 P99_mix 不是简单的加权平均，而是由核心区域流量占比 P_core 和长尾区域流量占比 P_tail = 1 - P_core 决定的分布分位数计算：P99_mix = F^{-1}_{mix}(0.99)，其中 F_{mix} 是核心与长尾延迟分布的混合分布函数。若 P_core >= 0.99，则 P99_mix ≈ P99_core；若 P_core < 0.99，则 P99_mix 受 P99_tail 影响显著。

## Evidence

先验知识/题面给定，逻辑校验通过：混合分布的分位数定义及边界条件（P_core>=0.99时P99由核心决定）符合概率论基本性质
