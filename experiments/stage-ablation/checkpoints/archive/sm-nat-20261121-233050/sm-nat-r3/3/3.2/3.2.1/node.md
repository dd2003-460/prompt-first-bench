# N43: 在 M/C = 1.0 的工作点下，由于缓存容量等于总数据量，LRU 和 LFU 均能缓存所有 10 万对象，因此 H_LFU = H_LRU = 1.0，最大

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

在 M/C = 1.0 的工作点下，由于缓存容量等于总数据量，LRU 和 LFU 均能缓存所有 10 万对象，因此 H_LFU = H_LRU = 1.0，最大增益 ΔH = 0 百分点。

## Corrected Claim

在 M/C = 1.0 的工作点下，由于缓存容量等于总数据量，LRU 和 LFU 均能缓存所有 10 万对象，因此 H_LFU = H_LRU = 1.0，最大增益 ΔH = 0 百分点。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量等于总数据量时，LRU和LFU均可缓存所有对象，命中率均为1.0，增益为0。
