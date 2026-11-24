# N94: 本地 NVMe SSD 扩容的停机迁移时间 Downtime_Hours 等于 迁移数据量 (Migration_Data_Size) 除以 迁移吞吐量 (Mi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

本地 NVMe SSD 扩容的停机迁移时间 Downtime_Hours 等于 迁移数据量 (Migration_Data_Size) 除以 迁移吞吐量 (Migration_Throughput)，假设迁移 100TB 数据，吞吐量 500MB/s，则 Downtime = 100*1024^3 / 500 / 3600 小时。

## Corrected Claim

本地 NVMe SSD 扩容的停机迁移时间 Downtime_Hours 等于 迁移数据量 (Migration_Data_Size) 除以 迁移吞吐量 (Migration_Throughput)，假设迁移 100TB 数据，吞吐量 500MB/s，则 Downtime = 100*1024^3 / 500 / 3600 小时。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Downtime = Data_Size / Throughput 符合物理定义，单位换算（TB转Byte，s转h）正确，计算过程自洽。
