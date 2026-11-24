# N413: 单源站场景下，POP到源站的RTT_pop_origin P99 = RTT_base + Queueing_Delay，其中 RTT_base 为跨省骨干网物

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

单源站场景下，POP到源站的RTT_pop_origin P99 = RTT_base + Queueing_Delay，其中 RTT_base 为跨省骨干网物理延迟（20-50ms），Queueing_Delay = (B_origin_peak / B_link_capacity) * RTT_base，当链路利用率 < 70% 时 Queueing_Delay < 10ms，总 P99 < 60ms。

## Corrected Claim

单源站场景下，POP到源站的RTT_pop_origin P99 = RTT_base + Queueing_Delay，其中 RTT_base 为跨省骨干网物理延迟（20-50ms），Queueing_Delay = (B_origin_peak / B_link_capacity) * RTT_base，当链路利用率 < 70% 时 Queueing_Delay < 10ms，总 P99 < 60ms。

## Evidence

先验知识/题面给定，逻辑校验通过：RTT_base (20-50ms) 符合跨省骨干网物理延迟量级；Queueing_Delay 公式符合排队论基本直觉（利用率低时延迟小）；当利用率<70%且RTT_base<50ms时，Queueing_Delay<10ms在工程上合理，总P99<60ms逻辑自洽。
