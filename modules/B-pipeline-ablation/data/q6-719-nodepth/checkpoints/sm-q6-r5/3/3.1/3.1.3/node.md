# N68: 存储容量 N_storage 的动态计算：N_storage = (Hot_Data_Size + Cold_Data_Size) * (1 + Hot_Spi

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

存储容量 N_storage 的动态计算：N_storage = (Hot_Data_Size + Cold_Data_Size) * (1 + Hot_Spillover_Ratio)，其中 Hot_Data_Size 为热数据量（日均2TB下载量中需缓存的Top N对象，假设占下载量20%即400GB/天，保留3天热数据约1.2TB），Cold_Data_Size 为冷数据量（非缓存内容，通常不存储在边缘，仅源站存储），Hot_Spillover_Ratio 为缓存溢出冗余系数（通常1.2-1.5，应对突发热点）；边缘节点存储通常仅保留热数据，故 N_storage ≈ 1.5TB - 5TB。

## Corrected Claim

存储容量 N_storage 的动态计算：N_storage = (Hot_Data_Size + Cold_Data_Size) * (1 + Hot_Spillover_Ratio)，其中 Hot_Data_Size 为热数据量（日均2TB下载量中需缓存的Top N对象，假设占下载量20%即400GB/天，保留3天热数据约1.2TB），Cold_Data_Size 为冷数据量（非缓存内容，通常不存储在边缘，仅源站存储），Hot_Spillover_Ratio 为缓存溢出冗余系数（通常1.2-1.5，应对突发热点）；边缘节点存储通常仅保留热数据，故 N_storage ≈ 1.5TB - 5TB。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数取值下的两个实例，而非独立的逻辑分支（存在冗余）。此外，父节点明确给出了N_storage的估算范围（1.5TB-5TB），但子节点B的计算结果（1.08TB）低于该下限，导致子节点未能覆盖父节点定义的完整参数空间或存在数值矛盾。）
