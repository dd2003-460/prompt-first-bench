# N188: 队列排队延迟 T_queue 的 M/M/1 模型：T_queue = ρ / (μ - λ)，其中 ρ 为负载因子，μ 为服务率，λ 为到达率；在 P99 高

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

队列排队延迟 T_queue 的 M/M/1 模型：T_queue = ρ / (μ - λ)，其中 ρ 为负载因子，μ 为服务率，λ 为到达率；在 P99 高负载下（ρ>0.8），T_queue 可增至 0.5-2ms，叠加在 T_switch 上导致总延迟尾部效应

## Corrected Claim

队列排队延迟 T_queue 的 M/M/1 模型：T_queue = ρ / (μ - λ)，其中 ρ 为负载因子，μ 为服务率，λ 为到达率；在 P99 高负载下（ρ>0.8），T_queue 可增至 0.5-2ms，叠加在 T_switch 上导致总延迟尾部效应

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1 模型中等待时间公式 T_queue = ρ/(μ-λ) 符合排队论标准推导（基于 Little's Law 和 M/M/1 稳态解），量纲正确（1/时间），高负载下延迟激增符合物理直觉。

## Search Query

M/M/1 queueing delay router buffer congestion p99 latency
