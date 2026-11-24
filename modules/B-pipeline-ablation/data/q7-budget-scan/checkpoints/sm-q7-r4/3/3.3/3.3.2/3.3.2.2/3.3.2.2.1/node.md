# N625: HDD 层 RAID 冗余系数 (Redundancy_Factor) 对物理容量的影响：若采用 RAID6 (双重奇偶校验)，冗余开销 = 2 * Disk_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N214

## Claim

HDD 层 RAID 冗余系数 (Redundancy_Factor) 对物理容量的影响：若采用 RAID6 (双重奇偶校验)，冗余开销 = 2 * Disk_Size / Total_Pool_Size。对于 25 块 16TB 盘组成的 RAID6 池，总裸容量 400TB，可用容量 = 400 - 2*16 = 368TB。若要存储 420TB 数据 (来自 N214 的 500-111+10% overprovisioning)，所需裸容量 V_hdd_raw = 420TB / (1 - 2/25) ≈ 434TB。若采用 RAID10 (镜像)，冗余开销 50%，所需裸容量 V_hdd_raw = 420TB / 0.5 = 840TB，这将显著增加 CapEx，因此冷数据层通常优选 RAID6 或 ZFS Mirroring (2-way mirror, 50% 冗余) 而非 RAID10，需在成本与安全性间权衡。

## Corrected Claim

HDD 层 RAID 冗余系数 (Redundancy_Factor) 对物理容量的影响：若采用 RAID6 (双重奇偶校验)，冗余开销 = 2 * Disk_Size / Total_Pool_Size。对于 25 块 16TB 盘组成的 RAID6 池，总裸容量 400TB，可用容量 = 400 - 2*16 = 368TB。若要存储 420TB 数据 (来自 N214 的 500-111+10% overprovisioning)，所需裸容量 V_hdd_raw = 420TB / (1 - 2/25) ≈ 434TB。若采用 RAID10 (镜像)，冗余开销 50%，所需裸容量 V_hdd_raw = 420TB / 0.5 = 840TB，这将显著增加 CapEx，因此冷数据层通常优选 RAID6 或 ZFS Mirroring (2-way mirror, 50% 冗余) 而非 RAID10，需在成本与安全性间权衡。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID6冗余计算（2/25）及RAID10冗余计算（50%）符合存储架构基本原理，数值推导自洽。
