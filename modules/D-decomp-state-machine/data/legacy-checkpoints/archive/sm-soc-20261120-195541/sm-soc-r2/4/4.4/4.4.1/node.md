# N50: 曝光权重敏感度系数 β_platform 的估计方法：通过 A/B 测试对比高挂价组与基准组的曝光量差异，β_platform = (Impressions_h

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

曝光权重敏感度系数 β_platform 的估计方法：通过 A/B 测试对比高挂价组与基准组的曝光量差异，β_platform = (Impressions_high - Impressions_base) / (Price_Discount_high - Price_Discount_base)，若 β_platform > 0.2 则支持平台算法驱动假设。

## Corrected Claim

曝光权重敏感度系数 β_platform 的估计方法：通过 A/B 测试对比高挂价组与基准组的曝光量差异，β_platform = (Impressions_high - Impressions_base) / (Price_Discount_high - Price_Discount_base)，若 β_platform > 0.2 则支持平台算法驱动假设。

## Evidence

先验知识/题面给定，逻辑校验通过
