# N144: RAID-6配置下的写惩罚（Write Penalty）对温数据更新的影响：RAID-6的写惩罚为4（读2旧数据+写2新数据+读2旧奇偶+写2新奇偶，简化为4倍

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

RAID-6配置下的写惩罚（Write Penalty）对温数据更新的影响：RAID-6的写惩罚为4（读2旧数据+写2新数据+读2旧奇偶+写2新奇偶，简化为4倍I/O），若温数据每日更新比例为5%（5TB/天），则每日额外I/O量 = 5TB * 4 = 20TB；这会导致SSD寿命（DWPD）加速消耗，若SSD DWPD=1，则每日写入20TB在128TB容量上占比15.6%，年均磨损 = 15.6% * 365 = 5694%，远超1年寿命，需修正为DWPD=10或降低更新频率，否则需增加SSD数量以摊薄写入负载。

## Corrected Claim

RAID-6配置下的写惩罚（Write Penalty）对温数据更新的影响：RAID-6的写惩罚为4（读2旧数据+写2新数据+读2旧奇偶+写2新奇偶，简化为4倍I/O），若温数据每日更新比例为5%（5TB/天），则每日额外I/O量 = 5TB * 4 = 20TB；这会导致SSD寿命（DWPD）加速消耗，若SSD DWPD=1，则每日写入20TB在128TB容量上占比15.6%，年均磨损 = 15.6% * 365 = 5694%，远超1年寿命，需修正为DWPD=10或降低更新频率，否则需增加SSD数量以摊薄写入负载。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-6写惩罚系数4符合标准定义；5TB*4=20TB计算正确；20TB/128TB≈15.6%占比计算正确；15.6%*365≈5694%年均磨损率推导符合DWPD定义逻辑。

## Search Query

RAID-6 write penalty SSD endurance DWPD calculation
