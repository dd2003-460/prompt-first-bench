# N230: 候选B采纳弹性中的衰减系数 β 的估计：β 反映卖家对建议价高于底价的敏感度，可通过最大似然估计从历史采纳数据中得出，β = -ln(P(Adopt|ΔP)) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

候选B采纳弹性中的衰减系数 β 的估计：β 反映卖家对建议价高于底价的敏感度，可通过最大似然估计从历史采纳数据中得出，β = -ln(P(Adopt|ΔP)) / ΔP，其中 ΔP = P_suggest - P_floor；若 β 过大，算法需更激进地压低建议价才能被采纳，导致平台 GMV 损失。

## Corrected Claim

候选B采纳弹性中的衰减系数 β 的估计：β 反映卖家对建议价高于底价的敏感度，可通过最大似然估计从历史采纳数据中得出，β = -ln(P(Adopt|ΔP)) / ΔP，其中 ΔP = P_suggest - P_floor；若 β 过大，算法需更激进地压低建议价才能被采纳，导致平台 GMV 损失。

## Evidence

先验知识/题面给定，逻辑校验通过
