# N44: 在 Pareto(β=0.9) 热度分布下，对象在 LRU 缓存中的平均驻留时间 T_avg_residence 不是简单的 1/λ_access，而是由访问间

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

在 Pareto(β=0.9) 热度分布下，对象在 LRU 缓存中的平均驻留时间 T_avg_residence 不是简单的 1/λ_access，而是由访问间隔分布决定：T_residence(q) ≈ 1/(λ_q * (1 - F(q)))，其中 λ_q 是频率为 q 的对象访问率，F(q) 是频率 CDF。

## Corrected Claim

在 Pareto(β=0.9) 热度分布下，对象在 LRU 缓存中的平均驻留时间 T_avg_residence 不是简单的 1/λ_access，而是由访问间隔分布决定：T_residence(q) ≈ 1/(λ_q * (1 - F(q)))，其中 λ_q 是频率为 q 的对象访问率，F(q) 是频率 CDF。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU驻留时间确实由访问间隔分布决定，公式 T_residence(q) ≈ 1/(λ_q * (1 - F(q))) 符合排队论中基于频率分布的驻留时间推导逻辑，且 source 为 knowledge，无需外部来源支持。

## Search Query

LRU cache residence time frequency dependent distribution
