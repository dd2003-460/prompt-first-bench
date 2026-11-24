# N218: L2 到源站的 RTT P99 为 30ms，基于源站位于北京/上海等一线城市，L2 节点位于区域中心（如广州/成都），跨省 RTT 典型值 20-50ms，取

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

L2 到源站的 RTT P99 为 30ms，基于源站位于北京/上海等一线城市，L2 节点位于区域中心（如广州/成都），跨省 RTT 典型值 20-50ms，取 P99 上界 30ms

## Corrected Claim

L2 到源站的 RTT P99 为 30ms，基于源站位于北京/上海等一线城市，L2 节点位于区域中心（如广州/成都），跨省 RTT 典型值 20-50ms，取 P99 上界 30ms

## Evidence

先验知识/题面给定，逻辑校验通过：北京/上海至广州/成都的跨省光纤传输距离在1500-2000km左右，光速延迟约8-10ms，加上路由跳数、设备处理及网络抖动，P99延迟在20-50ms区间内取30ms作为上界符合网络工程常识与物理直觉。
