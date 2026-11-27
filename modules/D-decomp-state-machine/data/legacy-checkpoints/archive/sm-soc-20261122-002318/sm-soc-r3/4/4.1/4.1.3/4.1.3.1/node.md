# N167: 线性近似工作点（低溢价区）：当 ΔP_anchor < 5% 时，DWL_linear = 0.5 * ΔP_anchor * ΔQ_linear，其中 ΔQ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

线性近似工作点（低溢价区）：当 ΔP_anchor < 5% 时，DWL_linear = 0.5 * ΔP_anchor * ΔQ_linear，其中 ΔQ_linear = -ε_price * Q_old * (ΔP_anchor / P_old)，ε_price 为需求价格弹性（二手市场通常 1.5-2.5），该点适用于小幅价格信号干扰。

## Corrected Claim

线性近似工作点（低溢价区）：当 ΔP_anchor < 5% 时，DWL_linear = 0.5 * ΔP_anchor * ΔQ_linear，其中 ΔQ_linear = -ε_price * Q_old * (ΔP_anchor / P_old)，ε_price 为需求价格弹性（二手市场通常 1.5-2.5），该点适用于小幅价格信号干扰。

## Evidence

先验知识/题面给定，逻辑校验通过：DWL公式符合微积分近似原理，弹性取值符合二手市场经验规律
