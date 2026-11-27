# N112: 在 M/C = 0.9 的工作点下，LRU 和 LFU 的字节命中率差异 ΔH 约为 0.5-1.5 个百分点，主要源于 LFU 对头部高频小对象的保留优势。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

在 M/C = 0.9 的工作点下，LRU 和 LFU 的字节命中率差异 ΔH 约为 0.5-1.5 个百分点，主要源于 LFU 对头部高频小对象的保留优势。

## Corrected Claim

在 M/C = 0.9 的工作点下，LFU 通常因对头部高频小对象的保留优势而表现出略高于 LRU 的字节命中率，但具体差异幅度需依赖特定负载实验数据，当前缺乏直接来源支持确切数值范围。

## Evidence

[质询]参考来源与缓存算法（LRU/LFU）及字节命中率完全无关，属于典型的检索结果不匹配；且具体数值范围（0.5-1.5个百分点）属于经验事实，缺乏直接来源支持。 | 逻辑上LFU在头部高频对象保留上优于LRU是成立的，但提供的三个来源（Minecraft版本、医学指标）均与该事实主题无关，无可用外部证据支持具体数值。

## Search Query

LRU vs LFU hit rate difference Pareto distribution alpha 1.1 beta 0.9 M/C 0.9

## Retrieval Sources

- {'url': 'https://minecraft.wiki/w/Pocket_Edition_alpha_1.1.0.9&rut=16ae8171ea6b7e5612f41617aa56b622f1e0c30167703b1b7398ce8441aedaf6', 'type': 'ddg', 'title': 'Pocket Edition alpha 1.1.0.9 - Minecraft Wiki'}
- {'url': 'https://healthmatters.io/understand-blood-test-results/albumin-globulin-ratio&rut=60ddf12d397f8198488b07cdf679c04664a1fda5785ebb6de82947fa9a3c1994', 'type': 'ddg', 'title': 'A/G Ratio High or Low: Albumin/Globulin Ratio Results Explained'}
- {'url': 'https://minecraft.wiki/w/Java_Edition_Alpha_v1.1.0&rut=ba9a4751ae1f7f516d3bbd18d33ad5346a083d2a62dac09764149d4511519974', 'type': 'ddg', 'title': 'Java Edition Alpha v1.1.0 - Minecraft Wiki'}
