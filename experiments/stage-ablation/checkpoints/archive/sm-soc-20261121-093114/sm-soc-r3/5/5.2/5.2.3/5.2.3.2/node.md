# N213: λ_loss 与 P_loss 的交互效应项：挂价溢价率 Premium = λ_loss * P_loss，需计算当 λ_loss=2.25 且 P_loss

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

λ_loss 与 P_loss 的交互效应项：挂价溢价率 Premium = λ_loss * P_loss，需计算当 λ_loss=2.25 且 P_loss 随时间从0.1增至0.9时，Premium 的变化区间 [0.225, 2.025]，并验证该区间是否覆盖观测到的 15-25% 溢价。

## Corrected Claim

λ_loss 与 P_loss 的交互效应项：挂价溢价率 Premium = λ_loss * P_loss，需计算当 λ_loss=2.25 且 P_loss 随时间从0.1增至0.9时，Premium 的变化区间 [0.225, 2.025]，并验证该区间是否覆盖观测到的 15-25% 溢价。

## Evidence

先验知识/题面给定，逻辑校验通过：2.25 * 0.1 = 0.225, 2.25 * 0.9 = 2.025，区间 [0.225, 2.025] 即 [22.5%, 202.5%]，确实覆盖 [15%, 25%] 区间。

## Search Query

loss aversion pricing strategy premium calculation interaction effect
