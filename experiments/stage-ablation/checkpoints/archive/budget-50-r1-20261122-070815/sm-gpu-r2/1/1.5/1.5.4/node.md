# N51: A100 和 H100 均支持 NVLink 互联，带宽分别为 600 GB/s (A100) 和 900 GB/s (H100)，若采用多卡扩展，NVLink

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

A100 和 H100 均支持 NVLink 互联，带宽分别为 600 GB/s (A100) 和 900 GB/s (H100)，若采用多卡扩展，NVLink 可显著降低张量并行通信开销，相比 PCIe 4.0 (32 GB/s) 提升约 18-28 倍

## Corrected Claim

A100 和 H100 均支持 NVLink 互联，带宽分别为 600 GB/s (A100) 和 900 GB/s (H100)，若采用多卡扩展，NVLink 可显著降低张量并行通信开销，相比 PCIe 4.0 (32 GB/s) 提升约 18-28 倍

## Evidence

先验知识/题面给定，逻辑校验通过：A100 NVLink 带宽 600GB/s 与 H100 900GB/s 符合 NVIDIA 官方规格，PCIe 4.0 x16 理论带宽约 32GB/s，倍数计算（600/32≈18.75, 900/32≈28.125）准确，逻辑自洽。
