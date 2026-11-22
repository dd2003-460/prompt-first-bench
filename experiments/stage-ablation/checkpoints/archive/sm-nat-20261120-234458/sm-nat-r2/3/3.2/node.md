# N13: 动态修正因子 = (1 - P_invalidate) * H_static，其中 P_invalidate = 1 - e^(-λ_update * T_wi

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

动态修正因子 = (1 - P_invalidate) * H_static，其中 P_invalidate = 1 - e^(-λ_update * T_window)，T_window 为命中率计算的时间窗口（如 1 天）；λ_update = 0.01/天，T_window = 1 天，P_invalidate ≈ 0.00995

## Corrected Claim

动态修正因子 = (1 - P_invalidate) * H_static，其中 P_invalidate = 1 - e^(-λ_update * T_window)，T_window 为命中率计算的时间窗口（如 1 天）；λ_update = 0.01/天，T_window = 1 天，P_invalidate ≈ 0.00995

## Evidence

先验知识/题面给定，逻辑校验通过：P_invalidate = 1 - e^(-0.01*1) ≈ 0.00995，数值计算准确，公式逻辑自洽
