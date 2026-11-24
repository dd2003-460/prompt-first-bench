# N418: 并发回源导致的队列延迟 T_queue_origin：当多个请求同时 Miss 且回源到同一源站时，T_queue = (N_concurrent_misses

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N129

## Claim

并发回源导致的队列延迟 T_queue_origin：当多个请求同时 Miss 且回源到同一源站时，T_queue = (N_concurrent_misses - 1) * T_transfer。若 N_concurrent_misses=10, T_transfer=0.12ms，则 T_queue ≈ 1.08ms；若 s_video=15MB, T_transfer=1.2ms, 则 T_queue ≈ 10.8ms，显著增加 P99。

## Corrected Claim

并发回源导致的队列延迟 T_queue_origin：当多个请求同时 Miss 且回源到同一源站时，T_queue = (N_concurrent_misses - 1) * T_transfer。若 N_concurrent_misses=10, T_transfer=0.12ms，则 T_queue ≈ 1.08ms；若 s_video=15MB, T_transfer=1.2ms, 则 T_queue ≈ 10.8ms，显著增加 P99。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_queue = (N-1)*T_transfer 符合串行排队模型，数值计算 9*0.12=1.08 和 9*1.2=10.8 准确无误。
