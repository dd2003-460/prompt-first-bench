# N394: PCIe Gen4 x16 理论单向带宽为 32 GB/s，双向理论带宽为 64 GB/s，有效双向带宽通常取 50%-70% 效率，即 32-45 GB/s。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N139, N140, N141

## Claim

PCIe Gen4 x16 理论单向带宽为 32 GB/s，双向理论带宽为 64 GB/s，有效双向带宽通常取 50%-70% 效率，即 32-45 GB/s。

## Corrected Claim

PCIe Gen4 x16 理论单向带宽为 32 GB/s，双向理论带宽为 64 GB/s，有效双向带宽通常取 50%-70% 效率，即 32-45 GB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen4 单通道速率 16 GT/s，x16 链路单向理论带宽 32 GB/s，双向 64 GB/s，有效带宽受协议开销影响通常取 50%-70% 效率，数值量级与工程常识一致。
