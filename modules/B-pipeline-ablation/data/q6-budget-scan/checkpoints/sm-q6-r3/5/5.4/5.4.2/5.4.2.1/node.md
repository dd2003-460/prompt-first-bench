# N259: 回源带宽需求 B_required 的计算公式为 B_required = p_miss * Q_peak * s_avg * 8 / T_slack，其中 T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

回源带宽需求 B_required 的计算公式为 B_required = p_miss * Q_peak * s_avg * 8 / T_slack，其中 T_slack 为允许的回源延迟缓冲时间（通常取P99延迟预算的10%）

## Corrected Claim

回源带宽需求 B_required 的计算公式为 B_required = p_miss * Q_peak * s_avg * 8 / T_slack，其中 T_slack 为允许的回源延迟缓冲时间（通常取P99延迟预算的10%）

## Evidence

先验知识/题面给定，逻辑校验通过
