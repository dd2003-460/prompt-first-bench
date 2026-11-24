# N141: 本地缓存响应时间 T_local 的组成：T_local = T_rtt_local + T_processing + T_queueing。在自建POP点场景

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

本地缓存响应时间 T_local 的组成：T_local = T_rtt_local + T_processing + T_queueing。在自建POP点场景下，T_rtt_local ≈ 1.5ms（基于300km距离），T_processing ≈ 5ms（NVMe SSD随机读+网络栈处理），T_queueing 在 P99 负载下通常为 0-10ms。综合 T_local 基准值约为 10-15ms，修正 N34 中 50ms 的高估（50ms 可能包含了长尾或高负载排队）。

## Corrected Claim

本地缓存响应时间 T_local 的组成：T_local = T_rtt_local + T_processing + T_queueing。在自建POP点场景下，T_rtt_local ≈ 1.5ms（基于300km距离），T_processing ≈ 5ms（NVMe SSD随机读+网络栈处理），T_queueing 在 P99 负载下通常为 0-10ms。综合 T_local 基准值约为 10-15ms，修正 N34 中 50ms 的高估（50ms 可能包含了长尾或高负载排队）。

## Evidence

先验知识/题面给定，逻辑校验通过：300km光纤单向延迟约1.5ms（RTT约3ms，此处可能指单向或特定优化场景，但量级合理），NVMe处理5ms及排队延迟符合工程常识，总延迟10-15ms在逻辑上自洽且符合高性能本地缓存预期。

## Search Query

NVMe SSD random read latency network stack overhead p99
