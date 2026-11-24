# N267: RTT_total 的P99合成公式：P99_RT_t_total = P99_RT_t_propagation + P99_RT_t_queue + P99_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115, N116, N121

## Claim

RTT_total 的P99合成公式：P99_RT_t_total = P99_RT_t_propagation + P99_RT_t_queue + P99_RT_t_processing。注意：各分量并非独立，网络拥塞会同时增加传播延迟（路径切换）和排队延迟。保守估计：P99_RT_t_total ≈ 1.2 * (P99_RT_t_propagation + P99_RT_t_queue + P99_RT_t_processing)。

## Corrected Claim

RTT_total 的P99合成公式：P99_RT_t_total = P99_RT_t_propagation + P99_RT_t_queue + P99_RT_t_processing。注意：各分量并非独立，网络拥塞会同时增加传播延迟（路径切换）和排队延迟。保守估计：P99_RT_t_total ≈ 1.2 * (P99_RT_t_propagation + P99_RT_t_queue + P99_RT_t_processing)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

P99 latency composition network propagation queue processing correlation
