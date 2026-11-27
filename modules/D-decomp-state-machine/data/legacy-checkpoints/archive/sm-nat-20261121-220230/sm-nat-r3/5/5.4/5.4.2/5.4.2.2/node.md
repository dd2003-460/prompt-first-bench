# N249: 静态内容折损可忽略的阈值：当 P_invalid = 1 - exp(-u*T_resident) < 0.001 时，折损对命中率影响 <0.1%。对于 u=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

静态内容折损可忽略的阈值：当 P_invalid = 1 - exp(-u*T_resident) < 0.001 时，折损对命中率影响 <0.1%。对于 u=0.001/天，要求 T_resident < 1.0 天；若 T_resident=0.5 天，P_invalid ≈ 0.0005，确实可忽略。

## Corrected Claim

静态内容折损可忽略的阈值：当 P_invalid = 1 - exp(-u*T_resident) < 0.001 时，折损对命中率影响 <0.1%。对于 u=0.001/天，要求 T_resident < 1.0 天；若 T_resident=0.5 天，P_invalid ≈ 0.0005，确实可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（1-exp(-0.001*0.5)≈0.0005<0.001），且符合指数衰减近似规律
