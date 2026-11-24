# N49: SSD 热层冗余策略选择：若采用 RAID-10，Usable_Factor_SSD = 0.5，需裸容量 200TB；若采用分布式纠删码（如 Ceph EC 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

SSD 热层冗余策略选择：若采用 RAID-10，Usable_Factor_SSD = 0.5，需裸容量 200TB；若采用分布式纠删码（如 Ceph EC 4+2），Usable_Factor_SSD = 4/6 ≈ 66.7%，需裸容量 150TB，两种策略的容量效率差异显著影响硬件采购成本。

## Corrected Claim

SSD 热层冗余策略选择：若采用 RAID-10，Usable_Factor_SSD = 0.5，需裸容量 200TB；若采用分布式纠删码（如 Ceph EC 4+2），Usable_Factor_SSD = 4/6 ≈ 66.7%，需裸容量 150TB，两种策略的容量效率差异显著影响硬件采购成本。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-10 冗余因子为 0.5，Ceph EC 4+2 可用因子为 4/6，数值计算与存储原理一致。
