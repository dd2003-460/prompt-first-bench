# N64: NPV 平衡点的计算公式：NPV = - (GMV_Loss_ShortTerm * Discount_Factor^0) + Σ_{t=1}^{T} (GMV

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

NPV 平衡点的计算公式：NPV = - (GMV_Loss_ShortTerm * Discount_Factor^0) + Σ_{t=1}^{T} (GMV_Gain_LongTerm_t * Discount_Factor^t)。其中 GMV_Loss_ShortTerm 由 N21 给出，GMV_Gain_LongTerm_t 需基于买家留存率提升 ΔRetention_Buyer 和复购率提升 ΔRepurchase 计算。平衡点 T* 为 NPV 首次转正的时间点，通常取决于平台折扣率 r（假设 10%/月）和留存提升幅度。

## Corrected Claim

NPV 平衡点的计算公式：NPV = - (GMV_Loss_ShortTerm * Discount_Factor^0) + Σ_{t=1}^{T} (GMV_Gain_LongTerm_t * Discount_Factor^t)。其中 GMV_Loss_ShortTerm 由 N21 给出，GMV_Gain_LongTerm_t 需基于买家留存率提升 ΔRetention_Buyer 和复购率提升 ΔRepurchase 计算。平衡点 T* 为 NPV 首次转正的时间点，通常取决于平台折扣率 r（假设 10%/月）和留存提升幅度。

## Evidence

先验知识/题面给定，逻辑校验通过：NPV公式结构符合财务净现值定义（初始成本为负，未来收益折现求和），平衡点定义逻辑自洽，且作为knowledge节点无需外部来源支持。
