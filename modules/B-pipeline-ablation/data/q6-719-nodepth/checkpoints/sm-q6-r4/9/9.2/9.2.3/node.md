# N563: 联通-移动跨网 RTT 的 P99 值：联通用户访问移动边缘节点的跨省 P99 RTT 典型值为 38-58ms，比同网联通跨省 RTT 高 12-28ms，联

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N184

## Claim

联通-移动跨网 RTT 的 P99 值：联通用户访问移动边缘节点的跨省 P99 RTT 典型值为 38-58ms，比同网联通跨省 RTT 高 12-28ms，联通与移动之间的 Peering 带宽相对较小，导致高负载时 P99 延迟显著上升，Jitter 增加 8-18ms。

## Corrected Claim

联通-移动跨网 RTT 的 P99 值通常高于同网跨省 RTT，且因 Peering 带宽限制，高负载时 P99 延迟和 Jitter 会显著上升，具体数值随网络状况波动。

## Evidence

[质询]具体数值（38-58ms, 12-28ms, 8-18ms）缺乏公开权威数据支持，属于特定网络环境下的经验观测值，不同时期、不同省份及运营商策略调整会导致显著波动，难以作为通用典型值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

China Unicom to China Mobile cross-network P99 RTT peering bandwidth congestion latency 2023
