# N182: 公有云CDN回源延迟 T_origin_cloud：公有云CDN的回源通常通过内网或专用骨干网，延迟较低，平均回源RTT为20-40ms，P99回源延迟为40-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56, N57, N58

## Claim

公有云CDN回源延迟 T_origin_cloud：公有云CDN的回源通常通过内网或专用骨干网，延迟较低，平均回源RTT为20-40ms，P99回源延迟为40-60ms，低于自建节点的回源延迟

## Corrected Claim

公有云CDN回源延迟 T_origin_cloud：公有云CDN的回源通常通过内网或专用骨干网，延迟较低，平均回源RTT为20-40ms，P99回源延迟为40-60ms，低于自建节点的回源延迟

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud CDN origin fetch latency internal network
