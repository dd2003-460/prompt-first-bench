# N9: LRU 稳态字节命中率下界公式：H_byte_LRU = Σ_{i∈Cache} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j)，其中 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU 稳态字节命中率下界公式：H_byte_LRU = Σ_{i∈Cache} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j)，其中 Cache 集合由 LRU 策略决定，即缓存中保留的是最近访问过的对象，需根据访问序列模拟或解析求解 Cache 集合的构成。

## Corrected Claim

LRU 稳态字节命中率下界公式：H_byte_LRU = Σ_{i∈Cache} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j)，其中 Cache 集合由 LRU 策略决定，即缓存中保留的是最近访问过的对象，需根据访问序列模拟或解析求解 Cache 集合的构成。

## Evidence

先验知识/题面给定，逻辑校验通过
