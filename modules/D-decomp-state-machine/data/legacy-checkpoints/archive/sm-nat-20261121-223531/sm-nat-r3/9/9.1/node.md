# N79: LFU 增益为零的边界条件量化：当缓存容量 C ≥ S_total（1.15GB）时，LRU 和 LFU 均能缓存所有对象，稳态字节命中率均为 100%（忽略更

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

LFU 增益为零的边界条件量化：当缓存容量 C ≥ S_total（1.15GB）时，LRU 和 LFU 均能缓存所有对象，稳态字节命中率均为 100%（忽略更新），因此 ΔH = 0 百分点。

## Corrected Claim

LFU 增益为零的边界条件量化：当缓存容量 C ≥ S_total（1.15GB）时，LRU 和 LFU 均能缓存所有对象，稳态字节命中率均为 100%（忽略更新），因此 ΔH = 0 百分点。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量大于等于工作集大小时，LRU和LFU均能容纳所有对象，命中率均为100%，差值为0，符合缓存基本原理。
