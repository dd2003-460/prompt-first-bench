# N158: 高成本低性工作点：U=80%, RTT_core=20ms, T_processing=12ms, T_queueing=25ms 时，P99_core ≈ 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

高成本低性工作点：U=80%, RTT_core=20ms, T_processing=12ms, T_queueing=25ms 时，P99_core ≈ 50 + 12 + 25 = 87ms，基础设施利用率高，成本 C_infra ≈ 52 万元/POP/年，但 P99 延迟显著上升，队列延迟主导，需扩容或限流

## Corrected Claim

高成本低性工作点：U=80%, RTT_core=20ms, T_processing=12ms, T_queueing=25ms 时，P99_core ≈ 50 + 12 + 25 = 87ms，基础设施利用率高，成本 C_infra ≈ 52 万元/POP/年，但 P99 延迟显著上升，队列延迟主导，需扩容或限流

## Evidence

先验知识/题面给定，逻辑校验通过：P99延迟计算（50+12+25=87ms）符合加法模型，高利用率（80%）导致队列延迟显著增加符合排队论直觉，成本数值量级合理。

## Search Query

edge node P99 latency high utilization 80% queueing delay cost
