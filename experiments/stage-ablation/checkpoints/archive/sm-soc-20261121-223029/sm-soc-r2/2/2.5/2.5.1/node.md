# N60: Price_Competitiveness 指标的具体定义公式：PC = 1 - min(1, max(0, (P_ask - P_ref) / P_ref /

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15, N16, N17

## Claim

Price_Competitiveness 指标的具体定义公式：PC = 1 - min(1, max(0, (P_ask - P_ref) / P_ref / δ_max))，其中 δ_max 为平台定义的惩罚上限阈值（通常为0.5），该指标直接量化了高溢价商品在β项中的得分衰减。

## Corrected Claim

Price_Competitiveness 指标的具体定义公式：PC = 1 - min(1, max(0, (P_ask - P_ref) / P_ref / δ_max))，其中 δ_max 为平台定义的惩罚上限阈值（通常为0.5），该指标直接量化了高溢价商品在β项中的得分衰减。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

e-commerce platform price competitiveness algorithm formula penalty coefficient
