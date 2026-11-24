# N329: 并发负载下的排队延迟 T_queue 遵循 M/M/1 或 M/G/1 队列模型，T_queue = ρ / (μ(1-ρ))，其中 ρ 为利用率，μ 为服务率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

并发负载下的排队延迟 T_queue 遵循 M/M/1 或 M/G/1 队列模型，T_queue = ρ / (μ(1-ρ))，其中 ρ 为利用率，μ 为服务率，P99 延迟对 ρ > 0.8 极其敏感，需监控 POP 节点 CPU/IO 饱和度。

## Corrected Claim

并发负载下的排队延迟 T_queue 遵循 M/M/1 或 M/G/1 队列模型，T_queue = ρ / (μ(1-ρ))，其中 ρ 为利用率，μ 为服务率，P99 延迟对 ρ > 0.8 极其敏感，需监控 POP 节点 CPU/IO 饱和度。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1 队列等待时间公式 Wq = ρ/(μ(1-ρ)) 符合排队论标准推导，且高利用率下延迟敏感性符合物理直觉。
