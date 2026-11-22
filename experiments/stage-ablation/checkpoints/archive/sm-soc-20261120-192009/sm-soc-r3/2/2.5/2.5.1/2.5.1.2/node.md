# N191: Recency 项对曝光权重的贡献：需计算 d(w_alg)/d(Recency) 的弹性，若弹性 > 0.5 则新上架商品获得显著曝光加成，导致卖家策略收敛于

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

Recency 项对曝光权重的贡献：需计算 d(w_alg)/d(Recency) 的弹性，若弹性 > 0.5 则新上架商品获得显著曝光加成，导致卖家策略收敛于快速上架高挂价商品。

## Corrected Claim

Recency 项通常会对新上架商品产生正向的曝光权重贡献，但具体的弹性阈值（如 > 0.5）及其导致的卖家策略收敛效应需依赖特定平台的实证数据或模型参数，通用定义无法证实该具体数值结论。

## Evidence

[质询]该陈述包含具体的量化阈值（弹性 > 0.5）和特定的市场行为结论（卖家策略收敛于快速上架高挂价商品），这属于特定平台或模型下的经验性结论，无法从通用的“Recency bias”定义中推导出来，且参考来源仅定义了认知偏差，未涉及任何算法权重弹性或卖家策略的具体数值。 | 参考来源[1]仅定义了Recency bias为一种认知偏差，与陈述中具体的算法弹性阈值（0.5）及卖家策略收敛结论无关，属于经验事实且缺乏直接来源支持。

## Search Query

e-commerce algorithm exposure weight recency impact on new listings

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Recency_bias&rut=061c2112459b91c51e97bc106146b174dc742864da8f0d1771fecfef9a14a07e', 'type': 'ddg', 'title': 'Recency bias - Wikipedia'}
