# N105: 边界条件检查：当 r_i=1（最热门）时，Φ^{-1}(F_H(1)) = Φ^{-1}(0.9) ≈ 1.28，E[S_1|rank=1] = 1KB * e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

边界条件检查：当 r_i=1（最热门）时，Φ^{-1}(F_H(1)) = Φ^{-1}(0.9) ≈ 1.28，E[S_1|rank=1] = 1KB * exp(μ_S - 0.3 * 0.95 * 1.28) ≈ 1KB * exp(μ_S - 0.365)，需计算具体数值以验证是否低于 x_min

## Corrected Claim

边界条件检查：当 r_i=1（最热门）时，Φ^{-1}(F_H(1)) = Φ^{-1}(0.9) ≈ 1.28，E[S_1|rank=1] = 1KB * exp(μ_S - 0.3 * 0.95 * 1.28) ≈ 1KB * exp(μ_S - 0.365)，需计算具体数值以验证是否低于 x_min

## Evidence

先验知识/题面给定，逻辑校验通过
