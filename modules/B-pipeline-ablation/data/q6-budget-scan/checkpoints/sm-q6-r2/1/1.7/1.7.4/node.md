# N39: 回源RTT = 边缘节点到源站的物理距离 d_origin / 2.0e8 * 2 * 1.05 + 网络排队延迟；源站部署在核心机房时，边缘节点到源站距离通常

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

回源RTT = 边缘节点到源站的物理距离 d_origin / 2.0e8 * 2 * 1.05 + 网络排队延迟；源站部署在核心机房时，边缘节点到源站距离通常为 200-500km，回源RTT约为 2-5ms 加上排队延迟。

## Corrected Claim

回源RTT = 边缘节点到源站的物理距离 d_origin / 2.0e8 * 2 * 1.05 + 网络排队延迟；源站部署在核心机房时，边缘节点到源站距离通常为 200-500km，回源RTT约为 2-5ms 加上排队延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：光速约3e8 m/s，200-500km距离对应单程1-1.7ms，往返2-3.4ms，加上1.05系数及排队延迟，2-5ms量级合理。

## Search Query

origin server RTT from edge node China data center
