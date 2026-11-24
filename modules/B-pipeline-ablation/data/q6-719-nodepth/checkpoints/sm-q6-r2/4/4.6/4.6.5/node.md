# N122: L1 边缘节点到 L2 中间层节点的 RTT_edge_L2 P99，基于骨干网延迟，通常为 5-15ms，取决于 L1 和 L2 节点之间的地理距离和网络拥塞

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

L1 边缘节点到 L2 中间层节点的 RTT_edge_L2 P99，基于骨干网延迟，通常为 5-15ms，取决于 L1 和 L2 节点之间的地理距离和网络拥塞情况。

## Corrected Claim

L1 边缘节点到 L2 中间层节点的 RTT_edge_L2 P99，基于骨干网延迟，通常为 5-15ms，取决于 L1 和 L2 节点之间的地理距离和网络拥塞情况。

## Evidence

先验知识/题面给定，逻辑校验通过：骨干网跨地域延迟通常在毫秒级，5-15ms符合L1到L2（通常涉及跨城或跨大区）的物理延迟量级及网络波动范围。

## Search Query

CDN L1 to L2 node RTT latency backbone network
