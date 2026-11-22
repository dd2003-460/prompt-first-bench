# N183: N62 的 C_steady 计算工作点 3（过渡区）：当 T_cold ≈ 100 days 时，C_steady = 1 - 1/e ≈ 0.632，P_h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

N62 的 C_steady 计算工作点 3（过渡区）：当 T_cold ≈ 100 days 时，C_steady = 1 - 1/e ≈ 0.632，P_hit_cold = 0 时 δ = 1 - 0.632 = 0.368，此点为线性近似与饱和近似的切换阈值，需使用精确指数公式计算。

## Corrected Claim

N62 的 C_steady 计算工作点 3（过渡区）：当 T_cold ≈ 100 days 时，C_steady = 1 - 1/e ≈ 0.632，P_hit_cold = 0 时 δ = 1 - 0.632 = 0.368，此点为线性近似与饱和近似的切换阈值，需使用精确指数公式计算。

## Evidence

先验知识/题面给定，逻辑校验通过：1 - 1/e ≈ 0.632 是数学常数，δ = 1 - 0.632 = 0.368 计算正确，符合指数衰减模型在过渡区的定义。
