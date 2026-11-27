# N41: RTX 3090 的 BF16/FP16 Tensor 算力为 35.6 TFLOPS，显存带宽为 936 GB/s，显存容量 24GB GDDR6X

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

RTX 3090 的 BF16/FP16 Tensor 算力为 35.6 TFLOPS，显存带宽为 936 GB/s，显存容量 24GB GDDR6X

## Corrected Claim

RTX 3090 的 BF16/FP16 Tensor 算力为 35.6 TFLOPS，显存带宽为 936 GB/s，显存容量 24GB GDDR6X

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 拥有 10496 个 CUDA 核心，FP16/BF16 Tensor Core 算力为 10496 * 2 * 2 * 1.7GHz ≈ 35.6 TFLOPS；显存带宽 936 GB/s 与 24GB GDDR6X 规格符合 NVIDIA 官方数据。
