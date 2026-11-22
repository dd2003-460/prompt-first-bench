# N67: 边界条件工作点 3 (过渡区)：当 λ_u * T_cold ≈ 1 (即 T_cold ≈ 100 days) 时，C_steady = 1 - 1/e ≈ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

边界条件工作点 3 (过渡区)：当 λ_u * T_cold ≈ 1 (即 T_cold ≈ 100 days) 时，C_steady = 1 - 1/e ≈ 0.632，δ = 1 - 0.632 * (1 - P_hit_cold)。此点为线性近似与饱和近似的切换阈值，需使用精确指数公式计算。

## Corrected Claim

边界条件工作点 3 (过渡区)：当 λ_u * T_cold ≈ 1 (即 T_cold ≈ 100 days) 时，C_steady = 1 - 1/e ≈ 0.632，δ = 1 - 0.632 * (1 - P_hit_cold)。此点为线性近似与饱和近似的切换阈值，需使用精确指数公式计算。

## Evidence

先验知识/题面给定，逻辑校验通过：指数饱和模型中，当时间常数与特征时间比值为1时，累积概率确实为1-1/e≈0.632，且该点通常作为线性与饱和近似的过渡阈值，数值量级与逻辑自洽。
