# N262: 扩容触发阈值 Traffic_Threshold 为当前物理带宽容量的 80%（即 0.8 × Provisioned_Bandwidth），超过此阈值将导致 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

扩容触发阈值 Traffic_Threshold 为当前物理带宽容量的 80%（即 0.8 × Provisioned_Bandwidth），超过此阈值将导致 P99 延迟因队列堆积而急剧上升，需提前扩容以避免 SLA 违规

## Corrected Claim

扩容触发阈值 Traffic_Threshold 为当前物理带宽容量的 80%（即 0.8 × Provisioned_Bandwidth），超过此阈值将导致 P99 延迟因队列堆积而急剧上升，需提前扩容以避免 SLA 违规

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node bandwidth utilization threshold for scaling 80% rule
