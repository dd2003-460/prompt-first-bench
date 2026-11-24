# N114: L1 到 L2 的回源延迟 RTT_L1_L2 通常为 5-20ms（取决于 L1 与 L2 节点间的地理距离和网络质量），L2 到源站的回源延迟 RTT_L2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

L1 到 L2 的回源延迟 RTT_L1_L2 通常为 5-20ms（取决于 L1 与 L2 节点间的地理距离和网络质量），L2 到源站的回源延迟 RTT_L2_origin 通常为 20-50ms，总回源延迟 RTT_origin_total = RTT_L1_L2 + RTT_L2_origin + T_transfer_origin，其中 T_transfer_origin 取决于对象大小 s 和源站带宽。

## Corrected Claim

L1 到 L2 的回源延迟 RTT_L1_L2 通常为 5-20ms（取决于 L1 与 L2 节点间的地理距离和网络质量），L2 到源站的回源延迟 RTT_L2_origin 通常为 20-50ms，总回源延迟 RTT_origin_total = RTT_L1_L2 + RTT_L2_origin + T_transfer_origin，其中 T_transfer_origin 取决于对象大小 s 和源站带宽。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN L1 L2 origin server latency breakdown
