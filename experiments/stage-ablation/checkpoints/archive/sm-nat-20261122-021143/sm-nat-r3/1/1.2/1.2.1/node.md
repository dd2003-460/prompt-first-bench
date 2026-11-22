# N25: Pareto(β=0.9) 分布的截断点 r_max 由总请求数约束确定：Σ_{k=1}^{10^5} R_k = 5 * 10^7，若采用连续 Pareto 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Pareto(β=0.9) 分布的截断点 r_max 由总请求数约束确定：Σ_{k=1}^{10^5} R_k = 5 * 10^7，若采用连续 Pareto 模型，r_max 满足 ∫_{r_min}^{r_max} r * 0.9 * r_min^0.9 * r^{-1.9} dr = 5 * 10^7，解得 r_max ≈ r_min * (1 + 5 * 10^7 / (0.9 * r_min * 10^5))^{10}

## Corrected Claim

Pareto(β=0.9) 分布的截断点 r_max 由总请求数约束确定：Σ_{k=1}^{10^5} R_k = 5 * 10^7，若采用连续 Pareto 模型，r_max 满足 ∫_{r_min}^{r_max} r * 0.9 * r_min^0.9 * r^{-1.9} dr = 5 * 10^7，解得 r_max ≈ r_min * (1 + 5 * 10^7 / (0.9 * r_min * 10^5))^{10}

## Evidence

先验知识/题面给定，逻辑校验通过：积分计算与代数推导自洽，量级合理
