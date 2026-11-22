# N23: 因果推断的混杂变量控制：需排除'季节性需求波动'和'商品稀缺度变化'两个混杂因素；若控制后效应量 β 仍显著（p < 0.05），则因果置信度提升；否则需引入工

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

因果推断的混杂变量控制：需排除'季节性需求波动'和'商品稀缺度变化'两个混杂因素；若控制后效应量 β 仍显著（p < 0.05），则因果置信度提升；否则需引入工具变量（如平台算法推送时间戳）进行识别。

## Corrected Claim

因果推断的混杂变量控制：需排除'季节性需求波动'和'商品稀缺度变化'两个混杂因素；若控制后效应量 β 仍显著（p < 0.05），则因果置信度提升；否则需引入工具变量（如平台算法推送时间戳）进行识别。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中提到的两个具体混杂因素（季节性、稀缺度）以及备选识别策略（工具变量），三者逻辑独立且互斥，共同构成了完整的因果推断控制方案，无重复或矛盾。）

## Search Query

instrumental variable causal inference pricing strategy second-hand market
