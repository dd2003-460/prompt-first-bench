# N210: 2x RTX 4090 在 PCIe 4.0 x16 互联下的理论双向带宽为 64 GB/s，但实际有效带宽受协议开销影响约为 55-60 GB/s，需使用此有

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67, N68, N69

## Claim

2x RTX 4090 在 PCIe 4.0 x16 互联下的理论双向带宽为 64 GB/s，但实际有效带宽受协议开销影响约为 55-60 GB/s，需使用此有效带宽值进行延迟计算。

## Corrected Claim

2x RTX 4090 在 PCIe 4.0 x16 互联下的理论双向带宽为 64 GB/s，实际有效带宽受协议开销影响通常约为 56-60 GB/s（损耗约 5-10%），需使用此有效带宽值进行延迟计算。

## Evidence

[质询]数值量级与协议开销比例存疑：PCIe 4.0 x16 单向理论带宽为 32 GB/s，双向为 64 GB/s。实际有效带宽通常受 TLP 头、CRC、流控等开销影响，损耗通常在 5%-10% 左右，即单向约 28-30 GB/s，双向约 56-60 GB/s。陈述中给出的 55-60 GB/s 范围下限 55 GB/s 意味着损耗超过 14%，这在标准 PCIe 4.0 负载下偏高，除非考虑了极端的非对齐访问或特定驱动开销，但作为通用理论值略显保守且缺乏具体场景限定。 | 经验事实，逻辑自洽但缺来源支持。PCIe 4.0 x16 双向理论带宽 64 GB/s 正确，实际带宽受协议开销影响低于理论值符合物理直觉，但具体数值 55-60 GB/s 缺乏直接来源佐证，且下限值可能偏低。

## Search Query

PCIe 4.0 x16 effective bandwidth GB/s overhead
