# N172: 当用户地理分布从集中（80%核心/20%长尾）变为分散（50%核心/50%长尾）时，混合策略的P99延迟 P99_mix 从 0.8*P99_core + 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

当用户地理分布从集中（80%核心/20%长尾）变为分散（50%核心/50%长尾）时，混合策略的P99延迟 P99_mix 从 0.8*P99_core + 0.2*P99_tail ≈ 0.8*100ms + 0.2*200ms = 120ms 变为 0.5*100ms + 0.5*200ms = 150ms，延迟上升 25%。

## Corrected Claim

当用户地理分布从集中（80%核心/20%长尾）变为分散（50%核心/50%长尾）时，混合策略的P99延迟 P99_mix 从 0.8*P99_core + 0.2*P99_tail ≈ 0.8*100ms + 0.2*200ms = 120ms 变为 0.5*100ms + 0.5*200ms = 150ms，延迟上升 25%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（0.8*100+0.2*200=120, 0.5*100+0.5*200=150），百分比变化计算正确（(150-120)/120=25%），且符合加权平均延迟随分布变化的线性逻辑。

## Search Query

Hybrid CDN latency calculation geographic distribution
