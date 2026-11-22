# N132: 有效缓存容量 C' 的计算公式：C' = 128GB × M_cache_ratio - Σ (S_i for i in Write_BW), 其中 M_cac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

有效缓存容量 C' 的计算公式：C' = 128GB × M_cache_ratio - Σ (S_i for i in Write_BW), 其中 M_cache_ratio 为内存分配比例（假设 0.5 至 1.0），Write_BW 为更新写带宽占用的缓存空间，需计算 Write_BW = N_obj × λ_upd × E[S] × T_dirty 以扣除脏页占用。

## Corrected Claim

有效缓存容量 C' 的计算公式：C' = 128GB × M_cache_ratio - Σ (S_i for i in Write_BW), 其中 M_cache_ratio 为内存分配比例（假设 0.5 至 1.0），Write_BW 为更新写带宽占用的缓存空间，需计算 Write_BW = N_obj × λ_upd × E[S] × T_dirty 以扣除脏页占用。

## Evidence

先验知识/题面给定，逻辑校验通过
