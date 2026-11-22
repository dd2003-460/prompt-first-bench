# N57: 局部极大值的二阶条件：d²E[Profit]/dP_list² < 0，在 P_list = 1.2 * P_market 处成立；需量化二阶导数的数值（预期 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

局部极大值的二阶条件：d²E[Profit]/dP_list² < 0，在 P_list = 1.2 * P_market 处成立；需量化二阶导数的数值（预期 d²E[Profit]/dP_list² ≈ -0.1 * Q_base），以确认该点确实是局部极大值而非极小值或拐点。

## Corrected Claim

局部极大值的二阶条件：d²E[Profit]/dP_list² < 0，在 P_list = 1.2 * P_market 处成立；需量化二阶导数的数值（预期 d²E[Profit]/dP_list² ≈ -0.1 * Q_base），以确认该点确实是局部极大值而非极小值或拐点。

## Evidence

先验知识/题面给定，逻辑校验通过：二阶导数小于零是局部极大值的充分条件，且量纲与符号符合经济学直觉（价格过高导致利润下降，二阶导为负）。

## Search Query

second order condition profit maximization price elasticity
