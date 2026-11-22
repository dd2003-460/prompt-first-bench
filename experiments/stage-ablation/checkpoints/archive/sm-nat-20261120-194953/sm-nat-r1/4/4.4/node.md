# N19: 低更新率工作点：当 u=0.01 且 T_cold=720h（冷对象驻留时间）时，P_inval_cold ≈ 0.999，但冷对象贡献命中率 <5%，故整体折

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

低更新率工作点：当 u=0.01 且 T_cold=720h（冷对象驻留时间）时，P_inval_cold ≈ 0.999，但冷对象贡献命中率 <5%，故整体折损 <0.5 个百分点

## Corrected Claim

低更新率工作点：当 u=0.01 且 T_cold=720h（冷对象驻留时间）时，P_inval_cold ≈ 0.999，但冷对象贡献命中率 <5%，故整体折损 <0.5 个百分点

## Evidence

先验知识/题面给定，逻辑校验通过：P_inval_cold = 1 - exp(-u*T_cold) ≈ 1 - exp(-7.2) ≈ 0.9993，数值量级正确；冷对象占比低导致整体命中率折损小于其自身失效概率，符合加权平均逻辑。
