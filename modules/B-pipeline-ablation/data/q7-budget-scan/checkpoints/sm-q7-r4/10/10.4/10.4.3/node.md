# N408: 数据量 < 100TB 且 IOPS > 100,000 场景下 HDD+SSD 方案的瓶颈：HDD 层 IOPS 上限 ~200/盘，即使 40 块 HDD 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N154

## Claim

数据量 < 100TB 且 IOPS > 100,000 场景下 HDD+SSD 方案的瓶颈：HDD 层 IOPS 上限 ~200/盘，即使 40 块 HDD 并行，总 IOPS ~8,000，远低于 100,000 需求，必须依赖 SSD 层缓存；若 SSD 层容量 < 100TB，缓存命中率需 > 90% 才能将 HDD 负载降至 < 10,000 IOPS，否则 HDD 成为瓶颈，导致整体 IOPS 无法满足，故 HDD+SSD 方案在此场景下需配置大容量 SSD，成本接近纯 NVMe 方案。

## Corrected Claim

数据量 < 100TB 且 IOPS > 100,000 场景下 HDD+SSD 方案的瓶颈：HDD 层 IOPS 上限 ~200/盘，即使 40 块 HDD 并行，总 IOPS ~8,000，远低于 100,000 需求，必须依赖 SSD 层缓存；若 SSD 层容量 < 100TB，缓存命中率需 > 90% 才能将 HDD 负载降至 < 10,000 IOPS，否则 HDD 成为瓶颈，导致整体 IOPS 无法满足，故 HDD+SSD 方案在此场景下需配置大容量 SSD，成本接近纯 NVMe 方案。

## Evidence

先验知识/题面给定，逻辑校验通过：HDD单盘IOPS约200，40盘并行约8000，远低于100,000需求；若SSD缓存命中率>90%，HDD负载降至<10,000 IOPS，逻辑自洽且数值量级合理。

## Search Query

HDD IOPS limit SSD cache hit ratio requirement
