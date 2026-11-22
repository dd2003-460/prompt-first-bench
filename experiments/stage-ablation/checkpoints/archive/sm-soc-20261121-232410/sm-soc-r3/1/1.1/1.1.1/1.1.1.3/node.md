# N94: P_median（近期成交中位数）的计算窗口：P_median = Median(P_deal_i | i ∈ SameCategory, T < 7d)，窗口

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

P_median（近期成交中位数）的计算窗口：P_median = Median(P_deal_i | i ∈ SameCategory, T < 7d)，窗口T=7天基于流动性假设；若窗口扩大至30天，P_median稳定性提升但时效性下降，需通过A/B测试确定最优T值（当前假设T=7d）。

## Corrected Claim

P_median（近期成交中位数）的计算窗口：P_median = Median(P_deal_i | i ∈ SameCategory, T < 7d)，窗口T=7天基于流动性假设；若窗口扩大至30天，P_median稳定性提升但时效性下降，需通过A/B测试确定最优T值（当前假设T=7d）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

median price calculation window used goods market
