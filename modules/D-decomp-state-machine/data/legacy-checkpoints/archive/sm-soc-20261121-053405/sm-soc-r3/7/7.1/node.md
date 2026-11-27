# N86: 需求函数 $Q_{demand}(P)$ 在二手非标品市场的实证斜率 $rac{\partial Q}{\partial P}$ 约为 -0.8 至 -1.2

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26, N27, N28

## Claim

需求函数 $Q_{demand}(P)$ 在二手非标品市场的实证斜率 $rac{\partial Q}{\partial P}$ 约为 -0.8 至 -1.2（基于闲鱼/ eBay 历史成交数据回归），用于确定低价段枯竭的具体价格阈值。

## Corrected Claim

二手非标品市场的需求价格弹性因品类和商品状态而异，通常表现为负值，但具体斜率需针对特定数据集进行回归分析，不存在通用的-0.8至-1.2固定区间。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上正交且覆盖了父节点定义的斜率范围（-0.8至-1.2）及延伸区间，但本质上是将单一连续参数（需求弹性/斜率）在不同价格区间的取值离散化为三个工作点。这种结构属于典型的‘参数分段’，而非独立的结构性维度，因此存在结构冗余。）

## Search Query

second hand marketplace demand elasticity slope regression price sensitivity
