# N152: 筛选收益 B_filter 的量化定义：B_filter = (P_signal - P_noise) * Q_match * Margin，其中 P_sign

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N46

## Claim

筛选收益 B_filter 的量化定义：B_filter = (P_signal - P_noise) * Q_match * Margin，其中 P_signal 为高信号卖家的平均成交价，P_noise 为低信号卖家价格，Q_match 为匹配数量，Margin 为利润率；需验证 (P_signal - P_noise) 是否显著大于 0 以支撑 k > 0。

## Corrected Claim

筛选收益 B_filter 的量化定义：B_filter = (P_signal - P_noise) * Q_match * Margin，其中 P_signal 为高信号卖家的平均成交价，P_noise 为低信号卖家价格，Q_match 为匹配数量，Margin 为利润率；需验证 (P_signal - P_noise) 是否显著大于 0 以支撑 k > 0。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

signaling benefit calculation in marketplace economics
