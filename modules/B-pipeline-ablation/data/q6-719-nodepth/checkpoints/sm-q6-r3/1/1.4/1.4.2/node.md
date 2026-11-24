# N61: 长尾区域（公有云CDN）的P99延迟 P99_tail = RTT_user_edge_tail_p99 + T_proc_edge + (1 - H_l1) 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

长尾区域（公有云CDN）的P99延迟 P99_tail = RTT_user_edge_tail_p99 + T_proc_edge + (1 - H_l1) * (RTT_edge_l2 + (1 - H_l2) * (RTT_l2_origin + T_transfer_origin))，其中H_l1和H_l2分别为L1和L2缓存命中率。

## Corrected Claim

长尾区域（公有云CDN）的P99延迟 P99_tail = RTT_user_edge_tail_p99 + T_proc_edge + (1 - H_l1) * (RTT_edge_l2 + (1 - H_l2) * (RTT_l2_origin + T_transfer_origin))，其中H_l1和H_l2分别为L1和L2缓存命中率。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一公式在不同参数组合下的三个采样点（工作点），而非对公式中不同物理机制或组件的独立分解。它们存在严重的参数冗余（本质是同一个多维参数空间的离散取值），且仅覆盖了特定的性能-成本权衡点，未覆盖公式中所有变量的独立影响或边界情况，因此不完备。）
