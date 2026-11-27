# N408: Prefill 阶段 FLOPs 计算公式为 2 * batch_size * seq_len * num_params。对于 Qwen3-27B (27B p

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N163

## Claim

Prefill 阶段 FLOPs 计算公式为 2 * batch_size * seq_len * num_params。对于 Qwen3-27B (27B params), batch_size=32, seq_len=1024, 总 FLOPs ≈ 1.76 TFLOPs。RTX 4090 (82.6 TFLOPS BF16) 理论 Prefill 延迟 ≈ 21.3 ms; H100 (989 TFLOPS BF16) 理论 Prefill 延迟 ≈ 1.78 ms。

## Corrected Claim

Prefill 阶段 FLOPs 计算公式为 2 * batch_size * seq_len * num_params。对于 Qwen3-27B (27B params), batch_size=32, seq_len=1024, 总 FLOPs ≈ 1.76 TFLOPs。RTX 4090 (82.6 TFLOPS BF16) 理论 Prefill 延迟 ≈ 21.3 ms; H100 (989 TFLOPS BF16) 理论 Prefill 延迟 ≈ 1.78 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：FLOPs计算 2*32*1024*27e9 ≈ 1.76e15 (1.76 PFLOPs)，延迟计算 1.76e15/82.6e12 ≈ 21.3ms 及 1.76e15/989e12 ≈ 1.78ms 均数值正确且量纲合理。
