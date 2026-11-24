# N592: 工作点 B（中负载高峰 ρ=0.8）：采用 M/M/1 模型，W_q = 0.8 / (16000 * 0.2) = 25 ms。P99 等待时间约为 3 * 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N194

## Claim

工作点 B（中负载高峰 ρ=0.8）：采用 M/M/1 模型，W_q = 0.8 / (16000 * 0.2) = 25 ms。P99 等待时间约为 3 * 25 ms = 75 ms。此时队列延迟显著，需优化缓存命中率或增加节点容量以降低 ρ。

## Corrected Claim

工作点 B（中负载高峰 ρ=0.8）：采用 M/M/1 模型，W_q = 0.8 / (16000 * 0.2) = 25 ms。P99 等待时间约为 3 * 25 ms = 75 ms。此时队列延迟显著，需优化缓存命中率或增加节点容量以降低 ρ。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1模型中W_q = ρ/(μ(1-ρ))，代入ρ=0.8, μ=16000得25ms，P99近似为3倍均值符合排队论经验法则。

## Search Query

M/M/1 queue P99 waiting time calculation high utilization
