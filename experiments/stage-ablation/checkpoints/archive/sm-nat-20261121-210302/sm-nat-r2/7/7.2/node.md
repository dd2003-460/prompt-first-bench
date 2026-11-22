# N76: LRU 驱逐对象的平均大小 S_LRU_evict 的估算公式：S_LRU_evict = E[S | P < P_evict]，其中 P_evict 是 LR

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

LRU 驱逐对象的平均大小 S_LRU_evict 的估算公式：S_LRU_evict = E[S | P < P_evict]，其中 P_evict 是 LRU 队列尾部对象的典型热度值，近似为热度分布的中位数或 50 分位数。

## Corrected Claim

LRU 驱逐对象的平均大小 S_LRU_evict 的估算公式：S_LRU_evict = E[S | P < P_evict]，其中 P_evict 是 LRU 队列尾部对象的典型热度值，近似为热度分布的中位数或 50 分位数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU eviction object size distribution
