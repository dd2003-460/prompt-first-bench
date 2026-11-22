# N386: PCIe Gen4 x16 单向理论带宽为 31.5 GB/s (有效载荷约 25-28 GB/s)，双向全双工带宽为 63 GB/s，这是 All-Reduc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

PCIe Gen4 x16 单向理论带宽为 31.5 GB/s (有效载荷约 25-28 GB/s)，双向全双工带宽为 63 GB/s，这是 All-Reduce 通信的物理上限，需与 NVLink 3.0 (600 GB/s) 形成对比基准。

## Corrected Claim

PCIe Gen4 x16 单向理论带宽为 31.5 GB/s (有效载荷约 25-28 GB/s)，双向全双工带宽为 63 GB/s，这是 All-Reduce 通信的物理上限，需与 NVLink 3.0 (600 GB/s) 形成对比基准。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen4 x16 单向理论带宽 31.5 GB/s 及双向 63 GB/s 符合标准规格，NVLink 3.0 600 GB/s 亦为已知稳定参数，数值量级合理且无内部矛盾。
