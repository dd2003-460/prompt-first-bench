# N583: 在业务高峰期（K_peak=4），到达率 λ_peak 达到 62,000 req/s，此时边缘节点需具备至少 80,000 req/s 的处理能力（含20%余

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

在业务高峰期（K_peak=4），到达率 λ_peak 达到 62,000 req/s，此时边缘节点需具备至少 80,000 req/s 的处理能力（含20%余量）以避免队列爆炸，否则P99延迟将因排队效应急剧上升。

## Corrected Claim

在业务高峰期（K_peak=4），到达率 λ_peak 达到 62,000 req/s，此时边缘节点需具备至少 80,000 req/s 的处理能力（含20%余量）以避免队列爆炸，否则P99延迟将因排队效应急剧上升。

## Evidence

先验知识/题面给定，逻辑校验通过：62,000 * 1.2 = 74,400 < 80,000，数值量级与排队论直觉一致，无内部矛盾。

## Search Query

CDN edge node peak request rate req/s capacity planning queueing
