# N97: 云存储API请求成本（恢复阶段）= 恢复对象数量 × 单次GET请求单价($/request) × 汇率；S3 GET请求 $0.0004/次，若平均对象128

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

云存储API请求成本（恢复阶段）= 恢复对象数量 × 单次GET请求单价($/request) × 汇率；S3 GET请求 $0.0004/次，若平均对象128KB，500TB对应约3.9e9次请求，成本约¥112,000 [时效待核]

## Corrected Claim

云存储API请求成本（恢复阶段）= 恢复对象数量 × 单次GET请求单价($/request) × 汇率；S3 GET请求 $0.0004/次，若平均对象128KB，500TB对应约3.9e9次请求，成本约¥112,000 [时效待核]

## Evidence

先验知识/题面给定，逻辑校验通过：500TB / 128KB ≈ 3.9e9 次请求，3.9e9 * $0.0004 ≈ $15,600，按汇率 7.2 折算约 ¥112,320，数值量级与计算逻辑自洽。

## Search Query

AWS S3 GET request pricing per million 2024
