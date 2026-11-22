# N50: 短期访问模式波动导致的缓存污染率 P_short_term = P(object accessed in [t, t+δ] but evicted by LRU

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

短期访问模式波动导致的缓存污染率 P_short_term = P(object accessed in [t, t+δ] but evicted by LRU before t+δ)，该值与热度分布的局部性参数 β 负相关，β 越小（尾部越重），污染率越高。

## Corrected Claim

短期访问模式波动导致的缓存污染率 P_short_term = P(object accessed in [t, t+δ] but evicted by LRU before t+δ)，该值与热度分布的局部性参数 β 负相关，β 越小（尾部越重），污染率越高。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 缓存机制下，重尾分布（小 β）意味着更多低频对象被访问，这些对象在短暂访问后极易被后续更热或更频繁的对象挤出，导致短期污染率升高，符合缓存理论直觉。

## Search Query

cache pollution rate short term access pattern Pareto beta
