# N104: HDD+SSD 分层方案中，新增 2,440 TB HDD 的年运维备件成本 (¥/年) = 2,440 TB / 16 TB/disk × 152.5 dis

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

HDD+SSD 分层方案中，新增 2,440 TB HDD 的年运维备件成本 (¥/年) = 2,440 TB / 16 TB/disk × 152.5 disks × (2.25% AFR × ¥650/disk)，约 ¥24,800/年

## Corrected Claim

HDD+SSD 分层方案中，新增 2,440 TB HDD 的年运维备件成本 (¥/年) = (2,440 TB / 16 TB/disk) × (2.25% AFR × ¥650/disk)，约 ¥162.6/年

## Evidence

[质询]计算逻辑存在严重内部矛盾：公式中 '2,440 TB / 16 TB/disk' 已计算出磁盘数量（152.5），但随后又乘以 '152.5 disks'，导致磁盘数量被重复计算（平方），使得最终成本结果比正确值高约152.5倍。 | 逻辑校验失败：公式结构错误，(Total Capacity / Capacity per Disk) * (Disk Count) 导致量纲和数值错误，正确公式应为 (Total Capacity / Capacity per Disk) * (AFR * Cost per Disk)。

## Search Query

enterprise hdd annual failure rate
