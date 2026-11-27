# N11: LFU 性能增益上限机制：LFU 保留高频访问对象，不受最近访问干扰。在负相关负载下，LFU 更倾向于保留热门小对象，但可能忽略偶尔访问的大对象，导致字节命中率

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LFU 性能增益上限机制：LFU 保留高频访问对象，不受最近访问干扰。在负相关负载下，LFU 更倾向于保留热门小对象，但可能忽略偶尔访问的大对象，导致字节命中率提升有限。需量化 LFU 与 LRU 在 Cache 集合差异上的字节命中率差值 ΔH = H_byte_LFU - H_byte_LRU。

## Corrected Claim

LFU 性能增益上限机制：LFU 保留高频访问对象，不受最近访问干扰。在负相关负载下，LFU 更倾向于保留热门小对象，但可能忽略偶尔访问的大对象，导致字节命中率提升有限。需量化 LFU 与 LRU 在 Cache 集合差异上的字节命中率差值 ΔH = H_byte_LFU - H_byte_LRU。

## Evidence

先验知识/题面给定，逻辑校验通过
