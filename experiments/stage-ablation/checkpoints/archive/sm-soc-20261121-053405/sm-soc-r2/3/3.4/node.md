# N17: 平台伤害量化：干预后平台GMV或佣金收入变化 $\Delta Rev_{platform} = \text{Commission} \times (GMV_{n

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N3

## Claim

平台伤害量化：干预后平台GMV或佣金收入变化 $\Delta Rev_{platform} = \text{Commission} \times (GMV_{new} - GMV_{old})$。若干预导致短期GMV下降，$\Delta Rev_{platform} < 0$，但长期可能因信任提升而增加，需计算净现值 $NPV = \sum \frac{\Delta Rev_t}{(1+r)^t}$。

## Corrected Claim

平台伤害量化：干预后平台GMV或佣金收入变化 $\Delta Rev_{platform} = \text{Commission} \times (GMV_{new} - GMV_{old})$。若干预导致短期GMV下降，$\Delta Rev_{platform} < 0$，但长期可能因信任提升而增加，需计算净现值 $NPV = \sum \frac{\Delta Rev_t}{(1+r)^t}$。

## Evidence

先验知识/题面给定，逻辑校验通过
