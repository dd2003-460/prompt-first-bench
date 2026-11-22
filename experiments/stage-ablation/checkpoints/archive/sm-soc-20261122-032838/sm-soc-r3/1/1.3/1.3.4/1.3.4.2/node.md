# N140: 有效注意力 A_eff 的构成项分解：A_eff = A_base * (1 + α_new*I_new + α_price*P_norm)，其中 A_base

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

有效注意力 A_eff 的构成项分解：A_eff = A_base * (1 + α_new*I_new + α_price*P_norm)，其中 A_base 为基准注意力，α_new 为新品溢价系数，α_price 为价格敏感度系数，P_norm 为归一化价格偏差，需分别估计 α_new 和 α_price 以识别注意力的主要驱动因素。

## Corrected Claim

有效注意力 A_eff 的构成项分解：A_eff = A_base * (1 + α_new*I_new + α_price*P_norm)，其中 A_base 为基准注意力，α_new 为新品溢价系数，α_price 为价格敏感度系数，P_norm 为归一化价格偏差，需分别估计 α_new 和 α_price 以识别注意力的主要驱动因素。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

decomposition of effective attention into base, novelty, and price components in e-commerce
