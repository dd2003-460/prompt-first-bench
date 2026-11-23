# N362: 公有云部分 P99 延迟 P99_cloud(1-α) 的估计公式：P99_cloud(1-α) = t_cache_cloud + p_miss_cloud(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

公有云部分 P99 延迟 P99_cloud(1-α) 的估计公式：P99_cloud(1-α) = t_cache_cloud + p_miss_cloud(1-α) * t_origin_cloud，其中 t_cache_cloud ≈ 20-50ms，p_miss_cloud(1-α) = 1 - H_cloud(1-α)，H_cloud(1-α) 为公有云缓存命中率

## Corrected Claim

公有云部分 P99 延迟 P99_cloud(1-α) 的估计公式：P99_cloud(1-α) = t_cache_cloud + p_miss_cloud(1-α) * t_origin_cloud，其中 t_cache_cloud ≈ 20-50ms，p_miss_cloud(1-α) = 1 - H_cloud(1-α)，H_cloud(1-α) 为公有云缓存命中率

## Evidence

先验知识/题面给定，逻辑校验通过
