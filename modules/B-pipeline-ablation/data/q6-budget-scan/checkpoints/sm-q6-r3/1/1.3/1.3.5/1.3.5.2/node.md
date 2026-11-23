# N162: H的最低阈值H_min计算：H_min = 1 - (T - P50_hit) / P99_origin。若T=80ms，P50_hit=50ms，P99_or

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

H的最低阈值H_min计算：H_min = 1 - (T - P50_hit) / P99_origin。若T=80ms，P50_hit=50ms，P99_origin=73.26ms，则H_min = 1 - (80-50)/73.26 = 1 - 30/73.26 ≈ 1 - 0.4095 = 0.5905。即H需≥59.05%才能满足P99≤80ms。若T=60ms，H_min = 1 - (60-50)/73.26 ≈ 1 - 0.1365 = 0.8635。

## Corrected Claim

H的最低阈值H_min计算：H_min = 1 - (T - P50_hit) / P99_origin。若T=80ms，P50_hit=50ms，P99_origin=73.26ms，则H_min = 1 - (80-50)/73.26 = 1 - 30/73.26 ≈ 1 - 0.4095 = 0.5905。即H需≥59.05%才能满足P99≤80ms。若T=60ms，H_min = 1 - (60-50)/73.26 ≈ 1 - 0.1365 = 0.8635。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 1 - 30/73.26 ≈ 0.5905 和 1 - 10/73.26 ≈ 0.8635 均正确，公式逻辑自洽。
