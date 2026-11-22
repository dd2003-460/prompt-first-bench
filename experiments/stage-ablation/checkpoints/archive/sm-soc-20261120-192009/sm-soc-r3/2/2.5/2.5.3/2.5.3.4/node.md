# N200: 成交周期缩短的净效应量化：ΔT_wait = T_base - T_high，其中 T_high = T_base / (1 + α_filter * Pric

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

成交周期缩短的净效应量化：ΔT_wait = T_base - T_high，其中 T_high = T_base / (1 + α_filter * Price_Deviation) * (1/k_exposure)；需验证在 k_exposure > 1 且 α_filter > 0 时，ΔT_wait 是否为正且显著。

## Corrected Claim

成交周期缩短的净效应量化：ΔT_wait = T_base - T_high，其中 T_high = T_base / (1 + α_filter * Price_Deviation) * (1/k_exposure)；需验证在 k_exposure > 1 且 α_filter > 0 时，ΔT_wait 是否为正且显著。

## Evidence

先验知识/题面给定，逻辑校验通过：当 k_exposure > 1 且 α_filter > 0 时，分母 (1 + α_filter * Price_Deviation) * (1/k_exposure) 在 Price_Deviation >= 0 的常规语境下小于 1，导致 T_high < T_base，故 ΔT_wait > 0，数学推导自洽。

## Search Query

listing duration impact of price premium and exposure
