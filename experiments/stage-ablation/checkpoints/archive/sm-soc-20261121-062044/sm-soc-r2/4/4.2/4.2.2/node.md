# N72: 置信度判定规则：若 Var(P_markup | λ) / Var(P_markup_total) > 0.8，则损失厌恶解释力充分，置信度为 0.85；若 <

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

置信度判定规则：若 Var(P_markup | λ) / Var(P_markup_total) > 0.8，则损失厌恶解释力充分，置信度为 0.85；若 < 0.5，则需引入其他噪声项，置信度降至 0.6，中间值线性插值。

## Corrected Claim

置信度判定规则：若 Var(P_markup | λ) / Var(P_markup_total) > 0.8，则损失厌恶解释力充分，置信度为 0.85；若 < 0.5，则需引入其他噪声项，置信度降至 0.6，中间值线性插值。

## Evidence

先验知识/题面给定，逻辑校验通过
