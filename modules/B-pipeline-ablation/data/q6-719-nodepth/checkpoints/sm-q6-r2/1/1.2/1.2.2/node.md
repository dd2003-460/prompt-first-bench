# N53: 公有云 CDN 用户到边缘节点 RTT 的 P99 估算：基于地理分布，假设 80% 用户距最近节点 <100km（RTT<20ms），20% 用户距 100-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

公有云 CDN 用户到边缘节点 RTT 的 P99 估算：基于地理分布，假设 80% 用户距最近节点 <100km（RTT<20ms），20% 用户距 100-300km（RTT 20-50ms），则 P99(RTT_user_edge) ≈ 50ms（保守估计）。

## Corrected Claim

公有云 CDN 用户到边缘节点 RTT 的 P99 估算：基于地理分布，假设 80% 用户距最近节点 <100km（RTT<20ms），20% 用户距 100-300km（RTT 20-50ms），则 P99(RTT_user_edge) ≈ 50ms（保守估计）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于光速传播延迟（~200km/ms）及光纤折射率修正，100-300km距离对应20-50ms RTT符合物理直觉；P99落在20%尾部区间的上限50ms，估算逻辑自洽且量级合理。

## Search Query

CDN edge node geographic distribution RTT P99 latency estimate 50ms
