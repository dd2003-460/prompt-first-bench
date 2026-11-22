# N112: LFU 相比 LRU 的增益上限并非由‘头部对象请求占比’直接决定，而是由‘LRU 因时间局部性缺失而驱逐的头部对象字节占比’决定。在全量驻留（$K_{cap}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

LFU 相比 LRU 的增益上限并非由‘头部对象请求占比’直接决定，而是由‘LRU 因时间局部性缺失而驱逐的头部对象字节占比’决定。在全量驻留（$K_{cap} > N_{obj}$）的前提下，LRU 和 LFU 均保留所有对象，因此 LFU 的增益为 0 个百分点，N47 声称的‘理论上界约 91% 命中率增益’仅在缓存容量受限（$K_{cap} < N_{obj}$）且负载极度偏斜时才可能接近，但在本题参数下（全量驻留），该增益为 0。

## Corrected Claim

LFU 相比 LRU 的增益上限并非由‘头部对象请求占比’直接决定，而是由‘LRU 因时间局部性缺失而驱逐的头部对象字节占比’决定。在全量驻留（$K_{cap} > N_{obj}$）的前提下，LRU 和 LFU 均保留所有对象，因此 LFU 的增益为 0 个百分点，N47 声称的‘理论上界约 91% 命中率增益’仅在缓存容量受限（$K_{cap} < N_{obj}$）且负载极度偏斜时才可能接近，但在本题参数下（全量驻留），该增益为 0。

## Evidence

先验知识/题面给定，逻辑校验通过：在全量驻留（缓存容量大于对象总数）条件下，LRU和LFU均不会发生驱逐，命中率均为100%，因此LFU相对于LRU的增益确实为0。

## Search Query

LFU vs LRU gain full cache scenario
