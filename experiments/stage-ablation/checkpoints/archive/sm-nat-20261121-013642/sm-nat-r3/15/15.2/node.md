# N286: 稳态下更新惩罚的精确计算：f_update = 1 - λ_u * T_residence_avg * (1 - P_hit_cold)。其中 T_reside

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N99

## Claim

稳态下更新惩罚的精确计算：f_update = 1 - λ_u * T_residence_avg * (1 - P_hit_cold)。其中 T_residence_avg 由 N91 给出，P_hit_cold 由 N62-N64 定义。在 λ_u=0.01/day 且 T_residence_avg≈50 days (N70) 时，f_update ≈ 1 - 0.01 * 50 * (1 - 0.5) = 0.75，即折损 25%，而非原命题声称的可忽略。

## Corrected Claim

稳态下更新惩罚的精确计算：f_update = 1 - λ_u * T_residence_avg * (1 - P_hit_cold)。其中 T_residence_avg 由 N91 给出，P_hit_cold 由 N62-N64 定义。在 λ_u=0.01/day 且 T_residence_avg≈50 days (N70) 时，f_update ≈ 1 - 0.01 * 50 * (1 - 0.5) = 0.75，即折损 25%，而非原命题声称的可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 f_update = 1 - λ_u * T_residence_avg * (1 - P_hit_cold) 在给定参数 λ_u=0.01, T=50, P=0.5 下计算结果为 1 - 0.01*50*0.5 = 0.75，折损 25%，数学推导自洽且量级合理。
