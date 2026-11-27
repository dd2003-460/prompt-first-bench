# N195: C_verify 的动态调整机制：C_verify 并非固定值，而是随买家历史核验经验增加而降低，C_verify(t) = C_verify_0 * exp(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

C_verify 的动态调整机制：C_verify 并非固定值，而是随买家历史核验经验增加而降低，C_verify(t) = C_verify_0 * exp(-δ_experience * t)，其中 δ_experience 为经验衰减系数（假设 0.05/day），需计算在降价后 48 小时内 C_verify 的变化对不等式成立区间的影响。

## Corrected Claim

C_verify 的动态调整机制：C_verify 并非固定值，而是随买家历史核验经验增加而降低，C_verify(t) = C_verify_0 * exp(-δ_experience * t)，其中 δ_experience 为经验衰减系数（假设 0.05/day），需计算在降价后 48 小时内 C_verify 的变化对不等式成立区间的影响。

## Evidence

先验知识/题面给定，逻辑校验通过
