# N215: 工作点A（高性能/高成本）：采用全 NVMe SSD 存储，单位成本 C_ssd = ¥1.2/GB/月（含 IOPS 溢价）；若 N_storage = 3.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

工作点A（高性能/高成本）：采用全 NVMe SSD 存储，单位成本 C_ssd = ¥1.2/GB/月（含 IOPS 溢价）；若 N_storage = 3.6TB，月度存储成本 C_storage_total = 3600GB * 1.2 = ¥4,320/月；此配置支持 P99 延迟 < 10ms 的本地读取。

## Corrected Claim

工作点A（高性能/高成本）：采用全 NVMe SSD 存储，单位成本 C_ssd = ¥1.2/GB/月（含 IOPS 溢价）；若 N_storage = 3.6TB，月度存储成本 C_storage_total = 3600GB * 1.2 = ¥4,320/月；此配置支持 P99 延迟 < 10ms 的本地读取。

## Evidence

先验知识/题面给定，逻辑校验通过：3600GB * 1.2元/GB/月 = 4320元/月，计算无误；NVMe SSD 支持 P99 < 10ms 本地读取符合工程常识。

## Search Query

NVMe SSD cost per GB monthly 2024 data center
