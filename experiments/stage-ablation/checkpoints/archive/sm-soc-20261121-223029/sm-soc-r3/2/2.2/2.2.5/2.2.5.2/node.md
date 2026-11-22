# N181: 平台通知阈值 Threshold_notification 的动态调整机制：若 Threshold = 0.05 * Average_Daily_Visitor

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

平台通知阈值 Threshold_notification 的动态调整机制：若 Threshold = 0.05 * Average_Daily_Visitors，需量化 Average_Daily_Visitors 在降价事件发生前后的变化率 ΔV，若 ΔV < -50% 则阈值降低，导致更多商品被判定为‘低热度’而不触发通知，从而放大‘无咨询’的感知比例。

## Corrected Claim

平台通知阈值 Threshold_notification 的动态调整机制：若 Threshold = 0.05 * Average_Daily_Visitors，需量化 Average_Daily_Visitors 在降价事件发生前后的变化率 ΔV，若 ΔV < -50% 则阈值降低，导致更多商品被判定为‘低热度’而不触发通知，从而放大‘无咨询’的感知比例。

## Evidence

先验知识/题面给定，逻辑校验通过：阈值与日均访客成正比，访客大幅下降导致阈值降低，进而使更多商品低于阈值被判定为低热度，逻辑链条自洽。
