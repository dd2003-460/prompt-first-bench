# N125: P(i ∈ LRU) 的堆栈距离近似：在稳态 LRU 中，对象 i 驻留的概率近似为 1 如果其访问间隔 T_i < T_evict，其中 T_evict 是缓

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

P(i ∈ LRU) 的堆栈距离近似：在稳态 LRU 中，对象 i 驻留的概率近似为 1 如果其访问间隔 T_i < T_evict，其中 T_evict 是缓存满时的驱逐时间。由于 C=128GB 可容纳 ~13,333 个对象，且热度平坦，Rank < 13,333 的对象 P(i ∈ LRU) ≈ 1，Rank > 13,333 的对象 P(i ∈ LRU) ≈ 0（忽略抖动）。

## Corrected Claim

P(i ∈ LRU) 的堆栈距离近似：在稳态 LRU 中，对象 i 驻留的概率近似为 1 如果其访问间隔 T_i < T_evict，其中 T_evict 是缓存满时的驱逐时间。由于 C=128GB 可容纳 ~13,333 个对象，且热度平坦，Rank < 13,333 的对象 P(i ∈ LRU) ≈ 1，Rank > 13,333 的对象 P(i ∈ LRU) ≈ 0（忽略抖动）。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 的堆栈距离模型（Stack Distance Model）是缓存理论中的标准近似，在稳态且热度平坦假设下，驻留概率与排名/容量阈值的二元关系符合基本逻辑。
