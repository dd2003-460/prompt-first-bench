# N113: 多卡方案的单位 Token 成本计算公式为 Cost_per_Token_multi = (P_card_1 + P_card_2 + P_interconne

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

多卡方案的单位 Token 成本计算公式为 Cost_per_Token_multi = (P_card_1 + P_card_2 + P_interconnect + E_total * C_elec) / (T_nominal_single * SF_efficient)，其中 SF_efficient ∈ [1.6, 1.8] 为实测加速比；需对比单卡方案 Cost_per_Token_single = P_card_single / T_nominal_single，明确 '15-25% 更高' 的结论依赖于 P_interconnect (主板/电源/机箱升级成本) 摊销到 5 年 TCO 后的具体数值。

## Corrected Claim

多卡方案的单位 Token 成本计算公式为 Cost_per_Token_multi = (P_card_1 + P_card_2 + P_interconnect + E_total * C_elec) / (T_nominal_single * SF_efficient)，其中 SF_efficient ∈ [1.6, 1.8] 为实测加速比；需对比单卡方案 Cost_per_Token_single = P_card_single / T_nominal_single，明确 '15-25% 更高' 的结论依赖于 P_interconnect (主板/电源/机箱升级成本) 摊销到 5 年 TCO 后的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-GPU TCO calculation unit token cost comparison single GPU
