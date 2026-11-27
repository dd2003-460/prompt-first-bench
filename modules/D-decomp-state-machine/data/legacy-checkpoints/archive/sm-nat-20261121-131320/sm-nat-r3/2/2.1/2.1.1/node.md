# N28: LFU 稳态字节命中率 H_LFU 的计算公式：H_LFU = (Σ_{i in TopK} f_i * S_i) / (Σ_{all} f_i * S_i)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

LFU 稳态字节命中率 H_LFU 的计算公式：H_LFU = (Σ_{i in TopK} f_i * S_i) / (Σ_{all} f_i * S_i)，其中 TopK 集合定义为满足 Σ_{j in TopK} S_j ≤ C 且按 f_j 降序排列的最大对象子集；需计算 TopK 中包含的对象数量 K_max 及其累计字节占比。

## Corrected Claim

LFU 稳态字节命中率 H_LFU 的计算公式：H_LFU = (Σ_{i in TopK} f_i * S_i) / (Σ_{all} f_i * S_i)，其中 TopK 集合定义为满足 Σ_{j in TopK} S_j ≤ C 且按 f_j 降序排列的最大对象子集；需计算 TopK 中包含的对象数量 K_max 及其累计字节占比。

## Evidence

先验知识/题面给定，逻辑校验通过
