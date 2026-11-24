# N47: 核心区域自建POP点的P99延迟具体构成：P99_core = RTT_core + T_processing + T_queueing。假设核心区域（一二线）

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

核心区域自建POP点的P99延迟具体构成：P99_core = RTT_core + T_processing + T_queueing。假设核心区域（一二线）平均RTT为20ms，P99 RTT为50ms；T_processing（服务器处理+缓存命中）为10ms；T_queueing（排队延迟，取决于负载率U）在U=50%时约为5ms。因此P99_core ≈ 50 + 10 + 5 = 65ms。若U=70%，T_queueing升至15ms，P99_core ≈ 80ms。

## Corrected Claim

核心区域自建POP点的P99延迟具体构成：P99_core = RTT_core + T_processing + T_queueing。假设核心区域（一二线）平均RTT为20ms，P99 RTT为50ms；T_processing（服务器处理+缓存命中）为10ms；T_queueing（排队延迟，取决于负载率U）在U=50%时约为5ms。因此P99_core ≈ 50 + 10 + 5 = 65ms。若U=70%，T_queueing升至15ms，P99_core ≈ 80ms。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式 P99_core = f(U) 在不同负载率 U 下的离散采样点，存在高度冗余；且未覆盖父节点中明确提到的 U=50% 和 U=70% 两个关键基准场景，导致对父节点具体数值的覆盖不完整。）
