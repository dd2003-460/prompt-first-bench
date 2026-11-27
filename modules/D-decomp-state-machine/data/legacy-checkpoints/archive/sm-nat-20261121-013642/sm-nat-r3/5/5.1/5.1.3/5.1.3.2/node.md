# N204: 线性近似 δ ≈ 1 - λ_u * T_cold 的有效边界条件为 λ_u * T_cold < 0.1；当 λ_u * T_cold = 0.5 时，线性近

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

线性近似 δ ≈ 1 - λ_u * T_cold 的有效边界条件为 λ_u * T_cold < 0.1；当 λ_u * T_cold = 0.5 时，线性近似误差达 exp(-0.5) - (1-0.5) = 0.6065 - 0.5 = 0.1065 (10.65%)，超出工程可接受误差（通常 <5%），因此必须使用精确指数公式 f_update = exp(-λ_u * T_cold)。

## Corrected Claim

线性近似 δ ≈ 1 - λ_u * T_cold 的有效边界条件为 λ_u * T_cold < 0.1；当 λ_u * T_cold = 0.5 时，线性近似误差达 exp(-0.5) - (1-0.5) = 0.6065 - 0.5 = 0.1065 (10.65%)，超出工程可接受误差（通常 <5%），因此必须使用精确指数公式 f_update = exp(-λ_u * T_cold)。

## Evidence

先验知识/题面给定，逻辑校验通过：数学上 exp(-x) ≈ 1-x 的截断误差为 x^2/2，当 x=0.5 时误差为 0.125（相对误差 25%），绝对误差 0.1065 与陈述一致；且 x<0.1 时误差极小，符合工程近似边界。
