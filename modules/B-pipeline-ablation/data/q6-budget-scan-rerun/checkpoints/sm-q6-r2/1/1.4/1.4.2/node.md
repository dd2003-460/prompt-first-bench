# N47: 核心区域自建POP点的P99延迟具体构成：P99_core = RTT_core + T_processing + T_queueing。假设核心区域（一二线）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

核心区域自建POP点的P99延迟具体构成：P99_core = RTT_core + T_processing + T_queueing。假设核心区域（一二线）平均RTT为20ms，P99 RTT为50ms；T_processing（服务器处理+缓存命中）为10ms；T_queueing（排队延迟，取决于负载率U）在U=50%时约为5ms。因此P99_core ≈ 50 + 10 + 5 = 65ms。若U=70%，T_queueing升至15ms，P99_core ≈ 80ms。

## Corrected Claim

核心区域自建POP点的P99延迟具体构成：P99_core = RTT_core + T_processing + T_queueing。假设核心区域（一二线）平均RTT为20ms，P99 RTT为50ms；T_processing（服务器处理+缓存命中）为10ms；T_queueing（排队延迟，取决于负载率U）在U=50%时约为5ms。因此P99_core ≈ 50 + 10 + 5 = 65ms。若U=70%，T_queueing升至15ms，P99_core ≈ 80ms。

## Evidence

先验知识/题面给定，逻辑校验通过
