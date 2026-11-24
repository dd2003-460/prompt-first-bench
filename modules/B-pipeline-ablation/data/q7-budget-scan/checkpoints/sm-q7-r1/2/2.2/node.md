# N14: HDD+SSD分层有效容量 = 100TB * (1 - 0.30) + 400TB * (1 - 0.10) = 70TB + 360TB = 430TB，其

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

HDD+SSD分层有效容量 = 100TB * (1 - 0.30) + 400TB * (1 - 0.10) = 70TB + 360TB = 430TB，其中SSD层损耗30%（RAID10+元数据），HDD层损耗10%（RAID5+元数据）

## Corrected Claim

HDD+SSD分层有效容量 = 100TB * (1 - 0.30) + 400TB * (1 - 0.10) = 70TB + 360TB = 430TB，其中SSD层损耗30%（RAID10+元数据），HDD层损耗10%（RAID5+元数据）

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（100*0.7=70, 400*0.9=360, 70+360=430），损耗率设定符合RAID10/RAID5及元数据开销的工程常识量级。

## Search Query

tiered storage usable capacity SSD RAID10 HDD RAID5 overhead
