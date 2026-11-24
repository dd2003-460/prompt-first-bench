# N129: 自建 POP 回源数据传输时间 T_transfer_origin_self，基于对象大小 s 和 POP 到源站的带宽 B_pop_origin，计算公式为 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

自建 POP 回源数据传输时间 T_transfer_origin_self，基于对象大小 s 和 POP 到源站的带宽 B_pop_origin，计算公式为 T_transfer_origin_self = s / B_pop_origin，P99 值受 POP 出口带宽限制。

## Corrected Claim

自建 POP 回源数据传输时间 T_transfer_origin_self，基于对象大小 s 和 POP 到源站的带宽 B_pop_origin，计算公式为 T_transfer_origin_self = s / B_pop_origin，P99 值受 POP 出口带宽限制。

## Evidence

父节点级核验未通过：不完备（子节点之间正交（分别关注带宽规格、传输时间计算、队列延迟）；但完备性不足，父节点明确提到“P99 值受 POP 出口带宽限制”，而子节点仅讨论了 POP 到源站的链路带宽和队列，完全遗漏了 POP 自身出口带宽（B_pop_egress）对整体 T_transfer 或 P99 的影响，导致关键约束缺失。）

## Search Query

self-built POP origin pull transfer time calculation
