# N48: 在 S_min=1MB 且 N_max/N_min=10 的边界条件下，计算得 E[S] ≈ 10MB，此时总空间 N*E[S] ≈ 1PB，覆盖比例 C = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

在 S_min=1MB 且 N_max/N_min=10 的边界条件下，计算得 E[S] ≈ 10MB，此时总空间 N*E[S] ≈ 1PB，覆盖比例 C = 128GB/1PB ≈ 0.000128，H_LRU 下界趋近于 0，表明若对象普遍较大，缓存几乎无效。

## Corrected Claim

在 S_min=1MB 且 N_max/N_min=10 的边界条件下，计算得 E[S] ≈ 10MB，此时总空间 N*E[S] ≈ 1PB，覆盖比例 C = 128GB/1PB ≈ 0.000128，H_LRU 下界趋近于 0，表明若对象普遍较大，缓存几乎无效。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算（10MB * 100,000,000 ≈ 1PB, 128GB/1PB ≈ 0.000128）准确，LRU缓存命中率随覆盖比例趋近于0而趋近于0符合缓存理论直觉。

## Search Query

Pareto distribution large object cache efficiency
