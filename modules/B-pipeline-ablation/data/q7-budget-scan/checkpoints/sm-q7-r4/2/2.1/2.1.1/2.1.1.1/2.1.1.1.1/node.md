# N474: RAID-6 有效容量公式展开：C_eff = (N_disks - 2) * C_disk * (1 - FS_overhead)。其中 N_disks=40

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N160

## Claim

RAID-6 有效容量公式展开：C_eff = (N_disks - 2) * C_disk * (1 - FS_overhead)。其中 N_disks=40, C_disk=16TB, FS_overhead=0.03 (XFS typical)。计算：C_eff = (40 - 2) * 16 * 0.97 = 38 * 16 * 0.97 = 608 * 0.97 = 589.76 TB。这与父节点中的 588.8TB 略有差异，源于文件系统开销计算基数不同（父节点用总容量，此处用净容量）。

## Corrected Claim

RAID-6 有效容量公式展开：C_eff = (N_disks - 2) * C_disk * (1 - FS_overhead)。其中 N_disks=40, C_disk=16TB, FS_overhead=0.03 (XFS typical)。计算：C_eff = (40 - 2) * 16 * 0.97 = 38 * 16 * 0.97 = 608 * 0.97 = 589.76 TB。这与父节点中的 588.8TB 略有差异，源于文件系统开销计算基数不同（父节点用总容量，此处用净容量）。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-6 有效容量公式及算术运算正确，差异解释符合逻辑。

## Search Query

RAID-6 effective capacity calculation formula filesystem overhead
