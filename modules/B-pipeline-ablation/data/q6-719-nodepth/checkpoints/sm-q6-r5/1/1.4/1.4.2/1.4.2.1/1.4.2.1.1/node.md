# N468: 缓存预热完成度 W_cache 的量化定义：W_cache = (Cached_Objects_Size / Total_Hot_Objects_Size)，其

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N150

## Claim

缓存预热完成度 W_cache 的量化定义：W_cache = (Cached_Objects_Size / Total_Hot_Objects_Size)，其中 Cached_Objects_Size 为当前缓存中有效对象大小，Total_Hot_Objects_Size 为热数据总量（1.2TB），W_cache ∈ [0,1]，该指标直接决定回源率 R_back = 1 - W_cache * H_base，H_base 为基础命中率（0.9）。

## Corrected Claim

缓存预热完成度 W_cache 的量化定义：W_cache = (Cached_Objects_Size / Total_Hot_Objects_Size)，其中 Cached_Objects_Size 为当前缓存中有效对象大小，Total_Hot_Objects_Size 为热数据总量（1.2TB），W_cache ∈ [0,1]，该指标直接决定回源率 R_back = 1 - W_cache * H_base，H_base 为基础命中率（0.9）。

## Evidence

先验知识/题面给定，逻辑校验通过
