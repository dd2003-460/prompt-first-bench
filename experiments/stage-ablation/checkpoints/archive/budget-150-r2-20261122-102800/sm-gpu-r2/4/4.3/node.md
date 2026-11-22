# N24: NVIDIA H100 PCIe (80 GB) 的 BF16 Tensor Core 峰值算力为 989 TFLOPS，FP8 峰值算力为 1979 TFLO

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

NVIDIA H100 PCIe (80 GB) 的 BF16 Tensor Core 峰值算力为 989 TFLOPS，FP8 峰值算力为 1979 TFLOPS，INT8 峰值算力为 3958 TOPS。

## Corrected Claim

NVIDIA H100 PCIe (80 GB) 的 BF16 Tensor Core 峰值算力为 989 TFLOPS，FP8 峰值算力为 1979 TFLOPS，INT8 峰值算力为 3958 TOPS。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 PCIe 80GB 的 BF16 峰值算力约为 989 TFLOPS，FP8 为 2 倍（1979 TFLOPS），INT8 为 4 倍（3958 TOPS），数值量级与比例关系符合 NVIDIA 官方规格及硬件架构逻辑。
