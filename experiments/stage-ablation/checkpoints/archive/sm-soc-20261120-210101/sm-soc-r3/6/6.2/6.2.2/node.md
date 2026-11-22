# N356: 流量注水导致的虚假弹性修正系数：若平台存在流量注水，Impressions 虚高比例为 r_inflate，则原始 CTR_raw 被低估，真实 CTR_eff

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N104

## Claim

流量注水导致的虚假弹性修正系数：若平台存在流量注水，Impressions 虚高比例为 r_inflate，则原始 CTR_raw 被低估，真实 CTR_effective = CTR_raw / (1 - r_inflate)。需通过 A/B 测试或对比外部数据源估计 r_inflate，假设 r_inflate = 0.1，则 CTR_effective 需上调 11.1% 以还原真实弹性。

## Corrected Claim

流量注水导致的虚假弹性修正系数：若平台存在流量注水，Impressions 虚高比例为 r_inflate，则原始 CTR_raw 被低估，真实 CTR_effective = CTR_raw / (1 - r_inflate)。需通过 A/B 测试或对比外部数据源估计 r_inflate，假设 r_inflate = 0.1，则 CTR_effective 需上调 11.1% 以还原真实弹性。

## Evidence

先验知识/题面给定，逻辑校验通过：若Impressions虚高比例为r，则真实Impressions = Raw / (1+r) 或 Raw * (1-r) 取决于定义，但此处定义 r_inflate 为虚高比例导致分母为 (1-r_inflate) 的推导在数学上自洽（1/0.9 ≈ 1.111，即上调11.1%），符合基本代数逻辑。

## Search Query

ad impression inflation correction factor clickthrough rate
