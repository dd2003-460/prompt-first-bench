# N65: 边界条件工作点 1 (低驻留时间)：当 λ_u * T_cold < 0.1 (即 T_cold < 10 days) 时，C_steady ≈ 0.1 * λ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

边界条件工作点 1 (低驻留时间)：当 λ_u * T_cold < 0.1 (即 T_cold < 10 days) 时，C_steady ≈ 0.1 * λ_u * T_cold (线性近似)，δ ≈ 1 - 0.01 * T_cold。此情形下更新惩罚 < 10%，可近似忽略。

## Corrected Claim

边界条件工作点 1 (低驻留时间)：当 λ_u * T_cold < 0.1 (即 T_cold < 10 days) 时，C_steady ≈ 0.1 * λ_u * T_cold (线性近似)，δ ≈ 1 - 0.01 * T_cold。此情形下更新惩罚 < 10%，可近似忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：当 x < 0.1 时，1-e^-x ≈ x 且 e^-x ≈ 1-x^2/2，线性近似成立，量级合理。
