# N36: 溢价率分布 [15%, 25%] 的右偏长尾特征意味着存在约10%的极端高溢价（>50%）长尾商品，这些商品虽然成交周期短但拉高了整体均价，需计算偏度系数 Sk

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

溢价率分布 [15%, 25%] 的右偏长尾特征意味着存在约10%的极端高溢价（>50%）长尾商品，这些商品虽然成交周期短但拉高了整体均价，需计算偏度系数 Skewness > 1 来确认分布形态。

## Corrected Claim

溢价率分布 [15%, 25%] 的右偏长尾特征意味着存在高溢价（>50%）长尾商品，这些商品虽然成交周期短但拉高了整体均价，需计算偏度系数 Skewness > 1 来确认分布形态，具体长尾占比需结合完整分布数据估算。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点基于市场分层（头部/中部/尾部）和样本量/统计特征进行划分，逻辑上互斥且覆盖了父节点提到的分布形态、极端值占比及成交周期影响，不存在重复或矛盾。）

## Search Query

price premium distribution skewness long tail second hand market
