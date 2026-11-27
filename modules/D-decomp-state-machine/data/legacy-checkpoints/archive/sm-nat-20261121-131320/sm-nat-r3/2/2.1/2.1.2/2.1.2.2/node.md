# N90: LRU 字节命中率 H_LRU 的数值积分结果：H_LRU = ∫_{x_min}^{S_evict} f(s) * s ds / Total_Bytes；代入

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

LRU 字节命中率 H_LRU 的数值积分结果：H_LRU = ∫_{x_min}^{S_evict} f(s) * s ds / Total_Bytes；代入 S_evict 和联合分布参数，计算积分值，该值即为 LRU 策略下的稳态字节命中率下界（未考虑更新衰减）。

## Corrected Claim

在特定联合分布f(s)和驱逐阈值S_evict下，通过积分∫_{x_min}^{S_evict} f(s) * s ds / Total_Bytes计算出的值，可作为未考虑更新衰减的LRU策略稳态字节命中率的近似下界。

## Evidence

[质询]该陈述将特定的数值积分公式直接等同于LRU策略下的稳态字节命中率下界，缺乏对联合分布f(s)具体形式及S_evict定义的严格推导支持，且未考虑更新衰减仅能作为简化模型的下界，直接断言其为通用下界存在逻辑跳跃。 | 参考来源[1]仅提及LRU算法名称，未提供命中率积分公式或数值结果，属于无关来源；该事实为经验性/模型推导结果，逻辑自洽但缺乏直接来源支持。

## Search Query

LRU byte hit rate calculation Pareto distribution cache simulation

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_algorithms', 'type': 'wikipedia', 'title': 'List of algorithms'}
