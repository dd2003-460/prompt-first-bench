# N91: H_effective 的精确值重算：采用 N47 修正后的 F_decay ≈ 0.99999991，H_effective = H_corrected * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

H_effective 的精确值重算：采用 N47 修正后的 F_decay ≈ 0.99999991，H_effective = H_corrected * F_decay = 0.679 * 0.99999991 ≈ 0.6789999389，与静态命中率 H_corrected=0.679 的相对误差为 1.2e-8，确认更新率影响在工程精度内可忽略。

## Corrected Claim

H_effective 的精确值重算：采用 N47 修正后的 F_decay ≈ 0.99999991，H_effective = H_corrected * F_decay = 0.679 * 0.99999991 ≈ 0.6789999389，与静态命中率 H_corrected=0.679 的相对误差为 1.2e-8，确认更新率影响在工程精度内可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：0.679 * 0.99999991 = 0.67899993889，与0.679的相对误差约为1.3e-8，量级与陈述一致，计算自洽。
