# N261: 平台流失率响应函数的具体形式：Δs_churn = 1 - exp(-β * (ΔRev_seller_high / C_switch)^γ)，其中 β 为流失

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N87, N88, N89

## Claim

平台流失率响应函数的具体形式：Δs_churn = 1 - exp(-β * (ΔRev_seller_high / C_switch)^γ)，其中 β 为流失敏感度系数，γ 为非线性指数，需基于历史卖家迁移数据校准参数。

## Corrected Claim

平台流失率响应函数的具体形式：Δs_churn = 1 - exp(-β * (ΔRev_seller_high / C_switch)^γ)，其中 β 为流失敏感度系数，γ 为非线性指数，需基于历史卖家迁移数据校准参数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

nonlinear churn rate function seller profit loss switching cost
