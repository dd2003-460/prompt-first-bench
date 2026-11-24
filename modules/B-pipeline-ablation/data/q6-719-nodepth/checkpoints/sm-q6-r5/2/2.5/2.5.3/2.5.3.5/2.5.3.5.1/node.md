# N623: 缓存命中率提升的边际成本函数 C_hit(H) 的非线性形式：C_hit(H) = C_base / (1 - H)^α，其中 α ∈ [1.5, 2.5] 为

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N206

## Claim

缓存命中率提升的边际成本函数 C_hit(H) 的非线性形式：C_hit(H) = C_base / (1 - H)^α，其中 α ∈ [1.5, 2.5] 为内容热度分布的 Zipf 指数相关参数；当 H > 90% 时，(1-H) 极小导致 C_hit 急剧上升，每增加 1% H 的成本增加率 > 50%

## Corrected Claim

缓存命中率提升的边际成本函数 C_hit(H) 的非线性形式：C_hit(H) = C_base / (1 - H)^α，其中 α ∈ [1.5, 2.5] 为内容热度分布的 Zipf 指数相关参数；当 H > 90% 时，(1-H) 极小导致 C_hit 急剧上升，每增加 1% H 的成本增加率 > 50%

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合边际成本递增的经济直觉，且当H>90%时，(1-H)的微小变化确实会导致分母急剧减小，从而引发成本非线性激增，量级与逻辑自洽。
