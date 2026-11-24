# N30: 公有云CDN的P99延迟构成项包括：用户到边缘RTT (RTT_user_edge) + 边缘处理时间 (T_proc_edge) + 回源延迟 (若Miss:

- **status**: pending
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

父节点级核验未通过：不完备（子节点之间正交性良好，分别覆盖了距离、处理、缓存命中、多级RTT和传输等独立维度。但完备性不足：父节点公式中明确列出的回源延迟项为 'RTT_edge_origin'，而子节点将其拆解为 'L1->L2 RTT' 和 'L2->Origin RTT'，缺失了 L2 节点自身的处理时间 (T_proc_L2) 以及 L1->L2 之间的数据传输/排队时间（若适用），导致分解后的各项之和无法严格还原父节点定义的 P99 延迟构成。）
