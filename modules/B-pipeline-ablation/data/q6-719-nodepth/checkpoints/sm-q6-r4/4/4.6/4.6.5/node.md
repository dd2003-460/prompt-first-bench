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

父节点级核验通过：正交+完备+无冗余（子节点分别对应物理距离、光纤传输延迟计算、排队延迟估计，三者分别描述了RTT的组成因素（传播距离、传播延迟、排队延迟），彼此正交且共同覆盖了父节点中提到的地理距离和网络拥塞两个关键方面。没有明显的冗余或矛盾。）

## Search Query

CDN L1 to L2 node RTT latency backbone network
