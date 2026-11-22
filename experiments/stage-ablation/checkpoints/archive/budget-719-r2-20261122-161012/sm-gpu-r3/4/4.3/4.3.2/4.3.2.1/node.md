# N215: PCIe 4.0 x16 的单向理论带宽为 32 GB/s，双向为 64 GB/s，但有效可用带宽通常仅为理论值的 90-95% (约 28.8-30.4 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

PCIe 4.0 x16 的单向理论带宽为 32 GB/s，双向为 64 GB/s，但有效可用带宽通常仅为理论值的 90-95% (约 28.8-30.4 GB/s)，计算延迟时应使用有效带宽而非理论峰值。

## Corrected Claim

PCIe 4.0 x16 的单向理论带宽为 32 GB/s，双向为 64 GB/s，但有效可用带宽通常仅为理论值的 90-95% (约 28.8-30.4 GB/s)，计算延迟时应使用有效带宽而非理论峰值。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 单通道速率 16 GT/s，x16 理论带宽 32 GB/s，有效带宽 90-95% 符合工程常识。
