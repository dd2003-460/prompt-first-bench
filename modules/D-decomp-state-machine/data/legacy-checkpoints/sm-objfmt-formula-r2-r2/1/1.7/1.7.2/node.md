# N63: PCIe 5.0 x16 链路的有效单向传输带宽为 ~31.5 GB/s，双向为 ~63 GB/s。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

PCIe 5.0 x16 链路的有效单向传输带宽为 ~31.5 GB/s，双向为 ~63 GB/s。

## Corrected Claim

PCIe 5.0 x16 链路的有效单向传输带宽为 ~31.5 GB/s，双向为 ~63 GB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 单通道速率 32 GT/s，采用 128b/130b 编码，有效带宽约为 32 * (128/130) ≈ 31.5 GB/s，x16 链路单向即为该值，双向翻倍符合物理定义。
