# N123: L2 中间层节点到源站的 RTT_L2_origin P99，通常为 10-30ms，取决于 L2 节点与源站的地理距离及跨网延迟（如电信/联通/移动）。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

L2 中间层节点到源站的 RTT_L2_origin P99，通常为 10-30ms，取决于 L2 节点与源站的地理距离及跨网延迟（如电信/联通/移动）。

## Corrected Claim

L2 中间层节点到源站的 RTT_L2_origin P99，通常为 10-30ms，取决于 L2 节点与源站的地理距离及跨网延迟（如电信/联通/移动）。

## Evidence

父节点级核验通过：正交+完备+无冗余（两个子节点分别量化了RTT的两个主要构成部分：基础物理传输延迟（由距离决定）和跨网惩罚延迟（由运营商差异决定）。两者在逻辑上是正交的加和项，共同覆盖了父节点中提到的'地理距离'和'跨网延迟'两个关键方面，且没有内容重叠或矛盾。）

## Search Query

CDN L2 node to origin server RTT latency
