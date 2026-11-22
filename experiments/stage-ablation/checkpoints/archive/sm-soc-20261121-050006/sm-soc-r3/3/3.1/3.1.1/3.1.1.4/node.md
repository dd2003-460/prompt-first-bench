# N226: 下游投影 4c：认知负荷对注意力噪声的调节，当商品描述长度 L_desc 超过阈值 L_crit (如 500 字) 时，σ²_attention 增加 20-

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N68

## Claim

下游投影 4c：认知负荷对注意力噪声的调节，当商品描述长度 L_desc 超过阈值 L_crit (如 500 字) 时，σ²_attention 增加 20-30%，进一步降低标签的传递效率，需通过 A/B 测试验证描述长度与标签阅读率的相关性。

## Corrected Claim

下游投影 4c：认知负荷对注意力噪声的调节，当商品描述长度 L_desc 超过一定阈值时，σ²_attention 可能增加，进一步降低标签的传递效率，具体阈值与增幅需通过 A/B 测试验证描述长度与标签阅读率的相关性。

## Evidence

[质询]具体数值（500字阈值、20-30%噪声增加）缺乏普适性实证支持，属于特定实验条件下的经验参数，不同认知模型或用户群体下可能显著不同。 | 先验知识/题面给定，逻辑校验通过（认知负荷增加导致注意力资源分配不均，进而增加噪声符合认知心理学基本直觉），但具体数值为经验估计，无外部来源直接支持。

## Search Query

cognitive load description length label reading rate A/B test
