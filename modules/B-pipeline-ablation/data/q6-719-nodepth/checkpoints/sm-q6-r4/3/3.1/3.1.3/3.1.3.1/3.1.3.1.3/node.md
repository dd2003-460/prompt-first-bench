# N640: 工作点A（高缓存命中率）的存储溢出风险：当突发热点导致热数据量超过3.6TB时，缓存命中率H_A将下降，假设每溢出100GB，H_A下降1%，则H_A = 0.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N213

## Claim

工作点A（高缓存命中率）的存储溢出风险：当突发热点导致热数据量超过3.6TB时，缓存命中率H_A将下降，假设每溢出100GB，H_A下降1%，则H_A = 0.92 - (Overflow_GB / 100) * 0.01；需设置监控阈值，当Overflow_GB > 200GB时触发告警，并动态调整Hot_Spillover_Ratio或增加存储。

## Corrected Claim

工作点A（高缓存命中率）的存储溢出风险：当突发热点导致热数据量超过3.6TB时，缓存命中率H_A将下降，假设每溢出100GB，H_A下降1%，则H_A = 0.92 - (Overflow_GB / 100) * 0.01；需设置监控阈值，当Overflow_GB > 200GB时触发告警，并动态调整Hot_Spillover_Ratio或增加存储。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cdn cache overflow hit rate degradation dynamic storage adjustment
