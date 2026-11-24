# N5: 本地NVMe SSD阵列采用RAID-10冗余机制，有效可用容量 = 原始物理容量 × 0.5（RAID-10冗余比）

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

本地NVMe SSD阵列采用RAID-10冗余机制，有效可用容量 = 原始物理容量 × 0.5（RAID-10冗余比）

## Corrected Claim

本地NVMe SSD阵列采用RAID-10冗余机制，有效可用容量 = 原始物理容量 × 0.5（RAID-10冗余比）

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-10由RAID-1镜像和RAID-0条带化组合而成，其存储效率固定为50%，即有效容量等于物理总容量的一半，符合存储技术基本原理。
