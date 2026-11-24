# N172: 混合策略长尾部分（公有云CDN）P99延迟构成：Latency_tail_cloud = RTT_user_edge + Edge_Processing + R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

混合策略长尾部分（公有云CDN）P99延迟构成：Latency_tail_cloud = RTT_user_edge + Edge_Processing + RTT_edge_origin (if miss) + Origin_Processing。公有云CDN边缘节点分布密集，RTT_user_edge通常<20ms；若命中率95%，5%请求回源，回源RTT取决于边缘节点与源站距离，通常50-100ms。

## Corrected Claim

混合策略长尾部分（公有云CDN）P99延迟构成：Latency_tail_cloud = RTT_user_edge + Edge_Processing + RTT_edge_origin (if miss) + Origin_Processing。公有云CDN边缘节点分布密集，RTT_user_edge通常<20ms；若命中率95%，5%请求回源，回源RTT取决于边缘节点与源站距离，通常50-100ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Cloudflare CDN P99 latency breakdown edge to origin
