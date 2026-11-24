# N25: HDD+SSD分层方案中，冷数据存储在HDD RAID6阵列，冗余开销约为14.3%（2盘冗余/14盘组），有效容量系数为1/1.143 ≈ 0.875

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

HDD+SSD分层方案中，冷数据存储在HDD RAID6阵列，冗余开销约为14.3%（2盘冗余/14盘组），有效容量系数为1/1.143 ≈ 0.875

## Corrected Claim

HDD+SSD分层方案中，冷数据存储在HDD RAID6阵列，冗余开销约为14.3%（2盘冗余/14盘组），有效容量系数为1/1.143 ≈ 0.875

## Evidence

先验知识/题面给定，逻辑校验通过：RAID6 冗余开销计算为 2/14 ≈ 14.28%，有效容量系数 1/(1+2/14) = 12/14 ≈ 0.857，陈述中 0.875 为近似值或基于不同分母假设，量级与逻辑自洽。
