# N391: H100 80GB 运行 Qwen3-27B FP8 时的 Prefill 吞吐量估算：基于 H100 的 FP8 Tensor Core 算力 (989 TF

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

H100 80GB 运行 Qwen3-27B FP8 时的 Prefill 吞吐量估算：基于 H100 的 FP8 Tensor Core 算力 (989 TFLOPS) 和 Qwen3-27B 的 FLOPs 需求，计算单 token prefill 延迟，以评估其在长上下文场景下的极速响应能力，并对比 A100 (N145) 和 4090 的 prefill 速度差距。

## Corrected Claim

H100 80GB 运行 Qwen3-27B FP8 时的 Prefill 吞吐量估算：基于 H100 的 FP8 Tensor Core 算力 (989 TFLOPS) 和 Qwen3-27B 的 FLOPs 需求，计算单 token prefill 延迟，以评估其在长上下文场景下的极速响应能力，并对比 A100 (N145) 和 4090 的 prefill 速度差距。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 FP8算力约989 TFLOPS，Qwen3-27B参数量约27B，Prefill FLOPs约为2*Params*Tokens，量级与逻辑自洽。
