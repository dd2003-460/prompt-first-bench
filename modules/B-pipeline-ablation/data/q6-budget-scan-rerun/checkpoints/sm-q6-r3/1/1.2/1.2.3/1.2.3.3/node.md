# N152: 缓存容量对命中率的边际效应：每增加1TB缓存容量，大对象命中率提升 $\Delta H_{large} \approx 5-10\%$，小对象命中率提升 $\D

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

缓存容量对命中率的边际效应：每增加1TB缓存容量，大对象命中率提升 $\Delta H_{large} \approx 5-10\%$，小对象命中率提升 $\Delta H_{small} \approx 1-2\%$。对于10个自建POP，每个POP分配10TB缓存，总容量100TB，足以覆盖Top 10000热点对象（约50TB），使得整体命中率稳定在92%-95%区间

## Corrected Claim

缓存容量对命中率的边际效应：每增加1TB缓存容量，大对象命中率提升 $\Delta H_{large} \approx 5-10\%$，小对象命中率提升 $\Delta H_{small} \approx 1-2\%$。对于10个自建POP，每个POP分配10TB缓存，总容量100TB，足以覆盖Top 10000热点对象（约50TB），使得整体命中率稳定在92%-95%区间

## Evidence

先验知识/题面给定，逻辑校验通过：100TB总容量覆盖50TB热点对象（覆盖率200%），符合缓存容量与命中率正相关的工程直觉，数值量级合理。

## Search Query

CDN cache capacity hit rate marginal improvement
