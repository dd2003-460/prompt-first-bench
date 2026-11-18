# N68: Tokens/second (生成速度) 的计算公式为 Throughput = Memory Bandwidth / (Model Size in Bytes

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

Tokens/second (生成速度) 的计算公式为 Throughput = Memory Bandwidth / (Model Size in Bytes * Precision Factor)，对于 27B BF16 模型，Throughput ≈ Bandwidth / 54GB

## Corrected Claim

Tokens/second (生成速度) 的计算公式为 Throughput = Memory Bandwidth / (Model Size in Bytes * Precision Factor)，对于 27B BF16 模型，Throughput ≈ Bandwidth / 54GB

## Evidence

先验知识/题面给定，逻辑校验通过
