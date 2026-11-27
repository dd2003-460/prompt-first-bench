# N44: ‘性价比指数’ $CPI$ 中 $QualityScore$ 的计算公式：$QualityScore = \frac{N_{positive\_reviews}

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15, N16, N17

## Claim

‘性价比指数’ $CPI$ 中 $QualityScore$ 的计算公式：$QualityScore = \frac{N_{positive\_reviews}}{N_{total\_reviews}} \times \log(1 + N_{views})$。该公式结合了卖家信誉（好评率）和商品热度（浏览量对数），确保高溢价但低信誉的商品在 $CPI$ 中得分较低，从而被算法降权。

## Corrected Claim

‘性价比指数’ $CPI$ 中 $QualityScore$ 的计算公式：$QualityScore = \frac{N_{positive\_reviews}}{N_{total\_reviews}} \times \log(1 + N_{views})$。该公式结合了卖家信誉（好评率）和商品热度（浏览量对数），确保高溢价但低信誉的商品在 $CPI$ 中得分较低，从而被算法降权。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于分子（好评率）的统计修正，子节点2聚焦于整体得分的下游应用（惩罚/权重），两者在逻辑层级和功能上正交，无重复。然而，父节点明确给出了包含对数浏览量项的完整公式，子节点仅覆盖了分子修正和下游阈值应用，完全缺失了对分母/乘数项（浏览量对数部分）的任何分解、解释或参数讨论，导致覆盖不全。）
