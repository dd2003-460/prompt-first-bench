# N206: NVMe SSD RAID6 重建的实际瓶颈带宽受限于 PCIe 通道聚合上限与 RAID 控制器单口限速，典型 16x PCIe Gen4 控制器背板聚合写带

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

NVMe SSD RAID6 重建的实际瓶颈带宽受限于 PCIe 通道聚合上限与 RAID 控制器单口限速，典型 16x PCIe Gen4 控制器背板聚合写带宽约为 12-15 GB/s，此值决定了重建时间的物理下限，即使单盘带宽更高也无法突破。

## Corrected Claim

NVMe SSD RAID6 重建的实际瓶颈带宽受限于 PCIe 通道聚合上限与 RAID 控制器单口限速，典型 16x PCIe Gen4 控制器背板聚合写带宽约为 12-15 GB/s，此值决定了重建时间的物理下限，即使单盘带宽更高也无法突破。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen4 x16 理论带宽约 32GB/s，扣除协议开销及RAID控制器处理损耗后，12-15GB/s 的聚合写带宽符合工程实际量级，且 RAID6 重建确实受限于控制器背板带宽而非单盘带宽。
