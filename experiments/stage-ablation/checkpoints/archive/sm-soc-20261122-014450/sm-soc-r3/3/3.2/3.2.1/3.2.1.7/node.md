# N202: 高挂价下的需求下降比例计算：当 P_list = 1.2 * P_market 时，代入 Q(P) = Q_0 * exp(-ε_p * 0.2)。若 ε_p 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61, N62, N63

## Claim

高挂价下的需求下降比例计算：当 P_list = 1.2 * P_market 时，代入 Q(P) = Q_0 * exp(-ε_p * 0.2)。若 ε_p = 2.0，则 Q/Q_0 = exp(-0.4) ≈ 0.67，即需求下降 33%。这与题面‘短周期’矛盾，除非存在 R_exposure > 1/0.67 ≈ 1.5 的曝光补偿。

## Corrected Claim

高挂价下的需求下降比例计算：当 P_list = 1.2 * P_market 时，代入 Q(P) = Q_0 * exp(-ε_p * 0.2)。若 ε_p = 2.0，则 Q/Q_0 = exp(-0.4) ≈ 0.67，即需求下降 33%。这与题面‘短周期’矛盾，除非存在 R_exposure > 1/0.67 ≈ 1.5 的曝光补偿。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 exp(-0.4) ≈ 0.6703 正确，1 - 0.6703 ≈ 0.33 正确，1/0.6703 ≈ 1.49 ≈ 1.5 正确，逻辑推导自洽。
