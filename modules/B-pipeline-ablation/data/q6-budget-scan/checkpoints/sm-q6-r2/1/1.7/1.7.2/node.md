# N51: 回源链路延迟 t_origin 的构成：t_origin = t_backbone + t_server + t_network_origin，其中 t_bac

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

回源链路延迟 t_origin 的构成：t_origin = t_backbone + t_server + t_network_origin，其中 t_backbone 为骨干网传输延迟（20-50ms），t_server 为源站处理延迟（<10ms），t_network_origin 为源站到边缘节点的网络延迟（通常 5-20ms），需根据源站位置与网络拓扑确定。

## Corrected Claim

回源链路延迟 t_origin 的构成：t_origin = t_backbone + t_server + t_network_origin，其中 t_backbone 为骨干网传输延迟（20-50ms），t_server 为源站处理延迟（<10ms），t_network_origin 为源站到边缘节点的网络延迟（通常 5-20ms），需根据源站位置与网络拓扑确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN origin fetch latency breakdown backbone server processing
