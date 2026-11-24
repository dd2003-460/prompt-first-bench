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

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了父节点中的两个核心维度：成本计算和性能指标（延迟）。两者内容不重叠，且共同构成了对“高性能/高成本”工作点的完整描述，没有遗漏父节点中的关键信息，也不存在冗余。）

## Search Query

NVMe SSD cost per GB monthly 2024 data center
