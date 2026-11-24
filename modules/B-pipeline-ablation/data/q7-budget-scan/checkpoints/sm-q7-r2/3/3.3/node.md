# N20: HDD+SSD分层方案带宽：SSD层200TB裸容量，假设单块SSD为5TB，共40块，总带宽 = 40 * 5GB/s = 200GB/s，远超温数据需求（1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

HDD+SSD分层方案带宽：SSD层200TB裸容量，假设单块SSD为5TB，共40块，总带宽 = 40 * 5GB/s = 200GB/s，远超温数据需求（1.2-2.3GB/s），可行性高。

## Corrected Claim

HDD+SSD分层方案带宽：SSD层200TB裸容量，假设单块SSD为5TB，共40块，总带宽 = 40 * 5GB/s = 200GB/s，远超温数据需求（1.2-2.3GB/s），可行性高。

## Evidence

先验知识/题面给定，逻辑校验通过：40块5TB SSD总容量200TB，单块5GB/s带宽乘以40块等于200GB/s，远超1.2-2.3GB/s需求，计算与量级均合理。

## Search Query

SSD sequential read bandwidth 5TB
