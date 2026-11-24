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

父节点级核验通过：正交+完备+无冗余（子节点分别对应距离参数、基于距离的RTT计算、传输延迟分量以及加权后的整体P99估算，逻辑链条清晰（参数->推导->分量->综合），各节点关注点不同（物理距离、传播延迟、传输延迟、统计加权），无重复或矛盾。）

## Search Query

CDN origin pull latency distance calculation
