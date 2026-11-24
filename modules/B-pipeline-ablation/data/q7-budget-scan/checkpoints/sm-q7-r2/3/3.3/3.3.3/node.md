# N96: 500TB总容量单点故障域约束：本地NVMe SSD阵列RAID-10单故障域=1块SSD，HDD+SSD分层HDD部分RAID-6单故障域=2块HDD，SSD

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

500TB总容量单点故障域约束：本地NVMe SSD阵列RAID-10单故障域=1块SSD，HDD+SSD分层HDD部分RAID-6单故障域=2块HDD，SSD部分RAID-10单故障域=1块SSD，云存储单点故障域=对象级别（自动多副本），需评估单点故障对业务的影响程度，若业务要求<1分钟故障切换，云存储最优

## Corrected Claim

500TB总容量单点故障域约束：本地NVMe SSD阵列RAID-10单故障域=1块SSD，HDD+SSD分层HDD部分RAID-6单故障域=2块HDD，SSD部分RAID-10单故障域=1块SSD，云存储单点故障域=对象级别（自动多副本），需评估单点故障对业务的影响程度，若业务要求<1分钟故障切换，云存储最优

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-10允许单盘故障，RAID-6允许双盘故障，云存储对象级多副本机制符合技术常识，且故障切换时间评估逻辑自洽。

## Search Query

RAID 10 RAID 6 failure domain single point of failure recovery time
