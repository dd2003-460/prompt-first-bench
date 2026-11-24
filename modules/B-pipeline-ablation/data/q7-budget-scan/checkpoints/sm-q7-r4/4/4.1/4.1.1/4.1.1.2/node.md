# N194: I/O 抑制因子（Throttling Factor）随 RAID 级别和盘数变化：RAID5 重建时因子约为 20%-30%，RAID6 约为 30%-50%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

I/O 抑制因子（Throttling Factor）随 RAID 级别和盘数变化：RAID5 重建时因子约为 20%-30%，RAID6 约为 30%-50%，RAID10 约为 10%-20%；该因子直接影响 RTO 期间可接受的并发业务请求上限。

## Corrected Claim

I/O 抑制因子（Throttling Factor）随 RAID 级别和盘数变化：RAID5 重建时因子约为 20%-30%，RAID6 约为 30%-50%，RAID10 约为 10%-20%；该因子直接影响 RTO 期间可接受的并发业务请求上限。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RAID level IO throttling factor comparison RAID5 RAID6 RAID10 performance degradation
