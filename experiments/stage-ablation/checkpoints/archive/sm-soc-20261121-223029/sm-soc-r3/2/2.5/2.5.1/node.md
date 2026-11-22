# N60: Price_Competitiveness 指标的具体定义公式：PC = 1 - min(1, max(0, (P_ask - P_ref) / P_ref /

- **status**: pending
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

父节点级核验未通过：不完备（子节点在主题上是正交的（一个关注边界条件/数值验证，一个关注参数敏感性/微积分分析），且没有冗余。但是，分解不完备，因为父节点明确提到了该指标用于量化'高溢价商品在β项中的得分衰减'，而两个子节点均聚焦于PC指标本身的数学性质（边界、导数），完全缺失了PC指标与β项（权重/衰减机制）之间关联关系的分解，导致父节点中关于'在β项中'这一关键应用场景未被覆盖。）

## Search Query

e-commerce platform price competitiveness algorithm formula penalty coefficient
