# N30: 公有云CDN的P99延迟构成项包括：用户到边缘RTT (RTT_user_edge) + 边缘处理时间 (T_proc_edge) + 回源延迟 (若Miss:

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

公有云CDN的P99延迟构成项包括：用户到边缘RTT (RTT_user_edge) + 边缘处理时间 (T_proc_edge) + 回源延迟 (若Miss: RTT_edge_origin + T_transfer_origin)，其中RTT_user_edge的P99值由地理分布决定。

## Corrected Claim

公有云CDN的P99延迟构成项包括：用户到边缘RTT (RTT_user_edge) + 边缘处理时间 (T_proc_edge) + 回源延迟 (若Miss: RTT_edge_origin + T_transfer_origin)，其中RTT_user_edge的P99值由地理分布决定。

## Evidence

先验知识/题面给定，逻辑校验通过：CDN延迟构成符合网络通信基本模型，P99延迟受地理分布影响的RTT主导符合物理直觉。
