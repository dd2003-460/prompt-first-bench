# N12: 缓存命中率对延迟的影响：P99延迟 = p_hit * t_cache + p_miss * (t_cache + t_origin)，其中 t_cache 为

- **status**: pending
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

父节点级核验未通过：不完备（子节点分别详细分解了公式中的 t_cache 和 t_origin 两个主要延迟分量，二者内容互不重叠且逻辑清晰，满足正交性。然而，父节点公式中明确包含 'p_hit' (缓存命中率) 这一关键变量，且标题强调 '命中率对延迟的影响'，但子节点完全未涵盖影响 p_hit 的因素（如缓存策略、对象大小分布、TTL设置、业务流量模式等），导致关键方面缺失，不满足完备性。）
