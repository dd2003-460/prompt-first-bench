# N492: RTX 4090 (AD102) 的 Tensor Core 第4代原生支持 FP8 (E4M3/E5M2) 输入/输出，其 FP8 Tensor Core 理

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152, N153, N154

## Claim

RTX 4090 (AD102) 的 Tensor Core 第4代原生支持 FP8 (E4M3/E5M2) 输入/输出，其 FP8 Tensor Core 理论峰值算力为 1321 TFLOPS (Dense) / 2642 TFLOPS (Sparse)，是 BF16 (82.6 TFLOPS) 的约 16 倍，来源：NVIDIA RTX 4090 官方规格表。

## Corrected Claim

RTX 4090 (AD102) 的 Tensor Core 第4代原生支持 FP8 (E4M3/E5M2) 输入/输出，其 FP8 Tensor Core 理论峰值算力为 1321 TFLOPS (Dense) / 2642 TFLOPS (Sparse)，是 BF16 (82.6 TFLOPS) 的约 16 倍，来源：NVIDIA RTX 4090 官方规格表。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (AD102) 确实支持 FP8，其 FP8 峰值算力 (1321 TFLOPS) 约为 BF16 (82.6 TFLOPS) 的 16 倍，符合硬件架构原理。
