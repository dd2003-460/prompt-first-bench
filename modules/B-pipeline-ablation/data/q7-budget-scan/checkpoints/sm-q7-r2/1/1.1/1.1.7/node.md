# N40: SSD层RAID10冗余系数：物理容量/逻辑容量 = 2.0（固定），因RAID10采用镜像+条带化，有效容量为标称容量的50%；该系数需计入SSD层总成本，与

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

SSD层RAID10冗余系数：物理容量/逻辑容量 = 2.0（固定），因RAID10采用镜像+条带化，有效容量为标称容量的50%；该系数需计入SSD层总成本，与P_SSD相乘

## Corrected Claim

SSD层RAID10冗余系数：物理容量/逻辑容量 = 2.0（固定），因RAID10采用镜像+条带化，有效容量为标称容量的50%；该系数需计入SSD层总成本，与P_SSD相乘

## Evidence

先验知识/题面给定，逻辑校验通过：RAID10由镜像（2倍冗余）和条带化组成，其有效容量确实为物理总容量的50%，即冗余系数为2.0，符合存储工程基本原理。
