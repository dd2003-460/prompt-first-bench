# N36: 投影1（曝光量）：高溢价商品的预期曝光量 E[Imp] = Base_Imp * (1 + α * δ) * (1 + ε_rank)，其中 α 为平台对高溢价

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N8

## Claim

投影1（曝光量）：高溢价商品的预期曝光量 E[Imp] = Base_Imp * (1 + α * δ) * (1 + ε_rank)，其中 α 为平台对高溢价商品的加权系数，需通过 A/B 测试数据估计 α ∈ [0.1, 0.3] 以量化曝光提升幅度。

## Corrected Claim

投影1（曝光量）：高溢价商品的预期曝光量 E[Imp] 通常建模为 Base_Imp 乘以加权因子，其中加权系数 α 需通过 A/B 测试数据估计以量化曝光提升幅度（具体数值范围需依据特定平台实验数据确定）。

## Evidence

[质询]该陈述包含具体的经验性参数范围（α ∈ [0.1, 0.3]）和特定的数学模型结构，属于平台内部算法或特定实验得出的经验事实，无法从第一性原理推导，且参考来源未提供该具体数值范围或公式支持。 | 逻辑自洽，但参考来源[1][2]仅定义曝光量指标，未涉及高溢价加权系数α的具体数值范围或公式，属于经验事实且缺来源直接支持。

## Search Query

marketplace platform algorithm exposure bias high price items A/B test alpha coefficient

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/671339454&rut=ef26bc3f247e911f2a713e8a5e82a4d1a182543858a05eeb99441c4ed312c73d', 'type': 'ddg', 'title': '亚马逊广告重要数据指标及基本含义介绍 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/631049403&rut=009b9984478d23d37414635fd203683a5ca207eee142effc0d90678838c91396', 'type': 'ddg', 'title': '亚马逊广告结果指标详解 - 知乎专栏'}
