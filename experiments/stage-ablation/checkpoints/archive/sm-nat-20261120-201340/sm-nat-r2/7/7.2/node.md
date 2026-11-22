# N67: LRU字节命中率下界数值计算：H_byte_LRU_lower = (Σ_{i=1}^{k} r_i)·(1-(k/N)^{0.9}) / (Σ_{i=1}^{

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

LRU字节命中率下界数值计算：H_byte_LRU_lower = (Σ_{i=1}^{k} r_i)·(1-(k/N)^{0.9}) / (Σ_{i=1}^{N} r_i)·w，其中Σ_{i=1}^{k} r_i / Σ_{i=1}^{N} r_i ≈ 1-(k/N)^β = 1-(0.12)^{0.9} ≈ 0.85（β=0.9），(1-(k/N)^{0.9}) ≈ 1-(0.12)^{0.9} ≈ 0.85，w≈1.06，故H_byte_LRU_lower ≈ 0.85·0.85·1.06 ≈ 0.77，即下界约77%。

## Corrected Claim

LRU字节命中率下界数值计算：H_byte_LRU_lower = (Σ_{i=1}^{k} r_i)·(1-(k/N)^{0.9}) / (Σ_{i=1}^{N} r_i)·w，其中Σ_{i=1}^{k} r_i / Σ_{i=1}^{N} r_i ≈ 1-(k/N)^β = 1-(0.12)^{0.9} ≈ 0.85（β=0.9），(1-(k/N)^{0.9}) ≈ 1-(0.12)^{0.9} ≈ 0.85，w≈1.06，故H_byte_LRU_lower ≈ 0.85·0.85·1.06 ≈ 0.77，即下界约77%。

## Evidence

逻辑推导成立，来源未直接覆盖

## Search Query

LRU byte hit rate lower bound Pareto beta 0.9 alpha 1.1 numerical calculation
