# N8: HDD+SSD分层方案中，HDD部分采用RAID-6（假设12盘组，2盘冗余），有效容量系数 = (12-2)/12 ≈ 83.3%；SSD部分采用RAID-1

- **status**: pending
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

父节点级核验未通过：非正交, 有冗余（子节点3（总系数）是子节点1和2计算结果的线性组合与汇总，导致信息严重冗余；且子节点2内部混合了策略选择与具体数值计算，逻辑层级不清晰。）

## Search Query

HDD RAID-6 effective capacity ratio 12 disk
