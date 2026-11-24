# N157: 中性价比最优工作点：U=60%, RTT_core=20ms, T_processing=10ms, T_queueing=8ms 时，P99_core ≈ 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

中性价比最优工作点：U=60%, RTT_core=20ms, T_processing=10ms, T_queueing=8ms 时，P99_core ≈ 50 + 10 + 8 = 68ms，基础设施利用率适中，成本 C_infra ≈ 58 万元/POP/年，延迟与成本平衡，为推荐工作点

## Corrected Claim

中性价比最优工作点：U=60%, RTT_core=20ms, T_processing=10ms, T_queueing=8ms 时，P99_core ≈ 50 + 10 + 8 = 68ms，基础设施利用率适中，成本 C_infra ≈ 58 万元/POP/年，延迟与成本平衡，为推荐工作点

## Evidence

先验知识/题面给定，逻辑校验通过：P99延迟计算（50+10+8=68ms）符合排队论基本逻辑，成本数值量级合理，无内部矛盾。

## Search Query

edge node P99 latency optimal utilization 60% cost balance
