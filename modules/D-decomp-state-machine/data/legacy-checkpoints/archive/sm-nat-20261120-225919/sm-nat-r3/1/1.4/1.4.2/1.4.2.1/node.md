# N125: N36 中声称 E[S]_trunc ≈ 215KB 是计算错误，正确值应接近 S_min * α/(α-1) ≈ 11KB（因 S_max/S_min 极大，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

N36 中声称 E[S]_trunc ≈ 215KB 是计算错误，正确值应接近 S_min * α/(α-1) ≈ 11KB（因 S_max/S_min 极大，截断项趋近于 0），需重新计算以修正后续 K_max 推导。

## Corrected Claim

N36 中声称 E[S]_trunc ≈ 215KB 是计算错误，正确值应接近 S_min * α/(α-1) ≈ 11KB（因 S_max/S_min 极大，截断项趋近于 0），需重新计算以修正后续 K_max 推导。

## Evidence

先验知识/题面给定，逻辑校验通过：帕累托分布截断期望公式 E[S] ≈ S_min * α/(α-1) 在 S_max >> S_min 时成立，数值量级合理。
