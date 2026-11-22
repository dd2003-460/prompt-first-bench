# N208: 在 N_cap=100 且 P_resident=0.5 的工作点下，T_avg_resident ≈ 100 / (5.787e5 * 0.5) ≈ 0.00

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

在 N_cap=100 且 P_resident=0.5 的工作点下，T_avg_resident ≈ 100 / (5.787e5 * 0.5) ≈ 0.000346 天，代表低存活率下的短驻留时间，影响更新惩罚项的计算。

## Corrected Claim

在 N_cap=100 且 P_resident=0.5 的工作点下，T_avg_resident ≈ 100 / (5.787e5 * 0.5) ≈ 0.000346 天，代表低存活率下的短驻留时间，影响更新惩罚项的计算。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 100 / (5.787e5 * 0.5) ≈ 0.0003456 与陈述一致，量纲与逻辑自洽。
