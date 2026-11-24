# N412: 源站出口带宽 B_origin 的峰值需求计算公式：B_origin_peak = B_avg * K_peak * H_miss_total，其中 B_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

源站出口带宽 B_origin 的峰值需求计算公式：B_origin_peak = B_avg * K_peak * H_miss_total，其中 B_avg=493.8Mbps, K_peak取典型值4, H_miss_total取0.05，得出 B_origin_peak ≈ 98.76 Mbps，决定了单源站出口链路规格。

## Corrected Claim

源站出口带宽 B_origin 的峰值需求计算公式：B_origin_peak = B_avg * K_peak * H_miss_total，其中 B_avg=493.8Mbps, K_peak取典型值4, H_miss_total取0.05，得出 B_origin_peak ≈ 98.76 Mbps，决定了单源站出口链路规格。

## Evidence

先验知识/题面给定，逻辑校验通过：493.8 * 4 * 0.05 = 98.76，计算无误，量级合理。
