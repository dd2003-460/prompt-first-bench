# N9: LRU 稳态字节命中率下界的理论下界公式：HitRate_LRU >= 1 - (TotalByteMiss / TotalByteRequest)，其中 To

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LRU 稳态字节命中率下界的理论下界公式：HitRate_LRU >= 1 - (TotalByteMiss / TotalByteRequest)，其中 TotalByteMiss 由 LRU 缓存替换策略下的驱逐字节数决定，需通过工作集大小与缓存容量的比值估算

## Corrected Claim

LRU 稳态字节命中率下界的理论下界公式：HitRate_LRU >= 1 - (TotalByteMiss / TotalByteRequest)，其中 TotalByteMiss 由 LRU 缓存替换策略下的驱逐字节数决定，需通过工作集大小与缓存容量的比值估算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache hit rate lower bound formula steady state
