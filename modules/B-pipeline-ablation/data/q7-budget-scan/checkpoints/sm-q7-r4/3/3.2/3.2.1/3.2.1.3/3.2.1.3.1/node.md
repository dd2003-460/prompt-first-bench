# N690: HDD+SSD分层方案中，RAID控制器及背板功耗的保守修正值 = 双控RAID卡(35W) + 背板/托架(25W) + 关联CPU/内存(60W) + 关联

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N255

## Claim

HDD+SSD分层方案中，RAID控制器及背板功耗的保守修正值 = 双控RAID卡(35W) + 背板/托架(25W) + 关联CPU/内存(60W) + 关联主板/PCIe(25W)，合计145W，替代原N255的60W估算

## Corrected Claim

HDD+SSD分层方案中，RAID控制器及背板功耗的保守修正值 = 双控RAID卡(35W) + 背板/托架(25W) + 关联CPU/内存(60W) + 关联主板/PCIe(25W)，合计145W，替代原N255的60W估算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

enterprise RAID controller backplane power consumption typical values
