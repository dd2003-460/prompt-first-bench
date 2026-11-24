# N160: 在 T=100ms 约束下，自建策略的合规性验证需计算加权平均 P99 延迟 L_p99_self = Σ p_i * (RTT_pop_i + T_queue

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38, N39, N40

## Claim

在 T=100ms 约束下，自建策略的合规性验证需计算加权平均 P99 延迟 L_p99_self = Σ p_i * (RTT_pop_i + T_queue_i + T_trans_i)，其中 p_i 为各区域流量占比，RTT_pop_i 需满足 max(RTT_pop_i) ≤ 50ms 以预留队列和处理时间余量。

## Corrected Claim

在 T=100ms 约束下，自建策略的合规性验证需计算加权平均 P99 延迟 L_p99_self = Σ p_i * (RTT_pop_i + T_queue_i + T_trans_i)，其中 p_i 为各区域流量占比，RTT_pop_i 需满足 max(RTT_pop_i) ≤ 50ms 以预留队列和处理时间余量。

## Evidence

先验知识/题面给定，逻辑校验通过
