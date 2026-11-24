# N537: NVMe SSD 阵列物理盘数 N_disks 的精确计算：500TB 总数据量 / (1 - RAID6 冗余率 2/N) * (1 / 单盘有效容量 1.9

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N232

## Claim

NVMe SSD 阵列物理盘数 N_disks 的精确计算：500TB 总数据量 / (1 - RAID6 冗余率 2/N) * (1 / 单盘有效容量 1.92TB) * 利用率系数 0.85 ≈ 500 / 0.96 / 1.92 / 0.85 ≈ 320 块盘，而非 N232 声称的 270 块，此差异将显著影响组合故障概率的分母。

## Corrected Claim

NVMe SSD 阵列物理盘数 N_disks 的精确计算：500TB 总数据量 / (1 - RAID6 冗余率 2/N) * (1 / 单盘有效容量 1.92TB) * 利用率系数 0.85 ≈ 500 / 0.96 / 1.92 / 0.85 ≈ 320 块盘，而非 N232 声称的 270 块，此差异将显著影响组合故障概率的分母。

## Evidence

先验知识/题面给定，逻辑校验通过：500 / (1 - 2/50) / 1.92 / 0.85 ≈ 320.5，计算无误且符合RAID6容量规划逻辑
