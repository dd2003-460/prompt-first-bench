# N190: 缓存有效工作集大小 W_set = N_unique_active_objects，其值由用户请求分布的 Zipf 参数 α 决定，α 越大热点越集中，所需缓存

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

缓存有效工作集大小 W_set = N_unique_active_objects，其值由用户请求分布的 Zipf 参数 α 决定，α 越大热点越集中，所需缓存容量越小 [待核验]

## Corrected Claim

缓存有效工作集大小 W_set 受用户请求分布的 Zipf 参数 α 影响，α 越大热点越集中，达到相同命中率所需的缓存容量越小；W_set 通常小于或等于唯一活跃对象数 N_unique_active_objects。

## Evidence

[质询]该陈述将缓存有效工作集大小直接等同于唯一活跃对象数（W_set = N_unique_active_objects），这在逻辑上是不严谨的。在缓存理论中，'有效工作集'通常指为了达到特定命中率（如90%）所需的缓存容量，其数值取决于访问频率分布（Zipf参数α）和总对象数，而非简单的唯一对象计数。唯一活跃对象数是工作集的上界，而非其定义值。此外，虽然α越大热点越集中、所需缓存容量越小的定性结论是正确的，但将W_set直接定义为N_unique_active_objects混淆了'工作集大小'与'活跃对象总数'的概念。 | 参考来源[1]讨论的是Linux内存管理中的workingset概念，与缓存系统中的Zipf分布及工作集大小定义无关，无法提供外部支持。逻辑上，W_set不应直接等于N_unique_active_objects，而是受α影响的函数值。

## Search Query

CDN cache hit rate zipf distribution parameter alpha

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/10798919273&rut=685c5bbb666144692b74186357b4681bf2c34f7018257eb2b92d24c964c97812', 'type': 'ddg', 'title': 'Linux memory workingset 内存工作集 - 知乎'}
