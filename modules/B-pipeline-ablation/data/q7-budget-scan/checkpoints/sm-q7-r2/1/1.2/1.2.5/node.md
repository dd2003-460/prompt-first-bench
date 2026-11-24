# N48: SSD缓存层的吞吐需求验证：温数据100TB日扫1-2次，假设每次4小时，所需吞吐 = 100TB / 4h = 25TB/h ≈ 6.94GB/s；16块16

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

SSD缓存层的吞吐需求验证：温数据100TB日扫1-2次，假设每次4小时，所需吞吐 = 100TB / 4h = 25TB/h ≈ 6.94GB/s；16块16TB NVMe SSD单块吞吐≈7GB/s，总吞吐 = 16 * 7 = 112GB/s，远超6.94GB/s需求；即使考虑RAID10写放大，读吞吐不受影响，满足SLA。

## Corrected Claim

SSD缓存层的吞吐需求验证：温数据100TB日扫1-2次，假设每次4小时，所需吞吐 = 100TB / 4h = 25TB/h ≈ 6.94GB/s；16块16TB NVMe SSD单块吞吐≈7GB/s，总吞吐 = 16 * 7 = 112GB/s，远超6.94GB/s需求；即使考虑RAID10写放大，读吞吐不受影响，满足SLA。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（100TB/4h≈6.94GB/s，16*7GB/s=112GB/s），量级合理，RAID10读吞吐不受写放大影响的陈述符合存储原理。

## Search Query

NVMe SSD throughput 100TB daily scan 4 hours
