# N49: 信号解码机制：买家将降价幅度 ΔP 映射为负面信号强度 S_neg = α * (P_ask_initial - P_ask_current) / P_mark

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N12

## Claim

信号解码机制：买家将降价幅度 ΔP 映射为负面信号强度 S_neg = α * (P_ask_initial - P_ask_current) / P_market，其中 α 为信号敏感度系数，若 S_neg > 阈值 θ_defect，则买家认为商品存在缺陷或卖家急迫，导致咨询意愿下降。

## Corrected Claim

信号解码机制：买家将降价幅度 ΔP 映射为负面信号强度 S_neg = α * (P_ask_initial - P_ask_current) / P_market，其中 α 为信号敏感度系数，若 S_neg > 阈值 θ_defect，则买家认为商品存在缺陷或卖家急迫，导致咨询意愿下降。

## Evidence

先验知识/题面给定，逻辑校验通过
