# N207: T_resident 的稳态值可通过求解 T_resident = (C_norm * N) / (λ_avg * (1 - P_eviction)) 的不动点

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

T_resident 的稳态值可通过求解 T_resident = (C_norm * N) / (λ_avg * (1 - P_eviction)) 的不动点方程获得，代入 P_eviction 的解析近似后，T_resident ≈ 23.8 / (1 - (1 - exp(-500 * T_resident / 0.119)))，需通过数值迭代求解。

## Corrected Claim

T_resident 的稳态值可通过求解 T_resident = (C_norm * N) / (λ_avg * (1 - P_eviction)) 的不动点方程获得，代入 P_eviction 的解析近似后，T_resident ≈ 23.8 / (1 - (1 - exp(-500 * T_resident / 0.119)))，需通过数值迭代求解。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合排队论/缓存模型中稳态驻留时间的不动点定义，量纲与数值量级（23.8, 0.119, 500）在工程语境下合理，无内部矛盾。
