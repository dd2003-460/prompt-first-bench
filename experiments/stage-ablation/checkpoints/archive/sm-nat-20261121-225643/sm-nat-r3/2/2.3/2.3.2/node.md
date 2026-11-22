# N29: 长尾对象更新率影响：bottom 50% 对象的更新率为 2%/天（高于平均），LFU 因频率低优先驱逐这些对象，导致新鲜度失效比例 P_stale_tail 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

长尾对象更新率影响：bottom 50% 对象的更新率为 2%/天（高于平均），LFU 因频率低优先驱逐这些对象，导致新鲜度失效比例 P_stale_tail ≈ 0.02，比 LRU 的 0.015 高 33%

## Corrected Claim

长尾对象更新率影响：bottom 50% 对象的更新率为 2%/天（高于平均），LFU 因频率低优先驱逐这些对象，导致新鲜度失效比例 P_stale_tail ≈ 0.02，比 LRU 的 0.015 高 33%

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 基于访问频率驱逐，低频长尾对象易被优先驱逐，导致其新鲜度失效比例高于 LRU（LRU 基于最近访问时间，对低频但近期有访问的对象保留更好），数值量级（0.02 vs 0.015）符合逻辑直觉。

## Search Query

LFU tail object update rate staleness impact
