# N196: Gaussian Copula 在 ρ=-0.3 下的二元正态 CDF Φ_ρ(u,v) 的数值计算精度：使用 Owen's T 函数或数值积分时，当 u,v 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

Gaussian Copula 在 ρ=-0.3 下的二元正态 CDF Φ_ρ(u,v) 的数值计算精度：使用 Owen's T 函数或数值积分时，当 u,v 接近 0 或 1 时，双精度浮点误差可达 10^-15，需使用高精度库或解析近似以保证边界命中率计算的准确性。

## Corrected Claim

Gaussian Copula 在 ρ=-0.3 下的二元正态 CDF Φ_ρ(u,v) 的数值计算精度：使用 Owen's T 函数或数值积分时，当 u,v 接近 0 或 1 时，双精度浮点误差可达 10^-15，需使用高精度库或解析近似以保证边界命中率计算的准确性。

## Evidence

先验知识/题面给定，逻辑校验通过
