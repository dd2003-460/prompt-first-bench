# N64: NVIDIA RTX 4090D 的 PCIe 版本 (PCIe 4.0 x16) 在双卡配置下的带宽瓶颈约为 32 GB/s，与 RTX 4090 相同，影响

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

NVIDIA RTX 4090D 的 PCIe 版本 (PCIe 4.0 x16) 在双卡配置下的带宽瓶颈约为 32 GB/s，与 RTX 4090 相同，影响多卡并行效率

## Corrected Claim

NVIDIA RTX 4090D 的 PCIe 版本 (PCIe 4.0 x16) 在双卡配置下的带宽瓶颈约为 32 GB/s，与 RTX 4090 相同，影响多卡并行效率

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 单向理论带宽约为 31.5 GB/s，工程上常近似为 32 GB/s，且 4090D 与 4090 接口规格一致，陈述符合物理事实。
