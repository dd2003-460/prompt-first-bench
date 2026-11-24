# N313: 事件期间 P99 延迟增量 ΔL_p99_event 的阈值效应：当 ΔK_event 导致边缘节点负载率 L_load > 80% 时，队列延迟呈非线性增长，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N102

## Claim

事件期间 P99 延迟增量 ΔL_p99_event 的阈值效应：当 ΔK_event 导致边缘节点负载率 L_load > 80% 时，队列延迟呈非线性增长，ΔL_p99 ≈ L_base * (L_load / (1 - L_load))^2；若 L_load < 80%，ΔL_p99 ≈ 0。该非线性项需纳入 P99 合规成本计算的惩罚函数。

## Corrected Claim

事件期间 P99 延迟增量 ΔL_p99_event 的阈值效应：当 ΔK_event 导致边缘节点负载率 L_load > 80% 时，队列延迟呈非线性增长，ΔL_p99 ≈ L_base * (L_load / (1 - L_load))^2；若 L_load < 80%，ΔL_p99 ≈ 0。该非线性项需纳入 P99 合规成本计算的惩罚函数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

queueing theory p99 latency load factor nonlinear increase threshold
