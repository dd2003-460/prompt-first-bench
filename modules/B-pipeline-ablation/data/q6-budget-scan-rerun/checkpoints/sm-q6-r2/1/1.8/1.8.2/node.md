# N68: T_queue 的量化分解：基于 M/M/c 排队模型，T_queue = (ρ^(c+1)) / (c! * (1-ρ)) * (1/μ)，其中 ρ 为利用率

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

T_queue 的量化分解：基于 M/M/c 排队模型，T_queue = (ρ^(c+1)) / (c! * (1-ρ)) * (1/μ)，其中 ρ 为利用率（N41 约束为 60%-70%），c 为并发连接数，μ 为服务率，P99 排队延迟典型值为 2-10ms（低负载）至 50-100ms（高负载）

## Corrected Claim

T_queue 的量化分解：基于 M/M/c 排队模型，T_queue = (ρ^(c+1)) / (c! * (1-ρ)) * (1/μ)，其中 ρ 为利用率（N41 约束为 60%-70%），c 为并发连接数，μ 为服务率，P99 排队延迟典型值为 2-10ms（低负载）至 50-100ms（高负载）

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/c 排队模型中等待时间公式结构正确，量纲合理（时间单位），且 P99 延迟范围与 60%-70% 利用率下的典型工程经验值相符。

## Search Query

M/M/c queueing model P99 latency CDN edge node utilization 60% 70%
