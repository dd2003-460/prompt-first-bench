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

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于成本计算（财务维度），子节点2聚焦于延迟性能（技术维度），两者维度不同且无逻辑冲突，共同覆盖了父节点中关于‘高成本’和‘高性能’的两个核心属性，且各自独立完整，不存在冗余或重复。）

## Search Query

NVMe SSD cost per GB monthly 2024 data center
