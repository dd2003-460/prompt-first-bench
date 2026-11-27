# N79: Prefill 阶段的计算密度瓶颈主要受限于 GPU 的峰值算力 (TFLOPS)，对于 Qwen3-27B (27B 参数)，Prefill 32K toke

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

Prefill 阶段的计算密度瓶颈主要受限于 GPU 的峰值算力 (TFLOPS)，对于 Qwen3-27B (27B 参数)，Prefill 32K tokens 所需的 FLOPs 约为 2 * 27e9 * 32000 = 1.73e15 FLOPs (即 1730 TFLOPs)

## Corrected Claim

Prefill 阶段的计算密度瓶颈主要受限于 GPU 的峰值算力 (TFLOPS)，对于 Qwen3-27B (27B 参数)，Prefill 32K tokens 所需的 FLOPs 约为 2 * 27e9 * 32000 = 1.73e15 FLOPs (即 1730 TFLOPs)

## Evidence

先验知识/题面给定，逻辑校验通过：Transformer Prefill 阶段 FLOPs 估算公式为 2 * N_params * N_tokens，代入 27e9 和 32000 计算得 1.728e15 FLOPs，与陈述中的 1.73e15 一致，量级合理。
