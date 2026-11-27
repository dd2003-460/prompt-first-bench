# N319: A100 80GB SXM4 在 BF16 精度下的理论峰值算力为 312 TFLOPS，此数值基于 NVIDIA 官方规格，是计算 Prefill 耗时的分子

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

A100 80GB SXM4 在 BF16 精度下的理论峰值算力为 312 TFLOPS，此数值基于 NVIDIA 官方规格，是计算 Prefill 耗时的分子基础。

## Corrected Claim

A100 80GB SXM4 在 BF16 精度下的理论峰值算力为 312 TFLOPS，此数值基于 NVIDIA 官方规格，是计算 Prefill 耗时的分子基础。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA A100 80GB SXM4 官方规格中 BF16 Tensor Core 峰值算力确为 312 TFLOPS（含稀疏加速为 624 TFLOPS，此处指稠密计算），数值量级与单位合理，符合硬件事实。
