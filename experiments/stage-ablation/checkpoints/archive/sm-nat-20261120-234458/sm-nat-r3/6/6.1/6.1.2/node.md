# N176: 稳态命中率 H_steady 的下界：在容量充足 (K>N) 且无更新时，H_steady = 1.0；考虑更新率 λ_update = 1%/day，H_st

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

稳态命中率 H_steady 的下界：在容量充足 (K>N) 且无更新时，H_steady = 1.0；考虑更新率 λ_update = 1%/day，H_steady_eff = 1 - P_invalidate = 1 - (1 - e^(-λ_update * T_residence_avg))，其中 T_residence_avg ≈ 1/500 day，H_steady_eff ≈ 0.99998

## Corrected Claim

稳态命中率 H_steady 的下界：在容量充足 (K>N) 且无更新时，H_steady = 1.0；考虑更新率 λ_update = 1%/day，H_steady_eff = 1 - P_invalidate = 1 - (1 - e^(-λ_update * T_residence_avg))，其中 T_residence_avg ≈ 1/500 day，H_steady_eff ≈ 0.99998

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合指数衰减模型，数值量级合理（1 - (1 - e^(-0.01/500)) ≈ 2e-5，即 0.99998）
