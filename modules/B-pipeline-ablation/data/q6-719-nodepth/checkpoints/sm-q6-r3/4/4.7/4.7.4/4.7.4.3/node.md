# N414: 多源站负载均衡场景下，若源站集群带宽 B_origin_cluster = N_origin * B_origin_single，且请求均匀分布，则单链路负载降

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

多源站负载均衡场景下，若源站集群带宽 B_origin_cluster = N_origin * B_origin_single，且请求均匀分布，则单链路负载降低 N_origin 倍，Queueing_Delay 趋近于 0，此时 RTT_pop_origin P99 主要受限于地理 RTT_base（20-50ms）及跨网惩罚 ΔT_cross（15-25ms），总 P99 约为 35-75ms。

## Corrected Claim

多源站负载均衡场景下，若源站集群带宽 B_origin_cluster = N_origin * B_origin_single，且请求均匀分布，则单链路负载降低 N_origin 倍，Queueing_Delay 趋近于 0，此时 RTT_pop_origin P99 主要受限于地理 RTT_base（20-50ms）及跨网惩罚 ΔT_cross（15-25ms），总 P99 约为 35-75ms。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽线性扩展消除排队延迟符合排队论基本直觉，P99延迟由固定地理RTT与跨网惩罚叠加构成，数值量级（20-50ms + 15-25ms = 35-75ms）符合网络工程常识。
