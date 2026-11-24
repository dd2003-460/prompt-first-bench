# N270: RAID 控制器与背板功耗绝对值估算：对于支持 471 块 NVMe SSD 的大型阵列，主 RAID/HBA 控制器功耗约为 25-35W，PCIe 背板及线

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

RAID 控制器与背板功耗绝对值估算：对于支持 471 块 NVMe SSD 的大型阵列，主 RAID/HBA 控制器功耗约为 25-35W，PCIe 背板及线缆损耗约为 50-70W，合计 P_ctrl_backplane ≈ 75-105W，而非简单的百分比关系

## Corrected Claim

RAID 控制器与背板功耗绝对值估算：对于支持 471 块 NVMe SSD 的大型阵列，主 RAID/HBA 控制器功耗约为 25-35W，PCIe 背板及线缆损耗约为 50-70W，合计 P_ctrl_backplane ≈ 75-105W，而非简单的百分比关系

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点本质上是同一物理量（功耗）在不同规模下的参数化取值，属于连续变量而非离散的正交概念。此外，工作点C直接否定并修正了父节点给出的范围（75-105W vs >150W），导致父子逻辑冲突，破坏了正交性和一致性。）

## Search Query

large scale nvme raid controller backplane power consumption watts
