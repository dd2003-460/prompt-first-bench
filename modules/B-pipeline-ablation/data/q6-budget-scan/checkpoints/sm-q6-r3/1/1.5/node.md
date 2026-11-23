# N11: 排队延迟的P99值：T_queue_P99 = f(λ, μ, K) 其中λ为请求到达率，μ为服务速率，K为队列长度，使用M/M/K或M/G/1/K模型计算，典

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

排队延迟的P99值：T_queue_P99 = f(λ, μ, K) 其中λ为请求到达率，μ为服务速率，K为队列长度，使用M/M/K或M/G/1/K模型计算，典型值为0-20ms（低负载）/20-100ms（高负载）

## Corrected Claim

排队延迟的P99值：T_queue_P99 = f(λ, μ, K) 其中λ为请求到达率，μ为服务速率，K为队列长度，使用M/M/K或M/G/1/K模型计算，典型值为0-20ms（低负载）/20-100ms（高负载）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

queueing delay P99 for web server M/M/K model
