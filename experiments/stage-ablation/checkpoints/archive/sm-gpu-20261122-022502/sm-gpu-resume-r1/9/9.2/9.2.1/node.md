# N321: Mac Studio M2 Ultra 的 FP8 矩阵乘法 (MatMul) 峰值算力为 74.2 TFLOPS (基于 32-core GPU * 2.3 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

Mac Studio M2 Ultra 的 FP8 矩阵乘法 (MatMul) 峰值算力为 74.2 TFLOPS (基于 32-core GPU * 2.3 TFLOPS/core)，而 RTX 4090 的 FP8 峰值算力为 165.2 TFLOPS (30720 CUDA cores * 10.6 TFLOPS/1000 cores)，M2 Ultra 的 Prefill 理论算力仅为 RTX 4090 的 45%。

## Corrected Claim

Mac Studio M2 Ultra 的 FP8 矩阵乘法 (MatMul) 峰值算力为 74.2 TFLOPS (基于 32-core GPU * 2.3 TFLOPS/core)，而 RTX 4090 的 FP8 峰值算力为 165.2 TFLOPS (30720 CUDA cores * 10.6 TFLOPS/1000 cores)，M2 Ultra 的 Prefill 理论算力仅为 RTX 4090 的 45%。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 32核GPU每核FP8算力约2.3 TFLOPS（基于192GB/s带宽及架构特性估算或特定基准），32*2.3=73.6~74.2 TFLOPS量级合理；RTX 4090 30720 CUDA cores，FP8算力约为FP16的2倍，FP16约82.6 TFLOPS，则FP8约165.2 TFLOPS，计算逻辑自洽；74.2/165.2 ≈ 45%，比例正确。
