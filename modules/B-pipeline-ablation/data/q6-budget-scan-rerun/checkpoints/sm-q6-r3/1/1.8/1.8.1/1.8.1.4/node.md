# N180: P99核心延迟工作点2（回源主导）：当 Miss_Rate_core ≥ 0.10 时，P99_core_self ≈ Miss_latency_core = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

P99核心延迟工作点2（回源主导）：当 Miss_Rate_core ≥ 0.10 时，P99_core_self ≈ Miss_latency_core = RTT_backhaul + Origin_Process + Origin_Delivery ≈ 50ms + 100ms + 20ms = 170ms，此时瓶颈为源站处理能力

## Corrected Claim

P99核心延迟工作点2（回源主导）：当 Miss_Rate_core ≥ 0.10 时，P99_core_self ≈ Miss_latency_core = RTT_backhaul + Origin_Process + Origin_Delivery ≈ 50ms + 100ms + 20ms = 170ms，此时瓶颈为源站处理能力

## Evidence

先验知识/题面给定，逻辑校验通过：在回源主导场景下，P99延迟由回源链路决定，数值加和（50+100+20=170ms）逻辑自洽，符合CDN/边缘计算典型延迟模型。
