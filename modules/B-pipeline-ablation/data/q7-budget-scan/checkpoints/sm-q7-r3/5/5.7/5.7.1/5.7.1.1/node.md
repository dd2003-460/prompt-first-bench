# N310: 本地 NVMe SSD 阵列生命周期管理成本中，RAID 6 重建期间有效 IOPS 下降幅度假设为 30%-50%，该参数决定性能降级监控告警阈值（基准 IO

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

本地 NVMe SSD 阵列生命周期管理成本中，RAID 6 重建期间有效 IOPS 下降幅度假设为 30%-50%，该参数决定性能降级监控告警阈值（基准 IOPS × 70%），若实际下降幅度偏离该区间，监控策略需调整。

## Corrected Claim

本地 NVMe SSD 阵列生命周期管理成本中，RAID 6 重建期间有效 IOPS 下降幅度假设为 30%-50%，该参数决定性能降级监控告警阈值（基准 IOPS × 70%），若实际下降幅度偏离该区间，监控策略需调整。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RAID 6 rebuild performance degradation IOPS drop percentage NVMe SSD
