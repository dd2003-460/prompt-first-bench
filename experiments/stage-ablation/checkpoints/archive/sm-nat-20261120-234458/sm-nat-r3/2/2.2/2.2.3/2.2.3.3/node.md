# N122: LRU 在容量受限 (K<N) 时的字节命中率 H_LRU_bytes 近似公式：H_LRU_bytes ≈ 1 - (Miss_Bytes_Cold / To

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

LRU 在容量受限 (K<N) 时的字节命中率 H_LRU_bytes 近似公式：H_LRU_bytes ≈ 1 - (Miss_Bytes_Cold / Total_Bytes)，其中 Miss_Bytes_Cold 为未命中对象的字节加权总和，需结合 Pareto(α) 大小分布积分

## Corrected Claim

LRU 在容量受限 (K<N) 时的字节命中率 H_LRU_bytes 近似公式：H_LRU_bytes ≈ 1 - (Miss_Bytes_Cold / Total_Bytes)，其中 Miss_Bytes_Cold 为未命中对象的字节加权总和，需结合 Pareto(α) 大小分布积分

## Evidence

先验知识/题面给定，逻辑校验通过
