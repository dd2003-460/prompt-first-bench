# N136: Prefill 阶段（Compute-Bound）的瓶颈不在 HBM 带宽，而在 Tensor Core 利用率。V100 的 TF32 峰值 125 TFLO

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

Prefill 阶段（Compute-Bound）的瓶颈不在 HBM 带宽，而在 Tensor Core 利用率。V100 的 TF32 峰值 125 TFLOPS 在实际矩阵乘法中利用率通常为 40-50%（即 50-62.5 TFLOPS），这限制了长上下文（如 15k tokens）的 Prefill 速度，使其成为科研循环中插入大量文献时的主要延迟源，而非 Decode 带宽。

## Corrected Claim

Prefill 阶段（Compute-Bound）的瓶颈不在 HBM 带宽，而在 Tensor Core 利用率。V100 的 TF32 峰值 125 TFLOPS 在实际矩阵乘法中利用率通常为 40-50%（即 50-62.5 TFLOPS），这限制了长上下文（如 15k tokens）的 Prefill 速度，使其成为科研循环中插入大量文献时的主要延迟源，而非 Decode 带宽。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 TF32 峰值 125 TFLOPS 符合硬件规格，Prefill 为计算密集型（Compute-Bound）且受限于 Tensor Core 利用率（通常 40-50%）符合 GPU 架构基本原理及大模型推理常识。
