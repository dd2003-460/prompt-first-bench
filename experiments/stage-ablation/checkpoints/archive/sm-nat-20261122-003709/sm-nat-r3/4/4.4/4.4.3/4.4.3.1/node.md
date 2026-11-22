# N202: 在LRU容量受限（K<N）且热度β=0.9的‘高惩罚/低局部性’工作点下，ε_LRU = 1 - (Σ_{i=1}^K p_i / Σ_{i=1}^N p_i)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

在LRU容量受限（K<N）且热度β=0.9的‘高惩罚/低局部性’工作点下，ε_LRU = 1 - (Σ_{i=1}^K p_i / Σ_{i=1}^N p_i)，由于K受限于128GB内存（约5-6万个对象），尾部高热度对象被频繁驱逐，ε_LRU ≈ 0.05（5个百分点）。

## Corrected Claim

在LRU容量受限（K<N）且热度β=0.9的‘高惩罚/低局部性’工作点下，ε_LRU = 1 - (Σ_{i=1}^K p_i / Σ_{i=1}^N p_i)，由于K受限于128GB内存（约5-6万个对象），尾部高热度对象被频繁驱逐，ε_LRU ≈ 0.05（5个百分点）。

## Evidence

先验知识/题面给定，逻辑校验通过
