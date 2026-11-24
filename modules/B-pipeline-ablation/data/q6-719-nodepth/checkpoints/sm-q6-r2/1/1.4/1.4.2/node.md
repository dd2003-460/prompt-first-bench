# N61: 长尾区域（公有云CDN）的P99延迟 P99_tail = RTT_user_edge_tail_p99 + T_proc_edge + (1 - H_l1) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

长尾区域（公有云CDN）的P99延迟 P99_tail = RTT_user_edge_tail_p99 + T_proc_edge + (1 - H_l1) * (RTT_edge_l2 + (1 - H_l2) * (RTT_l2_origin + T_transfer_origin))，其中H_l1和H_l2分别为L1和L2缓存命中率。

## Corrected Claim

长尾区域（公有云CDN）的P99延迟 P99_tail = RTT_user_edge_tail_p99 + T_proc_edge + (1 - H_l1) * (RTT_edge_l2 + (1 - H_l2) * (RTT_l2_origin + T_transfer_origin))，其中H_l1和H_l2分别为L1和L2缓存命中率。

## Evidence

先验知识/题面给定，逻辑校验通过
