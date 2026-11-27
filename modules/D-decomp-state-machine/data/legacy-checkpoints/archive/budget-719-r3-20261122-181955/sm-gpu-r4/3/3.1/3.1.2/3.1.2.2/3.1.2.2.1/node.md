# N769: A100 80GB HBM2e 在 BF16 权重读取时的理论峰值内存带宽为 2039 GB/s，基于 HBM2e 8-stack 架构规格（NVIDIA 官方

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N275

## Claim

A100 80GB HBM2e 在 BF16 权重读取时的理论峰值内存带宽为 2039 GB/s，基于 HBM2e 8-stack 架构规格（NVIDIA 官方数据表）。

## Corrected Claim

A100 80GB HBM2e 在 BF16 权重读取时的理论峰值内存带宽为 2039 GB/s，基于 HBM2e 8-stack 架构规格（NVIDIA 官方数据表）。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB 采用 8 个 HBM2e 堆栈，单堆栈带宽约 255 GB/s，总带宽 2039 GB/s 符合 NVIDIA 官方规格及物理量级。
