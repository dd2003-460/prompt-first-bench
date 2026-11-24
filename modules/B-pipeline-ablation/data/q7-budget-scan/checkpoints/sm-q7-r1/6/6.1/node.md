# N33: 有效可用容量换算系数：Raw_Capacity × Usable_Factor = Effective_Capacity，其中Usable_Factor因RAI

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

有效可用容量换算系数：Raw_Capacity × Usable_Factor = Effective_Capacity，其中Usable_Factor因RAID级别而异：RAID5 Usable_Factor = (N-1)/N，RAID6 = (N-2)/N，ZFS Mirror = 0.5，云存储无RAID开销但需考虑元数据开销（~2%~5%），典型值：本地RAID5 500TB raw → ~450TB effective，云存储500TB → ~480TB effective

## Corrected Claim

有效可用容量换算系数：Raw_Capacity × Usable_Factor = Effective_Capacity，其中Usable_Factor因RAID级别而异：RAID5 Usable_Factor = (N-1)/N，RAID6 = (N-2)/N，ZFS Mirror = 0.5，云存储无RAID开销但需考虑元数据开销（~2%~5%），典型值：本地RAID5 500TB raw → ~450TB effective，云存储500TB → ~480TB effective

## Evidence

先验知识/题面给定，逻辑校验通过：RAID5/6及Mirror的容量公式符合存储原理，500TB RAID5 (N=10假设) 得450TB及云存储扣除元数据后约480TB的数值量级合理且自洽。

## Search Query

RAID usable capacity factor
