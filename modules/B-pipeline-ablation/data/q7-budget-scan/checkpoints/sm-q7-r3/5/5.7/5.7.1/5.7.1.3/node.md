# N312: 本地 NVMe SSD 阵列生命周期管理成本中，监控告警阈值设为 IOPS 低于基准 70% 触发，该参数基于 RAID 6 重建期间 IOPS 下降 30%-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

本地 NVMe SSD 阵列生命周期管理成本中，监控告警阈值设为 IOPS 低于基准 70% 触发，该参数基于 RAID 6 重建期间 IOPS 下降 30%-50% 的假设，若实际 IOPS 波动超出该范围，告警灵敏度需重新校准。

## Corrected Claim

本地 NVMe SSD 阵列生命周期管理成本中，监控告警阈值设为 IOPS 低于基准 70% 触发，该参数基于 RAID 6 重建期间 IOPS 下降 30%-50% 的假设，若实际 IOPS 波动超出该范围，告警灵敏度需重新校准。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RAID rebuild IOPS monitoring alert threshold best practice
