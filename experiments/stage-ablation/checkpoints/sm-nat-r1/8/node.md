# N24: 对象更新率 U=1%/天 导致的 LRU 有效命中率衰减因子 D 可通过动态模型计算：D = 1 - U * T_residence * P_miss_upda

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 U=1%/天 导致的 LRU 有效命中率衰减因子 D 可通过动态模型计算：D = 1 - U * T_residence * P_miss_update。其中 T_residence 为对象平均驻留时间，可由 LRU 驱逐率推导：T_residence ≈ C / (Miss_Rate * Request_Rate * Avg_Size)。在稳态下，若 Miss_Rate ≈ 0.2，Request_Rate ≈ 5000万/天，Avg_Size ≈ 11KB，则 T_residence 约为数小时，D ≈ 1 - 0.01 * (T_residence/1day) * 0.85。

## Corrected Claim

对象更新率 U 导致的 LRU 有效命中率衰减因子 D 可通过动态模型计算：D = 1 - U * T_residence * P_miss_update。其中 T_residence 为对象平均驻留时间，可由 LRU 驱逐率推导：T_residence ≈ C / (Miss_Rate * Request_Rate * Avg_Size)。具体数值需根据实际系统参数确定。

## Evidence

[质询]该陈述包含具体的经验数值（Miss_Rate=0.2, Request_Rate=5000万/天, Avg_Size=11KB, P_miss_update=0.85），这些属于特定系统或场景下的经验事实，无法从第一性原理或数学公理中严格推导出来。虽然公式结构在逻辑上自洽，但具体数值缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅介绍缓存替换策略，未提供具体数值模型；来源[2]、[3]无关）

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Cache_replacement_policies', 'type': None, 'title': 'direct-browser: https://en.wikipedia.org/wiki/Cache_replacement_policies'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'http://arxiv.org/abs/1203.2287v4', 'type': 'arxiv', 'title': 'Bounds for rating override rates'}
