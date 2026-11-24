# N94: HDD 硬件成本的分项构成：总成本 $C_{hdd} = C_{hdd_drives} + C_{controller} + C_{chassis}$；其中 $

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

HDD 硬件成本的分项构成：总成本 $C_{hdd} = C_{hdd_drives} + C_{controller} + C_{chassis}$；其中 $C_{hdd_drives}$ 为盘体成本（$0.02-0.03/GB$），$C_{controller}$ 为 RAID 控制器成本（约 $1,500-3,000$ 美元），$C_{chassis}$ 为机架式存储机箱成本（约 $5,000-10,000$ 美元/机柜，含电源、风扇、管理模块）；对于 2 节点集群，非盘体固定成本约为 $15,000-20,000$ 美元，占总硬件成本的 30%-40%，显著高于 NVMe 方案

## Corrected Claim

HDD 硬件成本的分项构成：总成本 $C_{hdd} = C_{hdd_drives} + C_{controller} + C_{chassis}$；其中 $C_{hdd_drives}$ 为盘体成本（$0.02-0.03/GB$），$C_{controller}$ 为 RAID 控制器成本（约 $1,500-3,000$ 美元），$C_{chassis}$ 为机架式存储机箱成本（约 $5,000-10,000$ 美元/机柜，含电源、风扇、管理模块）；对于 2 节点集群，非盘体固定成本约为 $15,000-20,000$ 美元，占总硬件成本的 30%-40%，显著高于 NVMe 方案

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

HDD storage array hardware cost breakdown chassis controller overhead
