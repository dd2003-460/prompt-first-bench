# N225: 下游投影 4b：标签有效性偏差的量化，当 σ²_attention > 0.1 时，高价值买家（WTP > P_median * 1.2）忽略标签的概率 P(I

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N68

## Claim

下游投影 4b：标签有效性偏差的量化，当 σ²_attention > 0.1 时，高价值买家（WTP > P_median * 1.2）忽略标签的概率 P(Ignore | HighValue) 显著高于低价值买家，导致干预效果在高端商品上失效。

## Corrected Claim

在注意力方差较大的情况下，高价值买家可能比低价值买家更倾向于忽略价格标签，从而削弱干预效果，但具体阈值和显著性需依赖特定实证数据。

## Evidence

[质询]该陈述包含具体的经验性阈值（σ²_attention > 0.1）和特定的行为经济学结论（高价值买家忽略标签概率显著更高导致干预失效），这属于特定模型或实证研究的经验事实，无法从第一性原理或通用逻辑中严格推导出来。 | source=knowledge，逻辑上自洽（高价值买家对价格敏感度低，若注意力分散则更可能忽略标签，符合直觉），但缺乏外部来源支持具体阈值和量化关系，且属于经验事实，故降级。

## Search Query

label effectiveness bias high value buyers attention noise
