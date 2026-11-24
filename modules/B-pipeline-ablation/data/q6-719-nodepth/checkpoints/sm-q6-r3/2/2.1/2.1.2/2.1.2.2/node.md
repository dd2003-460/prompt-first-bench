# N207: N_Disks=8 的 RAID10 配置实际可用容量为 8×2TB/2=8TB，若采用 NVMe 全闪存阵列，需考虑 RAID 控制器或 HBA 卡的成本（约

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

N_Disks=8 的 RAID10 配置实际可用容量为 8×2TB/2=8TB，若采用 NVMe 全闪存阵列，需考虑 RAID 控制器或 HBA 卡的成本（约 ¥2,000-5,000），以及背板和线缆的成本（约 ¥500-1,000）。

## Corrected Claim

N_Disks=8 的 RAID10 配置实际可用容量为 8×2TB/2=8TB，若采用 NVMe 全闪存阵列，需考虑 RAID 控制器或 HBA 卡的成本（约 ¥2,000-5,000），以及背板和线缆的成本（约 ¥500-1,000）。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID10可用容量计算正确（8*2TB/2=8TB），硬件成本量级符合市场常识

## Search Query

RAID10 NVMe array controller HBA cost backplane cable 2024
