# N390: 修正N69 vs N85矛盾后的RAID6重建时间通用公式：T_rebuild = (Data_Size_to_Rebuild_GB) / (Bottlenec

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N172

## Claim

修正N69 vs N85矛盾后的RAID6重建时间通用公式：T_rebuild = (Data_Size_to_Rebuild_GB) / (Bottleneck_Write_Bandwidth_GBps) / 3600，其中 Bottleneck_Write_Bandwidth_GBps = min(Drive_Write_Speed, Controller_Max_Throughput)，对于HDD RAID6，瓶颈通常为单盘写速

## Corrected Claim

修正N69 vs N85矛盾后的RAID6重建时间通用公式：T_rebuild = (Data_Size_to_Rebuild_GB) / (Bottleneck_Write_Bandwidth_GBps) / 3600，其中 Bottleneck_Write_Bandwidth_GBps = min(Drive_Write_Speed, Controller_Max_Throughput)，对于HDD RAID6，瓶颈通常为单盘写速

## Evidence

先验知识/题面给定，逻辑校验通过：RAID6重建需读取所有存活数据并计算奇偶校验，写入新盘，瓶颈通常受限于单盘写带宽（HDD场景），公式量纲正确（GB/GBps=秒，除以3600转小时），符合存储系统基本原理。
