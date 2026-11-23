# N50: 边缘缓存命中延迟 t_cache 的构成：t_cache = t_network_edge + t_processing，其中 t_network_edge 为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

边缘缓存命中延迟 t_cache 的构成：t_cache = t_network_edge + t_processing，其中 t_network_edge 为用户到最近边缘节点的RTT（取决于地理分布，通常 10-50ms），t_processing 为边缘节点内部处理与IO延迟（通常 1-5ms），需根据具体POP点位置与硬件配置确定。

## Corrected Claim

边缘缓存命中延迟 t_cache 的构成：t_cache = t_network_edge + t_processing，其中 t_network_edge 为用户到最近边缘节点的RTT（取决于地理分布，通常 10-50ms），t_processing 为边缘节点内部处理与IO延迟（通常 1-5ms），需根据具体POP点位置与硬件配置确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge cache hit latency components RTT processing time
