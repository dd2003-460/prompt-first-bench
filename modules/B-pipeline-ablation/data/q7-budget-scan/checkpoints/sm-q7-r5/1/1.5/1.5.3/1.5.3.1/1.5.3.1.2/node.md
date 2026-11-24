# N383: 工作点B（N=24）单组RAID6故障重建时间 T_rebuild_group：假设单盘故障，需重建16TB数据，T = 16000GB / 0.2GB/s /

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N170

## Claim

工作点B（N=24）单组RAID6故障重建时间 T_rebuild_group：假设单盘故障，需重建16TB数据，T = 16000GB / 0.2GB/s / 3600 ≈ 22.2小时；若双盘故障（RAID6容忍），重建32TB，T ≈ 44.4小时

## Corrected Claim

工作点B（N=24）单组RAID6故障重建时间 T_rebuild_group：假设单盘故障，需重建16TB数据，T = 16000GB / 0.2GB/s / 3600 ≈ 22.2小时；若双盘故障（RAID6容忍），重建32TB，T ≈ 44.4小时

## Evidence

先验知识/题面给定，逻辑校验通过：16000GB/0.2GB/s=80000s≈22.2h，32000GB/0.2GB/s=160000s≈44.4h，计算无误。
