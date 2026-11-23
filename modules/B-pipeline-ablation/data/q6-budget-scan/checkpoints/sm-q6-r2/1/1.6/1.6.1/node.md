# N47: 骨干网延迟 t_backbone = t_hop * N_hops，其中 t_hop 为单跳延迟（典型 5-10ms），N_hops 为从边缘节点到源站的路由跳

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

骨干网延迟 t_backbone = t_hop * N_hops，其中 t_hop 为单跳延迟（典型 5-10ms），N_hops 为从边缘节点到源站的路由跳数（典型 3-10跳）；该值反映数据在运营商骨干网中的传输耗时。

## Corrected Claim

骨干网延迟 t_backbone = t_hop * N_hops，其中 t_hop 为单跳延迟（典型 5-10ms），N_hops 为从边缘节点到源站的路由跳数（典型 3-10跳）；该值反映数据在运营商骨干网中的传输耗时。

## Evidence

先验知识/题面给定，逻辑校验通过：骨干网延迟由单跳延迟乘以跳数构成，典型数值范围（5-10ms/跳，3-10跳）符合网络工程常识，量纲与量级合理。

## Search Query

internet backbone latency per hop ms
