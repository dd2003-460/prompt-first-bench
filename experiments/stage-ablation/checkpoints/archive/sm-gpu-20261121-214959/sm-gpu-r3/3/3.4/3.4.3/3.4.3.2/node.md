# N228: 修正后的 4x RTX 4090 (TP=4) 纯通信延迟计算：总通信量 = 60 layers * 8 KB = 480 KB。在 PCIe 4.0 x16 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

修正后的 4x RTX 4090 (TP=4) 纯通信延迟计算：总通信量 = 60 layers * 8 KB = 480 KB。在 PCIe 4.0 x16 (32 GB/s) 带宽下，理论通信延迟 = 0.00048 GB / 32 GB/s = 15 μs/token。此延迟远低于计算时间，证明 N83 中 '131 ms/token' 的结论是错误的。

## Corrected Claim

修正后的 4x RTX 4090 (TP=4) 纯通信延迟计算：总通信量 = 60 layers * 8 KB = 480 KB。在 PCIe 4.0 x16 (32 GB/s) 带宽下，理论通信延迟 = 0.00048 GB / 32 GB/s = 15 μs/token。此延迟远低于计算时间，证明 N83 中 '131 ms/token' 的结论是错误的。

## Evidence

先验知识/题面给定，逻辑校验通过：480KB/32GB/s ≈ 15μs，量级与计算正确，且远低于131ms，逻辑自洽。
