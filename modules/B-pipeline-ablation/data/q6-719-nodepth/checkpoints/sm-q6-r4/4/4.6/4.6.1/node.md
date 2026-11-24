# N118: 用户到最近公有云CDN边缘节点的物理距离 D_user_edge 的 P99 值，基于阿里云/Cloudflare 在中国/全球的节点分布密度（>1000 节点

- **status**: pending
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

父节点级核验未通过：不完备（子节点分别处理了物理距离和RTT计算，逻辑上正交且不重复。但是，父节点明确提到“基于...节点分布密度...估算”，而子节点仅给出了结果值（如50-100km），并未分解出“节点密度”与“用户地理分布”如何具体推导出这些距离的中间逻辑或约束条件（例如：为什么密度高就导致距离短？是否忽略了网络拓扑对物理距离映射的影响？）。此外，父节点提到的“全球”在子节点中仅被简化为中国大陆的细分，未覆盖全球场景，导致完备性不足。）

## Search Query

Alibaba Cloud CDN node distribution China distance RTT
