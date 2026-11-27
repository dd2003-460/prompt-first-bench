# N10: LRU 稳态字节命中率下界的通用公式：H_byte_LRU ≈ 1 - (Σ_{i∉Cache} p_i · s_i) / (Σ_{all} p_i · s_i

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 稳态字节命中率下界的通用公式：H_byte_LRU ≈ 1 - (Σ_{i∉Cache} p_i · s_i) / (Σ_{all} p_i · s_i)，其中 p_i 为对象 i 的访问概率，s_i 为大小，Cache 为 LRU 保留的对象集合。

## Corrected Claim

LRU 稳态字节命中率下界的通用公式：H_byte_LRU ≈ 1 - (Σ_{i∉Cache} p_i · s_i) / (Σ_{all} p_i · s_i)，其中 p_i 为对象 i 的访问概率，s_i 为大小，Cache 为 LRU 保留的对象集合。

## Evidence

先验知识/题面给定，逻辑校验通过
