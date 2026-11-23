# N12: 缓存命中率对延迟的影响：P99延迟 = p_hit * t_cache + p_miss * (t_cache + t_origin)，其中 t_cache 为

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

缓存命中率对延迟的影响：P99延迟 = p_hit * t_cache + p_miss * (t_cache + t_origin)，其中 t_cache 为边缘缓存命中延迟（通常 < 5ms），p_hit 为缓存命中率

## Corrected Claim

缓存命中率对延迟的影响：P99延迟 = p_hit * t_cache + p_miss * (t_cache + t_origin)，其中 t_cache 为边缘缓存命中延迟（通常 < 5ms），p_hit 为缓存命中率

## Evidence

先验知识/题面给定，逻辑校验通过
