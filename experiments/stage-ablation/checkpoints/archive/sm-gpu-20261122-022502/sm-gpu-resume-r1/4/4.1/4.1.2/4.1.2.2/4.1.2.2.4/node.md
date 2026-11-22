# N780: H100 SXM BF16 方案中，'单位吞吐成本 $817/token-s' 的计算隐含了 CapEx 一次性投入未摊销的假设；若按 3 年折旧 (直线法，残

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N242, N243, N244

## Claim

H100 SXM BF16 方案中，'单位吞吐成本 $817/token-s' 的计算隐含了 CapEx 一次性投入未摊销的假设；若按 3 年折旧 (直线法，残值 0) 计算，年化 CapEx 成本为 $8,333/年，需转换为每小时成本 ($0.95/h) 以与电费/OpEx 对比，从而修正性价比指标。

## Corrected Claim

H100 SXM BF16 方案中，'单位吞吐成本 $817/token-s' 的计算隐含了 CapEx 一次性投入未摊销的假设；若按 3 年折旧 (直线法，残值 0) 计算，年化 CapEx 成本为 $8,333/年，需转换为每小时成本 ($0.95/h) 以与电费/OpEx 对比，从而修正性价比指标。

## Evidence

先验知识/题面给定，逻辑校验通过：$8,333/年 ÷ 8760小时/年 ≈ $0.95/小时，数值量级与计算逻辑自洽。
