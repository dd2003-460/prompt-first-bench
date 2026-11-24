# N8: HDD+SSD分层方案中，HDD部分采用RAID-6（假设12盘组，2盘冗余），有效容量系数 = (12-2)/12 ≈ 83.3%；SSD部分采用RAID-1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

HDD+SSD分层方案中，HDD部分采用RAID-6（假设12盘组，2盘冗余），有效容量系数 = (12-2)/12 ≈ 83.3%；SSD部分采用RAID-10或无冗余（若依赖上层纠删），系数不同。需分别计算热层（SSD）和冷层（HDD）的有效容量系数。

## Corrected Claim

HDD+SSD分层方案中，HDD部分采用RAID-6（假设12盘组，2盘冗余），有效容量系数 = (12-2)/12 ≈ 83.3%；SSD部分采用RAID-10或无冗余（若依赖上层纠删），系数不同。需分别计算热层（SSD）和冷层（HDD）的有效容量系数。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-6在12盘组中保留2盘冗余，有效容量系数(12-2)/12=83.3%符合定义；SSD部分RAID-10或无冗余的系数差异描述符合存储架构常识。

## Search Query

HDD RAID-6 effective capacity ratio 12 disk
