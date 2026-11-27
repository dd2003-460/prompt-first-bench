# N186: 在引入更新率（1%/天）后，Miss_Bytes_LRU 的增量项为 Σ_{i=1}^{N} [S_i * q_i * (1 - e^{-λ_update * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N61

## Claim

在引入更新率（1%/天）后，Miss_Bytes_LRU 的增量项为 Σ_{i=1}^{N} [S_i * q_i * (1 - e^{-λ_update * T_residence_i})]，其中 T_residence_i 为对象 i 在 LRU 中的平均驻留时间，该项量化了因对象更新导致的缓存失效字节数。

## Corrected Claim

在引入更新率（1%/天）后，Miss_Bytes_LRU 的增量项为 Σ_{i=1}^{N} [S_i * q_i * (1 - e^{-λ_update * T_residence_i})]，其中 T_residence_i 为对象 i 在 LRU 中的平均驻留时间，该项量化了因对象更新导致的缓存失效字节数。

## Evidence

先验知识/题面给定，逻辑校验通过
