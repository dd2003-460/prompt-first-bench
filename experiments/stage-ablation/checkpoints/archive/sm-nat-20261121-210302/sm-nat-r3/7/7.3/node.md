# N77: LFU 相比 LRU 的最大提升百分点 Δ% 的量化上界：Δ% <= (S_LRU_evict / S_LFU_hot - 1) * MissRate_LRU 

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数取值下的具体实例，属于冗余重复而非独立维度的分解；且父节点核心是通用量化上界公式，子节点仅覆盖两个特定工作点，未涵盖公式本身的推导逻辑、变量定义或边界条件，导致不完备。）

## Search Query

LFU vs LRU hit rate improvement bound
