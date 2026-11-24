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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数下的三个具体实例（工作点），而非对父节点概念（长尾延迟）的结构性分解（如网络层、缓存层、计算层）。这导致严重的冗余（同一公式重复出现三次），且未覆盖公式中各组成部分的独立分析逻辑，仅覆盖了特定的参数组合，缺乏对一般性影响因素的完备性覆盖。）
