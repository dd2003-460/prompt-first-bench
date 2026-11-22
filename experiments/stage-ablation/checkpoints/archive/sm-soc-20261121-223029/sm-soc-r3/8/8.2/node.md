# N116: 平台通知触发阈值 Threshold_notification 的量化定义：Threshold_notification = 0.05 * Average_Da

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

平台通知触发阈值 Threshold_notification 的量化定义：Threshold_notification = 0.05 * Average_Daily_Visitors，即当预期咨询概率低于日均访客数的 5% 时，系统判定为低热度商品，不推送降价通知；需验证 60% 卖家降价后咨询率是否确实低于此动态阈值。

## Corrected Claim

平台通知触发阈值 Threshold_notification 的量化定义：Threshold_notification = 0.05 * Average_Daily_Visitors，即当预期咨询概率低于日均访客数的 5% 时，系统判定为低热度商品，不推送降价通知；需验证 60% 卖家降价后咨询率是否确实低于此动态阈值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

platform notification threshold algorithm low engagement trigger
