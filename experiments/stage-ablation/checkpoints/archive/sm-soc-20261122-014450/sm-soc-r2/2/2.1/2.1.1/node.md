# N49: 有效需求密度 D_eff 的计算公式：D_eff = D_base * (1 + α * Signal_Quality)，其中 Signal_Quality =

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

有效需求密度 D_eff 的计算公式：D_eff = D_base * (1 + α * Signal_Quality)，其中 Signal_Quality = (Seller_Rating - Avg_Rating) / Avg_Rating，α 为信号敏感度系数，需通过平台历史数据回归估计 α 的数值范围（预期 α ∈ [0.1, 0.3]）。

## Corrected Claim

有效需求密度 D_eff 的计算公式：D_eff = D_base * (1 + α * Signal_Quality)，其中 Signal_Quality = (Seller_Rating - Avg_Rating) / Avg_Rating，α 为信号敏感度系数，需通过平台历史数据回归估计 α 的数值范围（预期 α ∈ [0.1, 0.3]）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

e-commerce signal quality demand elasticity seller rating impact
