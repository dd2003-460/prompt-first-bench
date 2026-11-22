# N56: NVIDIA RTX 4090 的 PCIe 版本 (PCIe 4.0 x16) 在双卡配置下的带宽瓶颈约为 32 GB/s (16 GB/s * 2)，显著低

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

NVIDIA RTX 4090 的 PCIe 版本 (PCIe 4.0 x16) 在双卡配置下的带宽瓶颈约为 32 GB/s (16 GB/s * 2)，显著低于 NVLink 或单卡内部带宽，影响多卡并行效率

## Corrected Claim

NVIDIA RTX 4090 的 PCIe 版本 (PCIe 4.0 x16) 在双卡配置下的带宽瓶颈约为 32 GB/s (16 GB/s * 2)，显著低于 NVLink 或单卡内部带宽，影响多卡并行效率

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 单向带宽理论值约为 32 GB/s，双卡配置下总带宽瓶颈计算合理，且显著低于 NVLink 带宽符合工程常识。
