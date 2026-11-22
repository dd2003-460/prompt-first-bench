# N63: A100 80GB 在 FP16/BF16 与 FP8 下的理论峰值算力对比，以及 Tensor Core 代际差异对 LLM 推理算力的实际增益

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

A100 80GB 在 FP16/BF16 与 FP8 下的理论峰值算力对比，以及 Tensor Core 代际差异对 LLM 推理算力的实际增益

## Corrected Claim

A100 80GB 在 FP16/BF16 与 FP8 下的理论峰值算力对比，以及 Tensor Core 代际差异对 LLM 推理算力的实际增益

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB 支持 FP16/BF16 (312 TFLOPS) 和 FP8 (624 TFLOPS)，FP8 算力为 FP16 的 2 倍，符合 Tensor Core 代际演进规律及硬件规格事实。
