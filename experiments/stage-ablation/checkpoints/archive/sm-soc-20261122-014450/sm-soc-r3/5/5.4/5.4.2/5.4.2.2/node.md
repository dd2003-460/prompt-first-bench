# N306: 稳定性判据的数值阈值：det(J) = (-α_seller + β_platform) * (-γ_buyer) > 0 且 trace(J) = -α_se

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

稳定性判据的数值阈值：det(J) = (-α_seller + β_platform) * (-γ_buyer) > 0 且 trace(J) = -α_seller + β_platform - γ_buyer < 0，需代入 N129-N131 的系数范围验证不等式是否恒成立。

## Corrected Claim

稳定性判据的数值阈值：det(J) = (-α_seller + β_platform) * (-γ_buyer) > 0 且 trace(J) = -α_seller + β_platform - γ_buyer < 0，需代入 N129-N131 的系数范围验证不等式是否恒成立。

## Evidence

先验知识/题面给定，逻辑校验通过：对于2x2实矩阵，Routh-Hurwitz稳定性判据确实要求迹(trace) < 0 且 行列式(det) > 0，公式推导符合线性系统稳定性理论。
