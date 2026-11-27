# N109: 对比基准：1×A100 80GB (HBM2e, 2039 GB/s带宽) 运行BF16 Qwen3-27B的理论峰值Tokens/s = 2039 / 54 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

对比基准：1×A100 80GB (HBM2e, 2039 GB/s带宽) 运行BF16 Qwen3-27B的理论峰值Tokens/s = 2039 / 54 ≈ 37.8 Tokens/s；若使用FP8 (27GB权重)，理论峰值 = 2039 / 27 ≈ 75.5 Tokens/s，实际受计算瓶颈影响可能略低。

## Corrected Claim

对比基准：1×A100 80GB (HBM2e, 2039 GB/s带宽) 运行BF16 Qwen3-27B的理论峰值Tokens/s = 2039 / 54 ≈ 37.8 Tokens/s；若使用FP8 (27GB权重)，理论峰值 = 2039 / 27 ≈ 75.5 Tokens/s，实际受计算瓶颈影响可能略低。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e带宽确为2039 GB/s；Qwen3-27B BF16权重约54GB，FP8约27GB；解码阶段受内存带宽限制，理论峰值Tokens/s = 带宽/权重大小，计算无误。

## Search Query

A100 80GB HBM2e bandwidth 2039 GB/s LLM inference throughput calculation
