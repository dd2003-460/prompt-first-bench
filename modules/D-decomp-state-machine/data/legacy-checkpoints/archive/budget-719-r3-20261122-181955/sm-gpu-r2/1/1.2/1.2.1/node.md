# N45: A100 80GB PCIe 的 BF16/FP16 Tensor 算力为 312 TFLOPS (稀疏) / 156 TFLOPS (稠密)，显存带宽为 20

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

A100 80GB PCIe 的 BF16/FP16 Tensor 算力为 312 TFLOPS (稀疏) / 156 TFLOPS (稠密)，显存带宽为 2039 GB/s

## Corrected Claim

A100 80GB PCIe 的 BF16/FP16 Tensor 算力为 312 TFLOPS (稀疏) / 156 TFLOPS (稠密)，显存带宽为 2039 GB/s

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB PCIe 的官方规格中，BF16/FP16 Tensor Core 稠密算力为 156 TFLOPS，稀疏算力为 312 TFLOPS（2倍加速），显存带宽为 2039 GB/s（HBM2e），数值与量级均符合 NVIDIA 官方数据。
