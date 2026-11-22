# N330: PCIe 4.0 x16 在 GPU 间点对点通信时的有效带宽通常低于理论峰值 64 GB/s (双向)，实际受驱动和拓扑影响，常见有效带宽约为 50-55 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

PCIe 4.0 x16 在 GPU 间点对点通信时的有效带宽通常低于理论峰值 64 GB/s (双向)，实际受驱动和拓扑影响，常见有效带宽约为 50-55 GB/s，需根据具体主板拓扑（P2P 是否启用）确定。

## Corrected Claim

PCIe 4.0 x16 在 GPU 间点对点通信时的有效带宽通常低于理论峰值 64 GB/s (双向)，实际受驱动和拓扑影响，常见有效带宽约为 50-55 GB/s，需根据具体主板拓扑（P2P 是否启用）确定。

## Evidence

先验知识/题面给定，逻辑校验通过
