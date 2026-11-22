# N224: 下游投影 4a：注意力噪声方差 σ²_attention 的计算公式，基于 Beta 分布性质 Var(1[ReadLabel]) = (α_attention

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N68

## Claim

下游投影 4a：注意力噪声方差 σ²_attention 的计算公式，基于 Beta 分布性质 Var(1[ReadLabel]) = (α_attention * β_attention) / ((α_attention + β_attention)^2 * (α_attention + β_attention + 1))，需估计 α/β 参数以量化噪声大小。

## Corrected Claim

下游投影 4a：注意力噪声方差 σ²_attention 的计算公式，基于 Beta 分布性质 Var(1[ReadLabel]) = (α_attention * β_attention) / ((α_attention + β_attention)^2 * (α_attention + β_attention + 1))，需估计 α/β 参数以量化噪声大小。

## Evidence

先验知识/题面给定，逻辑校验通过：Beta分布方差公式正确，且指示函数方差与Beta分布参数关联符合概率论推导

## Search Query

beta distribution variance attention noise calculation
