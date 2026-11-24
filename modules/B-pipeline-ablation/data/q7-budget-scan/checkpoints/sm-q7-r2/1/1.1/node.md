# N7: 本地 NVMe SSD 阵列的冗余系数 R_raid = 1 + 1/N，其中 N 为 RAID5/6 或纠删码的磁盘数，典型值 1.1-1.25

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

本地 NVMe SSD 阵列的冗余系数 R_raid = 1 + 1/N，其中 N 为 RAID5/6 或纠删码的磁盘数，典型值 1.1-1.25

## Corrected Claim

本地 NVMe SSD 阵列的冗余系数 R_raid = 1 + 1/N，其中 N 为 RAID5/6 或纠删码的磁盘数，典型值 1.1-1.25

## Evidence

父节点级核验未通过：不完备（父节点定义了通用公式 R=1+1/N 及典型值范围（1.1-1.25），而唯一的子节点仅给出了一个特定配置（N=6, R=1.33）的实例。首先，子节点的 R 值（1.33）超出了父节点定义的典型值上限（1.25），存在潜在矛盾或范围未覆盖；其次，子节点未涵盖 RAID5/RAID6 等其他常见配置，也未解释为何典型值仅到 1.25 而该实例为 1.33，导致对父节点中'典型值'和'RAID5/6'部分的覆盖不全。）
