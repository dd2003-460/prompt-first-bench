# N508: H100 SXM5 运行 Qwen3-27B FP8 权重（27GB）时的理论 Decode 上限为 75.52 tokens/s，计算式：2039 GB/s 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N156

## Claim

H100 SXM5 运行 Qwen3-27B FP8 权重（27GB）时的理论 Decode 上限为 75.52 tokens/s，计算式：2039 GB/s (带宽) / 27 GB (权重大小)。

## Corrected Claim

H100 SXM5 运行 Qwen3-27B FP8 权重（27GB）时的理论 Decode 上限为 75.52 tokens/s，计算式：2039 GB/s (带宽) / 27 GB (权重大小)。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 显存带宽为 2039 GB/s，Qwen3-27B FP8 权重大小约为 27GB，理论 Decode 上限 = 带宽 / 权重大小 = 2039 / 27 ≈ 75.52 tokens/s，计算式与数值量级均合理。
