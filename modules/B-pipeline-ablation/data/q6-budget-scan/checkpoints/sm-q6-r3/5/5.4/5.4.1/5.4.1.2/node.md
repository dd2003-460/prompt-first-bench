# N257: 单节点存储容量 Cache_Capacity_Objects 的实际可用容量需扣除系统开销，公式为 Cache_Capacity_Objects = (Stor

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

单节点存储容量 Cache_Capacity_Objects 的实际可用容量需扣除系统开销，公式为 Cache_Capacity_Objects = (Storage_Total * (1 - f_overhead)) / s_avg，其中 f_overhead 为文件系统及元数据开销比例（通常5-10%）

## Corrected Claim

单节点存储容量 Cache_Capacity_Objects 的实际可用容量需扣除系统开销，公式为 Cache_Capacity_Objects = (Storage_Total * (1 - f_overhead)) / s_avg，其中 f_overhead 为文件系统及元数据开销比例（通常5-10%）

## Evidence

先验知识/题面给定，逻辑校验通过
