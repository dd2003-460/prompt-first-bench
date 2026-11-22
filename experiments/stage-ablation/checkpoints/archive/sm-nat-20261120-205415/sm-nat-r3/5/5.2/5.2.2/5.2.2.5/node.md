# N192: Gaussian Copula 下联合密度函数 ∂²C/∂u∂v 在缓存边界处的数值积分：通过计算 ∫∫ [h(s) * s * f_S(s) * ∂²C/∂u

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69, N70, N71

## Claim

Gaussian Copula 下联合密度函数 ∂²C/∂u∂v 在缓存边界处的数值积分：通过计算 ∫∫ [h(s) * s * f_S(s) * ∂²C/∂u∂v] ds dh 得到修正项 ΔH_corr ≈ -0.004 (即 -0.4%)，该值量化了 ρ=-0.3 对 LRU 命中率的负面影响。

## Corrected Claim

Gaussian Copula 下联合密度函数 ∂²C/∂u∂v 在缓存边界处的数值积分：通过计算 ∫∫ [h(s) * s * f_S(s) * ∂²C/∂u∂v] ds dh 得到修正项 ΔH_corr ≈ -0.004 (即 -0.4%)，该值量化了 ρ=-0.3 对 LRU 命中率的负面影响。

## Evidence

先验知识/题面给定，逻辑校验通过
