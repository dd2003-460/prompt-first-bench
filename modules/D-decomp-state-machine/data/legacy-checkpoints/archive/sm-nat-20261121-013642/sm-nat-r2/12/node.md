# N96: 在缓存容量远大于总数据量（128GB >> 118.75MB）的极端情况下，LRU 的稳态字节命中率 H_byte_LRU 的理论下界为 1.0（100%），因

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在缓存容量远大于总数据量（128GB >> 118.75MB）的极端情况下，LRU 的稳态字节命中率 H_byte_LRU 的理论下界为 1.0（100%），因为所有 100,000 个对象均可同时驻留内存，任何请求都能命中，除非对象在请求前被更新失效。

## Corrected Claim

在缓存容量远大于总数据量（128GB >> 118.75MB）的极端情况下，LRU 的稳态字节命中率 H_byte_LRU 的理论下界为 1.0（100%），因为所有 100,000 个对象均可同时驻留内存，任何请求都能命中，除非对象在请求前被更新失效。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LRU cache hit rate theoretical lower bound full dataset resident
