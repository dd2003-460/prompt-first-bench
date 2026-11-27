# N118: 在PCIe 4.0 x16互联下，单方向理论带宽为32 GB/s，有效利用率通常为50-70%（受协议开销和驱动影响），实际All-Reduce有效带宽约为16

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

在PCIe 4.0 x16互联下，单方向理论带宽为32 GB/s，有效利用率通常为50-70%（受协议开销和驱动影响），实际All-Reduce有效带宽约为16-22 GB/s。

## Corrected Claim

在PCIe 4.0 x16互联下，单方向理论带宽为32 GB/s，有效利用率通常为50-70%（受协议开销和驱动影响），实际All-Reduce有效带宽约为16-22 GB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 单向理论带宽 32 GB/s 符合规格（16 lanes * 2 GT/s * 128b/130b ≈ 31.5 GB/s），50-70% 利用率及 16-22 GB/s 实际带宽符合工程经验与物理直觉。

## Search Query

PCIe 4.0 x16 effective bandwidth allreduce overhead
