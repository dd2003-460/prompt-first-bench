# N459: PCIe 4.0 x16 接口的理论单向带宽为 32 GB/s，双向带宽为 64 GB/s，但实际有效带宽受协议开销影响，通常约为理论值的 80%-90%，即单

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N147

## Claim

PCIe 4.0 x16 接口的理论单向带宽为 32 GB/s，双向带宽为 64 GB/s，但实际有效带宽受协议开销影响，通常约为理论值的 80%-90%，即单向 25.6-28.8 GB/s

## Corrected Claim

PCIe 4.0 x16 接口的理论单向带宽为 32 GB/s，双向带宽为 64 GB/s，但实际有效带宽受协议开销影响，通常约为理论值的 80%-90%，即单向 25.6-28.8 GB/s

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 单通道速率 16 GT/s，x16 接口理论单向带宽 32 GB/s，双向 64 GB/s，实际有效带宽受协议开销影响约为理论值的 80%-90%，数值量级与工程常识一致。

## Search Query

PCIe 4.0 x16 effective bandwidth GB/s
