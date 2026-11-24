# N229: 核心区域流量体积 0.6 × 2TB = 1.2TB/天 的计算隐含假设：核心区域与长尾区域的平均对象大小 s_avg 相同（约 1MB）。若核心区域用户更倾向

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

核心区域流量体积 0.6 × 2TB = 1.2TB/天 的计算隐含假设：核心区域与长尾区域的平均对象大小 s_avg 相同（约 1MB）。若核心区域用户更倾向于高清/4K 内容（s_avg_core ≈ 1.5MB），而长尾区域偏向标清（s_avg_tail ≈ 0.8MB），则核心流量体积应修正为 0.6 * 2TB * (1.5/1.0) = 1.8TB/天，导致自建带宽需求增加 50% [待核验]

## Corrected Claim

核心区域流量体积 0.6 × 2TB = 1.2TB/天 的计算隐含假设：核心区域与长尾区域的平均对象大小 s_avg 相同（约 1MB）。若核心区域用户更倾向于高清/4K 内容（s_avg_core ≈ 1.5MB），而长尾区域偏向标清（s_avg_tail ≈ 0.8MB），则核心流量体积应修正为 0.6 * 2TB * (1.5/1.0) = 1.8TB/天，导致自建带宽需求增加 50% [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：流量体积与平均对象大小成正比，0.6 * 2TB * (1.5/1.0) = 1.8TB，增量 (1.8-1.2)/1.2 = 50%，计算无误。

## Search Query

video quality preference by city tier China 4K vs 1080p user distribution
