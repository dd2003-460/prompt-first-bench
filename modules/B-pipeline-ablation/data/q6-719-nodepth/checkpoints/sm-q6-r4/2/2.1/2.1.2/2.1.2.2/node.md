# N207: N_Disks=8 的 RAID10 配置实际可用容量为 8×2TB/2=8TB，若采用 NVMe 全闪存阵列，需考虑 RAID 控制器或 HBA 卡的成本（约

- **status**: pending
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

父节点级核验未通过：不完备（子节点在主题上正交（分别讨论控制器选型、寿命/写入放大、背板线缆），且无冗余。但完备性不足：父节点明确包含“RAID10 配置实际可用容量为 8TB”这一关键计算，而三个子节点均未涉及容量验证或修正，遗漏了父节点的核心信息之一。）

## Search Query

RAID10 NVMe array controller HBA cost backplane cable 2024
