# N590: 工作点 C（突发热点事件）：当病毒式传播事件发生时，局部区域流量瞬时增加 200%（K_event=3），单 POP 峰值 λ 可达 6,666 req/s（基

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N193

## Claim

工作点 C（突发热点事件）：当病毒式传播事件发生时，局部区域流量瞬时增加 200%（K_event=3），单 POP 峰值 λ 可达 6,666 req/s（基于东部基线）。若 μ=16,000 req/s，ρ = 0.42；若 μ=8,000 req/s，ρ = 0.83。此时 ρ 接近 1，M/M/1 延迟急剧上升，必须引入 M/M/c 模型或队列溢出机制，否则 P99 延迟将超过阈值。

## Corrected Claim

工作点 C（突发热点事件）：当病毒式传播事件发生时，局部区域流量瞬时增加 200%（K_event=3），单 POP 峰值 λ 可达 6,666 req/s（基于东部基线）。若 μ=16,000 req/s，ρ = 0.42；若 μ=8,000 req/s，ρ = 0.83。此时 ρ 接近 1，M/M/1 延迟急剧上升，必须引入 M/M/c 模型或队列溢出机制，否则 P99 延迟将超过阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（6666/16000≈0.42, 6666/8000≈0.83），M/M/1队列论在ρ接近1时延迟急剧上升的结论符合排队论基本规律。

## Search Query

CDN burst traffic handling queueing theory M/M/c model
