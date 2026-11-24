# N118: 用户到最近公有云CDN边缘节点的物理距离 D_user_edge 的 P99 值，基于阿里云/Cloudflare 在中国/全球的节点分布密度（>1000 节点

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

用户到最近公有云CDN边缘节点的物理距离 D_user_edge 的 P99 值，基于阿里云/Cloudflare 在中国/全球的节点分布密度（>1000 节点）及用户地理分布，估算为 50-200km，对应 RTT_user_edge P99 ≈ 5-20ms（光速传播延迟 + 路由开销）。

## Corrected Claim

用户到最近公有云CDN边缘节点的物理距离 D_user_edge 的 P99 值，基于阿里云/Cloudflare 在中国/全球的节点分布密度（>1000 节点）及用户地理分布，估算为 50-200km，对应 RTT_user_edge P99 ≈ 5-20ms（光速传播延迟 + 路由开销）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于>1000个节点覆盖中国/全球的密度，P99距离50-200km符合工程常识；光速延迟约0.17-0.67ms，加上路由、交换及处理开销，5-20ms的RTT估算在量级上合理且自洽。

## Search Query

Alibaba Cloud CDN node distribution China distance RTT
