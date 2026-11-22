# N172: 市场流动性 L 的标准化定义：L = N_active_buyers_7d / N_active_buyers_peak，其中 N_active_buyers_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

市场流动性 L 的标准化定义：L = N_active_buyers_7d / N_active_buyers_peak，其中 N_active_buyers_7d 为过去7天至少浏览1次二手商品的用户数，N_active_buyers_peak 为过去12个月中的月度峰值用户数；L 的取值范围为 [0, 1]，用于计算 w_speed。

## Corrected Claim

市场流动性 L 的标准化定义：L = N_active_buyers_7d / N_active_buyers_peak，其中 N_active_buyers_7d 为过去7天至少浏览1次二手商品的用户数，N_active_buyers_peak 为过去12个月中的月度峰值用户数；L 的取值范围为 [0, 1]，用于计算 w_speed。

## Evidence

先验知识/题面给定，逻辑校验通过：分子为近期活跃用户，分母为历史峰值，比值自然落在[0,1]区间，定义自洽。
