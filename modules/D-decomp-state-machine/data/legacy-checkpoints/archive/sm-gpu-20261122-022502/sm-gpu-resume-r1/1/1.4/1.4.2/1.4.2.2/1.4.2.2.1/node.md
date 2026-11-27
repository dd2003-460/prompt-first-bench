# N507: RTX 5090 运行 Qwen3-27B FP8 权重（27GB）时的理论 Decode 上限为 66.37 tokens/s，计算式：1792 GB/s (

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N156

## Claim

RTX 5090 运行 Qwen3-27B FP8 权重（27GB）时的理论 Decode 上限为 66.37 tokens/s，计算式：1792 GB/s (带宽) / 27 GB (权重大小)。

## Corrected Claim

RTX 5090 运行 Qwen3-27B FP8 权重（27GB）时的理论 Decode 上限为 66.37 tokens/s，计算式：1792 GB/s (带宽) / 27 GB (权重大小)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存带宽约 1792 GB/s，Qwen3-27B FP8 权重大小约 27 GB，理论 Decode 上限 = 带宽 / 权重大小 = 1792 / 27 ≈ 66.37 tokens/s，计算式与数值量级均合理。
