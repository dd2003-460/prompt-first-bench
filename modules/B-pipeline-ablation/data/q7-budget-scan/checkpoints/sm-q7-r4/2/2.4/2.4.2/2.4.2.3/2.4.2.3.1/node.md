# N582: N194中SSD静态功耗假设0.5W/TB与N385中NVMe SSD典型静态功耗5-10W/盘（2TB盘即2.5-5W/TB）严重不符；若采用2TB NVMe

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N194

## Claim

N194中SSD静态功耗假设0.5W/TB与N385中NVMe SSD典型静态功耗5-10W/盘（2TB盘即2.5-5W/TB）严重不符；若采用2TB NVMe SSD，100TB温数据需50块盘，静态功耗应为 50盘 × 5W/盘 = 250W，而非 100TB × 0.5W/TB = 50W。

## Corrected Claim

N194中SSD静态功耗假设0.5W/TB与N385中NVMe SSD典型静态功耗5-10W/盘（2TB盘即2.5-5W/TB）严重不符；若采用2TB NVMe SSD，100TB温数据需50块盘，静态功耗应为 50盘 × 5W/盘 = 250W，而非 100TB × 0.5W/TB = 50W。

## Evidence

先验知识/题面给定，逻辑校验通过：0.5W/TB与5-10W/盘(2TB)的量级差异及功耗计算(250W vs 50W)符合物理直觉与算术逻辑

## Search Query

NVMe SSD idle power consumption watts per TB
