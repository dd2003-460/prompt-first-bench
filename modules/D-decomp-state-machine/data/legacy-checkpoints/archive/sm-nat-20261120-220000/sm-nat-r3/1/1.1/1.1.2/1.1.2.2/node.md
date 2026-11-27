# N70: C >> S_total 结论对命中率下界的影响量化：若 S_total ≈ 602 MB (S_max=10MB) 或 499 MB (S_max=1GB)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

C >> S_total 结论对命中率下界的影响量化：若 S_total ≈ 602 MB (S_max=10MB) 或 499 MB (S_max=1GB)，均远小于 C=128GB，则缓存可容纳所有对象，LRU 字节命中率下界 H_LRU ≥ 1 - P_miss_tail，其中 P_miss_tail 由请求分布决定而非容量限制，需计算在容量无限大时，LRU 的稳态命中率是否趋近于 1（即所有请求均命中，因为所有对象都在缓存中）。

## Corrected Claim

C >> S_total 结论对命中率下界的影响量化：若 S_total ≈ 602 MB (S_max=10MB) 或 499 MB (S_max=1GB)，均远小于 C=128GB，则缓存可容纳所有对象，LRU 字节命中率下界 H_LRU ≥ 1 - P_miss_tail，其中 P_miss_tail 由请求分布决定而非容量限制，需计算在容量无限大时，LRU 的稳态命中率是否趋近于 1（即所有请求均命中，因为所有对象都在缓存中）。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量 C 远大于工作集大小 S_total 时，LRU 缓存可容纳所有对象，稳态下所有请求均命中，命中率趋近于 1，逻辑自洽且符合缓存基本原理。
