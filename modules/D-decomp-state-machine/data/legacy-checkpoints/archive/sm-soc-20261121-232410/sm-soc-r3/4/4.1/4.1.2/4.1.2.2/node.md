# N156: CTR 与 Conversion_Rate 的协方差效应：由于 CTR 与 Conversion_Rate 存在正相关（r=0.6），仅调整 w3 可能导致高 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

CTR 与 Conversion_Rate 的协方差效应：由于 CTR 与 Conversion_Rate 存在正相关（r=0.6），仅调整 w3 可能导致高 CTR 但低 Conversion 的商品被过度惩罚；需引入修正项 Δw3 = w3_base * (1 - r * (CTR_norm - CVR_norm))，以避免误伤高流量商品。

## Corrected Claim

CTR 与 Conversion_Rate 存在正相关（r=0.6），仅调整 w3 可能导致高 CTR 但低 Conversion 的商品被过度惩罚；需引入基于 CTR 与 CVR 差异的修正项以避免误伤高流量商品。

## Evidence

[质询]修正项公式 Δw3 = w3_base * (1 - r * (CTR_norm - CVR_norm)) 缺乏明确的理论推导或标准文献支持，属于启发式经验公式，且未定义 CTR_norm 和 CVR_norm 的具体归一化方式，可能导致量纲或数值范围问题。 | 先验知识/题面给定，逻辑校验通过，但具体公式为经验性修正，缺乏直接来源支持，降级为定性表述。
