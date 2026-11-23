# N87: 自建节点在缓存未命中场景下的 P99 延迟构成 = 用户到节点 RTT + 节点到源站 RTT + 源站处理时间 + 回源传输时间；对于 500km 距离，若回

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

自建节点在缓存未命中场景下的 P99 延迟构成 = 用户到节点 RTT + 节点到源站 RTT + 源站处理时间 + 回源传输时间；对于 500km 距离，若回源带宽受限，传输时间 T_transfer = s_avg / Bandwidth_backhaul，需计入总延迟。

## Corrected Claim

自建节点在缓存未命中场景下的 P99 延迟构成 = 用户到节点 RTT + 节点到源站 RTT + 源站处理时间 + 回源传输时间；对于 500km 距离，若回源带宽受限，传输时间 T_transfer = s_avg / Bandwidth_backhaul，需计入总延迟。

## Evidence

先验知识/题面给定，逻辑校验通过
