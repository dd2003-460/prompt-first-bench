# N134: PCIe 5.0 x16 接口在双向传输 KV Cache 时的有效带宽效率因子：理论峰值 64 GB/s，实际受协议开销和驱动影响，有效带宽约为 50-55 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

PCIe 5.0 x16 接口在双向传输 KV Cache 时的有效带宽效率因子：理论峰值 64 GB/s，实际受协议开销和驱动影响，有效带宽约为 50-55 GB/s；若使用 PCIe 4.0，有效带宽约为 25-28 GB/s，需根据主机插槽代际确定分母。

## Corrected Claim

PCIe 5.0 x16 接口在双向传输 KV Cache 时的有效带宽效率因子：理论峰值 64 GB/s，实际受协议开销和驱动影响，有效带宽约为 50-55 GB/s；若使用 PCIe 4.0，有效带宽约为 25-28 GB/s，需根据主机插槽代际确定分母。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x16 理论带宽 64 GB/s，实际有效带宽 50-55 GB/s 符合工程经验（约 80-85% 效率）；PCIe 4.0 x16 理论 32 GB/s，实际 25-28 GB/s 亦符合逻辑。

## Search Query

PCIe 5.0 x16 effective bandwidth GB/s real world benchmark
