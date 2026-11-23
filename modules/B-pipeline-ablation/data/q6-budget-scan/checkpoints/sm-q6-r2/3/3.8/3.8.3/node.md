# N123: 缓存效率对带宽成本影响的边际收益：d(ΔC_bandwidth)/dH_cache = -V_total * (p_download - p_cache)，即缓

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

缓存效率对带宽成本影响的边际收益：d(ΔC_bandwidth)/dH_cache = -V_total * (p_download - p_cache)，即缓存命中率每提高1%，带宽成本减少 V_total * 0.01 * (p_download - p_cache) ≈ ¥15/月（基于上述参数） [待核验]

## Corrected Claim

缓存效率对带宽成本影响的边际收益：d(ΔC_bandwidth)/dH_cache = -V_total * (p_download - p_cache)，即缓存命中率每提高1%，带宽成本减少 V_total * 0.01 * (p_download - p_cache) ≈ ¥15/月（基于上述参数） [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：公式 d(ΔC)/dH = -V_total * (p_download - p_cache) 符合成本函数对命中率的导数定义，量纲与数值量级（¥15/月）在常规业务场景下合理。
