# N103: 缓存命中率 H_cache 的精确计算需考虑对象大小分布：H_cache = Σ (f_i * s_i) / Σ s_i，其中 f_i 为对象 i 的访问频次，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N26, N27

## Claim

缓存命中率 H_cache 的精确计算需考虑对象大小分布：H_cache = Σ (f_i * s_i) / Σ s_i，其中 f_i 为对象 i 的访问频次，s_i 为对象 i 的大小；仅用请求数计算的命中率会高估实际带宽节省效果。

## Corrected Claim

缓存命中率 H_cache 的精确计算需考虑对象大小分布：H_cache = Σ (f_i * s_i) / Σ s_i，其中 f_i 为对象 i 的访问频次，s_i 为对象 i 的大小；仅用请求数计算的命中率会高估实际带宽节省效果。

## Evidence

先验知识/题面给定，逻辑校验通过：基于字节/带宽维度的加权命中率公式在数学上自洽，且符合缓存评估中区分请求数与数据量的基本工程原理。

## Search Query

cache hit rate weighted by object size calculation
