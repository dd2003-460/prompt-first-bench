# N68: 存储容量 N_storage 的动态计算：N_storage = (Hot_Data_Size + Cold_Data_Size) * (1 + Hot_Spi

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别对应高投入（高命中率）和低投入（低成本）两个极端工作点，参数取值互斥且覆盖范围合理（3.6TB 和 1.08TB 均在父节点估算的 1.5-5TB 区间或附近，体现了参数的敏感性）。虽然本质上是同一公式的不同参数代入，但在架构设计中，这些‘工作点’代表了不同的设计决策维度（性能 vs 成本），因此不属于冗余，而是对设计空间的必要采样。）
