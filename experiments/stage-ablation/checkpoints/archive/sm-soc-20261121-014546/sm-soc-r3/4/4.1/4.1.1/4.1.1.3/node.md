# N275: 锚点权重衰减系数 λ_decay：随着时间推移，卖家对初始锚点的依赖程度衰减，λ_decay = 0.95/week。在干预后第 t 周，有效锚点强度为 β_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N82

## Claim

锚点权重衰减系数 λ_decay：随着时间推移，卖家对初始锚点的依赖程度衰减，λ_decay = 0.95/week。在干预后第 t 周，有效锚点强度为 β_i * λ_decay^t，该系数决定了干预效果的长期稳定性及偏离度回升速度。

## Corrected Claim

锚点权重衰减系数 λ_decay：随着时间推移，卖家对初始锚点的依赖程度衰减，λ_decay = 0.95/week。在干预后第 t 周，有效锚点强度为 β_i * λ_decay^t，该系数决定了干预效果的长期稳定性及偏离度回升速度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

temporal decay of price anchoring effect in dynamic online markets
