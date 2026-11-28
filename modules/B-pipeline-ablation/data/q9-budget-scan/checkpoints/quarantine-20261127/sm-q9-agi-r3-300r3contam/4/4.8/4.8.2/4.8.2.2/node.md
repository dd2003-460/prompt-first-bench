# N227: 数值不一致判定容差公式：若 Ground_Truth 值为 V_true，模型回答值为 V_pred，当 |V_pred - V_true| / V_true 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

数值不一致判定容差公式：若 Ground_Truth 值为 V_true，模型回答值为 V_pred，当 |V_pred - V_true| / V_true > ε_numeric 时判定为数值不一致，其中 ε_numeric 设定为 5%（相对误差），对于整数计数型事实（如细胞数量）则要求完全匹配（ε_numeric = 0）。

## Corrected Claim

数值不一致判定容差公式：若 Ground_Truth 值为 V_true，模型回答值为 V_pred，当 |V_pred - V_true| / V_true > ε_numeric 时判定为数值不一致，其中 ε_numeric 设定为 5%（相对误差），对于整数计数型事实（如细胞数量）则要求完全匹配（ε_numeric = 0）。

## Evidence

先验知识/题面给定，逻辑校验通过
