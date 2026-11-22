# N6: LRU稳态字节命中率下界 = (Σ_{i∈C} λ_i * s_i) / (Σ_{j=1}^{N} λ_j * s_j)，其中C为LRU缓存驻留对象集合，λ_i

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

LRU稳态字节命中率下界 = (Σ_{i∈C} λ_i * s_i) / (Σ_{j=1}^{N} λ_j * s_j)，其中C为LRU缓存驻留对象集合，λ_i为对象i的请求频率，s_i为对象i的大小。

## Corrected Claim

LRU稳态字节命中率下界 = (Σ_{i∈C} λ_i * s_i) / (Σ_{j=1}^{N} λ_j * s_j)，其中C为LRU缓存驻留对象集合，λ_i为对象i的请求频率，s_i为对象i的大小。

## Evidence

先验知识/题面给定，逻辑校验通过
