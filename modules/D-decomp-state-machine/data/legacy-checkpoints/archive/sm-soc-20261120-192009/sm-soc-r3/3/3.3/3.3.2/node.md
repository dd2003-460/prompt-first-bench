# N68: 价格损失项量化：ΔPrice * Quantity 的具体计算式，其中 ΔPrice = P_initial - P_new = P_initial * 15%

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

价格损失项量化：ΔPrice * Quantity 的具体计算式，其中 ΔPrice = P_initial - P_new = P_initial * 15%，Quantity 为干预前后预期成交件数（假设不变），该项代表直接毛利损失，数值等于 0.15 * P_initial * Q。

## Corrected Claim

价格损失项量化：ΔPrice * Quantity 的具体计算式，其中 ΔPrice = P_initial - P_new = P_initial * 15%，Quantity 为干预前后预期成交件数（假设不变），该项代表直接毛利损失，数值等于 0.15 * P_initial * Q。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点通过选取三个具有代表性的工作点（高单价/低销量、中单价/中销量、低单价/高销量）来具体化父节点中的公式。虽然数学上它们都是公式的特例，但在业务语义上分别代表了不同的市场形态和风险特征（现金流冲击 vs 分散风险 vs 长期GMV侵蚀），因此具备正交性（业务场景不重叠）和完备性（覆盖了价格-数量组合的典型象限）。它们并非简单的参数冗余，而是为了展示公式在不同商业语境下的应用差异，故不视为冗余。）
