# N77: LFU 相比 LRU 的最大提升百分点 Δ% 的量化上界：Δ% <= (S_LRU_evict / S_LFU_hot - 1) * MissRate_LRU 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

LFU 相比 LRU 的最大提升百分点 Δ% 的量化上界：Δ% <= (S_LRU_evict / S_LFU_hot - 1) * MissRate_LRU * (1 - P_hot_bytes)，其中 P_hot_bytes 是热点对象占缓存总字节的比例。

## Corrected Claim

LFU 相比 LRU 的最大提升百分点 Δ% 的量化上界：Δ% <= (S_LRU_evict / S_LFU_hot - 1) * MissRate_LRU * (1 - P_hot_bytes)，其中 P_hot_bytes 是热点对象占缓存总字节的比例。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU hit rate improvement bound
