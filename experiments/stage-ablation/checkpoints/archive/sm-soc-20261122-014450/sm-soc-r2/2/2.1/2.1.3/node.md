# N51: 高信号卖家筛选阈值 T_filter：买家仅在 P_list <= V_buyer + λ * C_verify 时发起咨询，其中 V_buyer 为买家估值分

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

高信号卖家筛选阈值 T_filter：买家仅在 P_list <= V_buyer + λ * C_verify 时发起咨询，其中 V_buyer 为买家估值分布 N(μ_v, σ_v)，λ 为风险调整因子；需计算在 P_list = 1.2 * P_market 条件下，满足该不等式的买家比例 P(Consult | High_P) 与 P(Consult | Market_P) 的比值，预期比值 > 1.5 以支撑短周期假设。

## Corrected Claim

高信号卖家筛选阈值 T_filter：买家仅在 P_list <= V_buyer + λ * C_verify 时发起咨询，其中 V_buyer 为买家估值分布 N(μ_v, σ_v)，λ 为风险调整因子；需计算在 P_list = 1.2 * P_market 条件下，满足该不等式的买家比例 P(Consult | High_P) 与 P(Consult | Market_P) 的比值，预期比值 > 1.5 以支撑短周期假设。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price threshold buyer consultation probability second hand goods
