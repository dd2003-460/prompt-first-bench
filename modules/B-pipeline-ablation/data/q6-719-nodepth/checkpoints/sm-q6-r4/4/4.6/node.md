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

父节点级核验未通过：不完备（子节点之间定义清晰，分别对应距离/RTT、处理时间、各级缓存命中率、级联RTT及传输时间，无重叠或矛盾（正交性好）。但父节点明确提及“回源延迟”包含“回源数据传输时间”，且通常P99延迟分析需考虑TCP握手或TLS握手的完整开销（若未复用连接），子节点仅列出了“HTTP响应头生成”和“TLS握手开销（若未复用）”，未明确区分TCP SYN-ACK与TLS握手的独立延迟项，且未包含源站处理时间（T_proc_origin）这一常见构成项，导致对“回源延迟”的分解不够完备。）
