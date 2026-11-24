# N108: POP Miss 时的回源延迟 RTT_pop_origin_p99 (ms)，由 POP 到源站的地理距离 D_pop_origin 决定，RTT_pop_o

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

POP Miss 时的回源延迟 RTT_pop_origin_p99 (ms)，由 POP 到源站的地理距离 D_pop_origin 决定，RTT_pop_origin_p99 = 2 * D_pop_origin / v_fiber + T_transfer_origin，由于 POP 通常位于城市核心，D_pop_origin 可能大于公有云 L2 到源站的距离。

## Corrected Claim

POP Miss 时的回源延迟 RTT_pop_origin_p99 (ms)，由 POP 到源站的地理距离 D_pop_origin 决定，RTT_pop_origin_p99 = 2 * D_pop_origin / v_fiber + T_transfer_origin，由于 POP 通常位于城市核心，D_pop_origin 可能大于公有云 L2 到源站的距离。

## Evidence

先验知识/题面给定，逻辑校验通过：RTT公式符合物理直觉（光速传播+传输时间），POP位于城市核心导致回源距离可能大于边缘L2节点至源站距离的陈述符合CDN网络拓扑常识。

## Search Query

CDN origin pull latency distance calculation
