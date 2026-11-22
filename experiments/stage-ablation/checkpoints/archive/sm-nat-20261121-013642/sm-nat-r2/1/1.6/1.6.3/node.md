# N48: 缓存集合差异量化：ΔCache = |Cache_LFU \ Cache_LRU|，即 LFU 缓存中有但 LRU 缓存中没有的对象数量，这些对象通常是低频但较

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

缓存集合差异量化：ΔCache = |Cache_LFU \ Cache_LRU|，即 LFU 缓存中有但 LRU 缓存中没有的对象数量，这些对象通常是低频但较大的对象，需计算 ΔCache 中对象的总字节流量占比。

## Corrected Claim

缓存集合差异量化：ΔCache = |Cache_LFU \ Cache_LRU|，即 LFU 缓存中有但 LRU 缓存中没有的对象数量，这些对象通常是低频但较大的对象，需计算 ΔCache 中对象的总字节流量占比。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache set difference LFU LRU byte traffic contribution
