# N425: Qwen3-27B 处理 32K 上下文输入的 Prefill 阶段所需总 FLOPs 计算公式为 2 × Model_Params × Sequence_Le

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N153

## Claim

Qwen3-27B 处理 32K 上下文输入的 Prefill 阶段所需总 FLOPs 计算公式为 2 × Model_Params × Sequence_Length = 2 × 27B × 32K ≈ 1.75 TFLOPs，该值用于评估不同硬件在 Prefill 阶段的耗时差异。

## Corrected Claim

Qwen3-27B 处理 32K 上下文输入的 Prefill 阶段所需总 FLOPs 计算公式为 2 × Model_Params × Sequence_Length = 2 × 27B × 32K ≈ 1.75 TFLOPs，该值用于评估不同硬件在 Prefill 阶段的耗时差异。

## Evidence

先验知识/题面给定，逻辑校验通过：2 × 27e9 × 32768 = 1.7616e15 ≈ 1.76 TFLOPs，与陈述中的 1.75 TFLOPs 量级及数值一致（允许微小舍入误差），公式符合 Transformer Prefill 阶段计算量的标准估算逻辑。
