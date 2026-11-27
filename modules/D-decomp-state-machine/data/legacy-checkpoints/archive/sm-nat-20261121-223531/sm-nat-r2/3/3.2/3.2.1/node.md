# N46: 在 N24 确认的容量充足前提下，LFU 完美保留 top-K% 对象（K=100%）的命中率 H_LFU_top = 100%，与 LRU 命中率相同，因此 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

在 N24 确认的容量充足前提下，LFU 完美保留 top-K% 对象（K=100%）的命中率 H_LFU_top = 100%，与 LRU 命中率相同，因此 LFU 相对增益 ΔH = 0 百分点。

## Corrected Claim

在 N24 确认的容量充足前提下，LFU 完美保留 top-K% 对象（K=100%）的命中率 H_LFU_top = 100%，与 LRU 命中率相同，因此 LFU 相对增益 ΔH = 0 百分点。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量足以容纳所有对象（K=100%）时，任何缓存策略（包括LFU和LRU）的命中率均为100%，因此相对增益为0。
