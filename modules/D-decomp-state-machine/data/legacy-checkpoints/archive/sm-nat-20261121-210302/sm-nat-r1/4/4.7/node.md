# N15: LFU 提升的瓶颈约束：LFU 对长尾对象适应差，当对象更新率非零时 LFU 可能滞留过期对象，提升上限受限于热点集合的字节占比与缓存容量的比值，需计算热点集合

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LFU 提升的瓶颈约束：LFU 对长尾对象适应差，当对象更新率非零时 LFU 可能滞留过期对象，提升上限受限于热点集合的字节占比与缓存容量的比值，需计算热点集合字节占比 P_hot_bytes = Sum(S_i for i in HotSet) / TotalBytes

## Corrected Claim

LFU 提升的瓶颈约束：LFU 对长尾对象适应差，当对象更新率非零时 LFU 可能滞留过期对象，提升上限受限于热点集合的字节占比与缓存容量的比值，需计算热点集合字节占比 P_hot_bytes = Sum(S_i for i in HotSet) / TotalBytes

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU cache long tail object update rate hit rate upper bound constraint
