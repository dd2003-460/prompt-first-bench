# N361: 自建部分 P99 延迟 P99_self(α) 的估计公式：P99_self(α) = t_cache_self + p_miss_self(α) * t_or

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

自建部分 P99 延迟 P99_self(α) 的估计公式：P99_self(α) = t_cache_self + p_miss_self(α) * t_origin_self，其中 t_cache_self ≈ 3-5ms，p_miss_self(α) = 1 - H_self(α)，H_self(α) 为自建缓存命中率

## Corrected Claim

自建部分 P99 延迟 P99_self(α) 的估计公式：P99_self(α) = t_cache_self + p_miss_self(α) * t_origin_self，其中 t_cache_self ≈ 3-5ms，p_miss_self(α) = 1 - H_self(α)，H_self(α) 为自建缓存命中率

## Evidence

先验知识/题面给定，逻辑校验通过
