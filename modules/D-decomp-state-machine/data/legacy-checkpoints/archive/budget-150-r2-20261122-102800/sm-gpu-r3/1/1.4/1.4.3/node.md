# N66: 2×RTX 4090 在 PCIe 4.0 (有效带宽 ~32 GB/s) 下的 AllReduce 延迟：Latency = Comm_Vol / Bandw

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

2×RTX 4090 在 PCIe 4.0 (有效带宽 ~32 GB/s) 下的 AllReduce 延迟：Latency = Comm_Vol / Bandwidth = 67.1 MB / 32 GB/s ≈ 2.1 ms/token。

## Corrected Claim

2×RTX 4090 在 PCIe 4.0 (有效带宽 ~32 GB/s) 下的 AllReduce 延迟：Latency = Comm_Vol / Bandwidth = 67.1 MB / 32 GB/s ≈ 2.1 ms/token。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 双向有效带宽约 32 GB/s，67.1 MB / 32 GB/s ≈ 2.097 ms，计算无误且量级合理。
