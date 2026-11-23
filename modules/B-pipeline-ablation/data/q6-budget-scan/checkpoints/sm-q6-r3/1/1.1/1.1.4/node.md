# N37: T（SLA目标值）的确定依据：基于用户体验研究，P99延迟<200ms对应用户感知'流畅'，200-500ms对应'可接受'，>500ms对应'卡顿'；需结合业

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

T（SLA目标值）的确定依据：基于用户体验研究，P99延迟<200ms对应用户感知'流畅'，200-500ms对应'可接受'，>500ms对应'卡顿'；需结合业务KPI（如留存率与延迟的弹性系数）确定T的具体数值，通常T=300ms为平衡点

## Corrected Claim

T（SLA目标值）的确定依据：基于用户体验研究，P99延迟<200ms对应用户感知'流畅'，200-500ms对应'可接受'，>500ms对应'卡顿'；需结合业务KPI（如留存率与延迟的弹性系数）确定T的具体数值，通常T=300ms为平衡点

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

user experience latency threshold 200ms 500ms CDN SLA target
