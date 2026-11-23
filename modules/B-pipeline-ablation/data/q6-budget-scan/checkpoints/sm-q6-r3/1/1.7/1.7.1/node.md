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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的两个独立分量（t_network_edge 和 t_processing），内容互不重叠且无矛盾，覆盖了父节点定义的所有关键方面，且各自代表了不同的物理/硬件维度，不存在冗余。）

## Search Query

CDN edge cache hit latency components RTT processing time
