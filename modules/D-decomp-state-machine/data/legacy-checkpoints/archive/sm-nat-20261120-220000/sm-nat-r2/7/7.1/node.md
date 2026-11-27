# N52: LRU稳态字节命中率下界的正确公式应为 H_LRU ≥ 1 - (1 - q*) * (S_uncovered / S_total)，其中q*为被缓存对象的热度

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

LRU稳态字节命中率下界的正确公式应为 H_LRU ≥ 1 - (1 - q*) * (S_uncovered / S_total)，其中q*为被缓存对象的热度占比，S_uncovered为未缓存对象的字节占比。

## Corrected Claim

LRU稳态字节命中率下界的正确公式应为 H_LRU ≥ 1 - (1 - q*) * (S_uncovered / S_total)，其中q*为被缓存对象的热度占比，S_uncovered为未缓存对象的字节占比。

## Evidence

先验知识/题面给定，逻辑校验通过
