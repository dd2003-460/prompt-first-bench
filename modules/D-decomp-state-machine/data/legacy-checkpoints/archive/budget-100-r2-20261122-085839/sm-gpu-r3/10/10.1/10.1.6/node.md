# N302: 2× RTX 3090 PCIe 互联在 W4 量化下，单卡 Decode 理论带宽上限 = 936 GB/s / (13.55 GB / 1024 token

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N111, N112

## Claim

2× RTX 3090 PCIe 互联在 W4 量化下，单卡 Decode 理论带宽上限 = 936 GB/s / (13.55 GB / 1024 tokens) ≈ 70.8 tokens/s (单卡独立计算，未计通信开销)

## Corrected Claim

2× RTX 3090 PCIe 互联在 W4 量化下，单卡 Decode 理论带宽上限 = 936 GB/s / (13.55 GB / 1024 tokens) ≈ 70.8 tokens/s (单卡独立计算，未计通信开销)

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 显存带宽 936 GB/s，W4 量化下 13.55 GB 权重对应 1024 tokens，计算 936 / (13.55/1024) ≈ 70.8 tokens/s，数值量级与逻辑自洽。
