# N387: 工作点C（N=12）单组RAID6故障重建时间 T_rebuild_group：单盘故障重建16TB，T = 16000GB / 0.2GB/s / 3600 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N171

## Claim

工作点C（N=12）单组RAID6故障重建时间 T_rebuild_group：单盘故障重建16TB，T = 16000GB / 0.2GB/s / 3600 ≈ 22.2小时；双盘故障重建32TB，T ≈ 44.4小时。注意：虽然单组重建时间与N170相同，但N171的总盘数相同（48块），故障频率相同，但每组容量小，意味着更多组别，故障隔离性更好但总硬件成本更高

## Corrected Claim

工作点C（N=12）单组RAID6故障重建时间 T_rebuild_group：单盘故障重建16TB，T = 16000GB / 0.2GB/s / 3600 ≈ 22.2小时；双盘故障重建32TB，T ≈ 44.4小时。注意：虽然单组重建时间与N170相同，但N171的总盘数相同（48块），故障频率相同，但每组容量小，意味着更多组别，故障隔离性更好但总硬件成本更高

## Evidence

先验知识/题面给定，逻辑校验通过：16000GB/0.2GB/s/3600s/h ≈ 22.2h，32000GB/0.2GB/s/3600s/h ≈ 44.4h，计算无误且符合RAID6重建逻辑。
