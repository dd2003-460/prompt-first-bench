# N64: NPV 平衡点的计算公式：NPV = - (GMV_Loss_ShortTerm * Discount_Factor^0) + Σ_{t=1}^{T} (GMV

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

NPV 平衡点的计算公式：NPV = - (GMV_Loss_ShortTerm * Discount_Factor^0) + Σ_{t=1}^{T} (GMV_Gain_LongTerm_t * Discount_Factor^t)。其中 GMV_Loss_ShortTerm 由 N21 给出，GMV_Gain_LongTerm_t 需基于买家留存率提升 ΔRetention_Buyer 和复购率提升 ΔRepurchase 计算。平衡点 T* 为 NPV 首次转正的时间点，通常取决于平台折扣率 r（假设 10%/月）和留存提升幅度。

## Corrected Claim

NPV 平衡点的计算公式：NPV = - (GMV_Loss_ShortTerm * Discount_Factor^0) + Σ_{t=1}^{T} (GMV_Gain_LongTerm_t * Discount_Factor^t)。其中 GMV_Loss_ShortTerm 由 N21 给出，GMV_Gain_LongTerm_t 需基于买家留存率提升 ΔRetention_Buyer 和复购率提升 ΔRepurchase 计算。平衡点 T* 为 NPV 首次转正的时间点，通常取决于平台折扣率 r（假设 10%/月）和留存提升幅度。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个核心组成部分：初始成本（短期损失）、收益流（长期增益）以及求解目标（平衡点T*）。三者逻辑独立，无重叠，且共同覆盖了NPV计算所需的全部关键变量和求解逻辑，无冗余。）
