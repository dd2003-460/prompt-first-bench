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

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义地理距离参数，节点2基于距离推导传播延迟（RTT），节点3定义传输延迟（T_transfer），节点4进行加权综合。各部分分别对应公式 RTT = Propagation + Transfer 的不同组成部分及最终统计结果，无重复或矛盾。）

## Search Query

CDN origin pull latency distance calculation
