# N23: NVMe SSD阵列的T_restore计算：T_restore = (Failed_Disk_Capacity / RAID_Reconstruction_B

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

NVMe SSD阵列的T_restore计算：T_restore = (Failed_Disk_Capacity / RAID_Reconstruction_Bandwidth) × 60，假设单盘故障，RAID5/6或ZFS镜像，重建带宽取决于剩余盘IOPS与顺序写吞吐（典型值：10GB/s~20GB/s for NVMe RAID）

## Corrected Claim

NVMe SSD阵列的T_restore计算：T_restore = (Failed_Disk_Capacity / RAID_Reconstruction_Bandwidth) × 60，假设单盘故障，RAID5/6或ZFS镜像，重建带宽取决于剩余盘IOPS与顺序写吞吐（典型值：10GB/s~20GB/s for NVMe RAID）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe RAID reconstruction time per TB
