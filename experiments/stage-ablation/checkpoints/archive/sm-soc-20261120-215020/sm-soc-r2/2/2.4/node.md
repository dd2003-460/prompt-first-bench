# N13: 均衡稳定性判据：当前均衡为‘古诺-纳什’混合均衡，若单一卖家降价，其收益变化 $\Delta \Pi_{seller} < 0$（因价格降幅 > 销量增量带来的

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

均衡稳定性判据：当前均衡为‘古诺-纳什’混合均衡，若单一卖家降价，其收益变化 $\Delta \Pi_{seller} < 0$（因价格降幅 > 销量增量带来的边际收益），故无个体偏离激励。平台若改变推荐算法（打破信号机制），则 $\Pr(Sale | P_{high})$ 下降，均衡崩塌。

## Corrected Claim

均衡稳定性判据：当前均衡为‘古诺-纳什’混合均衡，若单一卖家降价，其收益变化 $\Delta \Pi_{seller} < 0$（因价格降幅 > 销量增量带来的边际收益），故无个体偏离激励。平台若改变推荐算法（打破信号机制），则 $\Pr(Sale | P_{high})$ 下降，均衡崩塌。

## Evidence

先验知识/题面给定，逻辑校验通过：古诺-纳什均衡的定义即包含无单方偏离激励（ΔΠ<0），且信号机制破坏导致概率下降进而均衡崩塌符合博弈论基本逻辑。

## Search Query

Nash equilibrium stability deviation incentive seller price cut marketplace
