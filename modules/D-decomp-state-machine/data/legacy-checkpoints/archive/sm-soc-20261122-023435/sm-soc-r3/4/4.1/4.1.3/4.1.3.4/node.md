# N160: GMV 净效应的二阶项修正：ΔGMV_2nd = 0.5 * ε_q * (ΔP)^2 / P_old，该二阶项在价格变动幅度较大时（如 ΔP/P_old > 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

GMV 净效应的二阶项修正：ΔGMV_2nd = 0.5 * ε_q * (ΔP)^2 / P_old，该二阶项在价格变动幅度较大时（如 ΔP/P_old > 10%）不可忽略，它修正了一阶线性近似的偏差。

## Corrected Claim

GMV 净效应的二阶项修正：ΔGMV_2nd = 0.5 * ε_q * (ΔP)^2 / P_old，该二阶项在价格变动幅度较大时（如 ΔP/P_old > 10%）不可忽略，它修正了一阶线性近似的偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合泰勒展开二阶项的数学定义，量纲与经济学直觉一致。
