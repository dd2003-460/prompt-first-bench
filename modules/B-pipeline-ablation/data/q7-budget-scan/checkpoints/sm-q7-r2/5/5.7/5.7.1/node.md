# N108: 本地 NVMe SSD 阵列的生命周期管理成本主要体现为 RAID 重建期间的性能降级监控与 IOPS 损耗量化：假设 RAID 6 重建期间阵列有效 IOPS

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

本地 NVMe SSD 阵列的生命周期管理成本主要体现为 RAID 重建期间的性能降级监控与 IOPS 损耗量化：假设 RAID 6 重建期间阵列有效 IOPS 下降 30%-50%，重建时间 50-100 小时，需监控告警阈值设为 IOPS 低于基准 70% 触发，年运维人力成本约为 2 人 × 1 小时/月 × 12 月 × ¥100/小时 = ¥2,400（假设人工时薪 ¥100）

## Corrected Claim

本地 NVMe SSD 阵列的生命周期管理成本主要体现为 RAID 重建期间的性能降级监控与 IOPS 损耗量化：假设 RAID 6 重建期间阵列有效 IOPS 下降 30%-50%，重建时间 50-100 小时，需监控告警阈值设为 IOPS 低于基准 70% 触发，年运维人力成本约为 2 人 × 1 小时/月 × 12 月 × ¥100/小时 = ¥2,400（假设人工时薪 ¥100）

## Evidence

先验知识/题面给定，逻辑校验通过：RAID 6 重建期间性能下降 30%-50% 符合工程经验；重建时间 50-100 小时对于大容量 NVMe 阵列合理；告警阈值设为基准 70% 与 30% 的性能下降下限对应，逻辑自洽；人力成本计算 2*1*12*100=2400 数学正确。

## Search Query

RAID rebuild performance degradation monitoring cost
