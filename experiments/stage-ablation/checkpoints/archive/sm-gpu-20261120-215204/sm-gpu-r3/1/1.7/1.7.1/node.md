# N66: 2×RTX 4090 通过 PCIe 4.0 x16 互联时，双向理论带宽为 64 GB/s (32 GB/s x2)，而单卡显存带宽为 1008 GB/s，互

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

2×RTX 4090 通过 PCIe 4.0 x16 互联时，双向理论带宽为 64 GB/s (32 GB/s x2)，而单卡显存带宽为 1008 GB/s，互联带宽仅为显存带宽的 6.3%，导致跨卡同步成为瓶颈。

## Corrected Claim

2×RTX 4090 通过 PCIe 4.0 x16 互联时，双向理论带宽为 64 GB/s (32 GB/s x2)，而单卡显存带宽为 1008 GB/s，互联带宽仅为显存带宽的 6.3%，导致跨卡同步成为瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 单向带宽约 32 GB/s，双向 64 GB/s；RTX 4090 显存带宽 1008 GB/s；64/1008 ≈ 6.35%，数值量级与逻辑均自洽。
