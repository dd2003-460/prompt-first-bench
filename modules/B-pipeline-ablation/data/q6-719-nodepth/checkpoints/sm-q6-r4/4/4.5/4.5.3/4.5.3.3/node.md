# N381: 自建 POP 回源总延迟 P99_RTT_self_origin 的组成公式为 P99_RTT_self_origin = RTT_base_origin + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

自建 POP 回源总延迟 P99_RTT_self_origin 的组成公式为 P99_RTT_self_origin = RTT_base_origin + T_queue_origin + T_transfer_origin，其中 T_transfer_origin 为对象传输时间，若 s_weighted = 5MB 且带宽为 10Gbps，T_transfer_origin ≈ 4ms。

## Corrected Claim

自建 POP 回源总延迟 P99_RTT_self_origin 的组成公式为 P99_RTT_self_origin = RTT_base_origin + T_queue_origin + T_transfer_origin，其中 T_transfer_origin 为对象传输时间，若 s_weighted = 5MB 且带宽为 10Gbps，T_transfer_origin ≈ 4ms。

## Evidence

先验知识/题面给定，逻辑校验通过：5MB * 8 / 10Gbps = 4ms，计算正确且量级合理
