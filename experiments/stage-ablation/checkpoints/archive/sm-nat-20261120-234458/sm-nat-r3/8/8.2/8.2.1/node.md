# N196: 热对象更新概率工作点：对于 Top 1% 热对象，T_res ≈ 0.0018 天，P_update = 1 - exp(-0.01 * 0.0018) ≈ 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

热对象更新概率工作点：对于 Top 1% 热对象，T_res ≈ 0.0018 天，P_update = 1 - exp(-0.01 * 0.0018) ≈ 1.8e-5，折减因子 ≈ 0.999982

## Corrected Claim

热对象更新概率工作点：对于 Top 1% 热对象，T_res ≈ 0.0018 天，P_update = 1 - exp(-0.01 * 0.0018) ≈ 1.8e-5，折减因子 ≈ 0.999982

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1 - exp(-0.01 * 0.0018) ≈ 1 - (1 - 0.000018) = 1.8e-5，折减因子 1 - 1.8e-5 = 0.999982，数值量级与数学推导一致。
