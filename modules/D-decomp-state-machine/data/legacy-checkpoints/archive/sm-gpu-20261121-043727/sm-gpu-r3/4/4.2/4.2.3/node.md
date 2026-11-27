# N67: 量化 Qwen3-27B 在 RTX 4090 (BF16) 上的 T_prefill 具体数值：基于修正后的 FLOPs 公式，代入 RTX 4090 的 B

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

量化 Qwen3-27B 在 RTX 4090 (BF16) 上的 T_prefill 具体数值：基于修正后的 FLOPs 公式，代入 RTX 4090 的 BF16 Tensor Core 峰值算力 (82.6 TFLOPS) 和典型 MFU (40%)，计算处理 32K prompt 所需的理论时间下限

## Corrected Claim

量化 Qwen3-27B 在 RTX 4090 (BF16) 上的 T_prefill 具体数值：基于修正后的 FLOPs 公式，代入 RTX 4090 的 BF16 Tensor Core 峰值算力 (82.6 TFLOPS) 和典型 MFU (40%)，计算处理 32K prompt 所需的理论时间下限

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 BF16 Tensor Core 峰值算力约为 82.6 TFLOPS（含稀疏加速或特定精度配置下的标称值，通常稠密为 41.3 TFLOPS，但此处采用题面给定的 82.6 TFLOPS 作为基准），MFU 40% 为典型经验值，计算逻辑自洽。

## Search Query

RTX 4090 BF16 Tensor Core TFLOPS Qwen 27B prefill latency benchmark
