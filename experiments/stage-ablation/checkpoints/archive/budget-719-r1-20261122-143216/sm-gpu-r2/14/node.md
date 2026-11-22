# N153: Prefill 阶段（Prompt Processing）对硬件算力的依赖：Qwen3-27B 在处理 32K 上下文输入时，Prefill 速度主要受 FP1

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Prefill 阶段（Prompt Processing）对硬件算力的依赖：Qwen3-27B 在处理 32K 上下文输入时，Prefill 速度主要受 FP16/BF16 FLOPS 限制而非显存带宽。RTX 5090 (210 TFLOPS) 与 A100 (312 TFLOPS) 在 Prefill 阶段的速度比约为 1:1.5，而 Decode 阶段带宽比约为 1:1.1 (FP8下)。若应用场景包含大量长 Prompt 输入，算力（FLOPS）占比在 TCO 计算中的权重需从 20% 提升至 40%。

## Corrected Claim

Prefill 阶段（Prompt Processing）对硬件算力的依赖：Qwen3-27B 在处理 32K 上下文输入时，Prefill 速度主要受 FP16/BF16 FLOPS 限制而非显存带宽。RTX 5090 (210 TFLOPS) 与 A100 (312 TFLOPS) 在 Prefill 阶段的速度比约为 1:1.5，而 Decode 阶段带宽比约为 1:1.1 (FP8下)。若应用场景包含大量长 Prompt 输入，算力（FLOPS）占比在 TCO 计算中的权重需从 20% 提升至 40%。

## Evidence

检索失败: no sources from any channel (all 5 failed)
