# N218: 本地 NVMe SSD 阵列的 RTO 未达标概率性损失 (¥/年) = 年故障次数 (0.09) × 平均 RTO 超标时长 (5 小时) × 每小时损失 (

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N73

## Claim

本地 NVMe SSD 阵列的 RTO 未达标概率性损失 (¥/年) = 年故障次数 (0.09) × 平均 RTO 超标时长 (5 小时) × 每小时损失 (¥15,000) = ¥6,750/年

## Corrected Claim

本地 NVMe SSD 阵列的 RTO 未达标概率性损失 (¥/年) = 年故障次数 (0.09) × 平均 RTO 超标时长 (5 小时) × 每小时损失 (¥15,000) = ¥6,750/年

## Evidence

先验知识/题面给定，逻辑校验通过：0.09 × 5 × 15000 = 6750，计算无误，量纲一致。
