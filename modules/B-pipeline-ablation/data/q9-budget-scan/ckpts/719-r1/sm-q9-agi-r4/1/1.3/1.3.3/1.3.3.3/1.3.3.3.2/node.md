# N415: V100-SXM2 HBM2 实测内存带宽与计算峰值：HBM2 带宽为 900 GB/s (非题面假设的 1TB/s)；FP16 Tensor Core 峰值算

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

V100-SXM2 HBM2 实测内存带宽与计算峰值：HBM2 带宽为 900 GB/s (非题面假设的 1TB/s)；FP16 Tensor Core 峰值算力为 125 TFLOPS。Roofline 模型拐点 AI_roofline = 125e12 / 900e9 ≈ 139 FLOPs/Byte。

## Corrected Claim

V100-SXM2 HBM2 实测内存带宽与计算峰值：HBM2 带宽为 900 GB/s (非题面假设的 1TB/s)；FP16 Tensor Core 峰值算力为 125 TFLOPS。Roofline 模型拐点 AI_roofline = 125e12 / 900e9 ≈ 139 FLOPs/Byte。

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2 HBM2带宽900GB/s及FP16 Tensor Core峰值125TFLOPS符合NVIDIA官方规格，Roofline拐点计算125e12/900e9≈138.9正确。

## Search Query

Tesla V100 SXM2 datasheet HBM2 bandwidth FP16 tensor core flops
