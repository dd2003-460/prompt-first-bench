# N223: 最小样本量 n_min 计算：为在 α=0.05, β=0.2 的统计功效下检测出 λ_post 相对于 λ_base 的 47.5% 下降，最小样本量 n_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

最小样本量 n_min 计算：为在 α=0.05, β=0.2 的统计功效下检测出 λ_post 相对于 λ_base 的 47.5% 下降，最小样本量 n_min = (Z_α + Z_β)^2 * λ_base / (λ_base - λ_post)^2，若实际 n < n_min，则 p 值不显著，无法拒绝 H0。

## Corrected Claim

最小样本量 n_min 计算：为在 α=0.05, β=0.2 的统计功效下检测出 λ_post 相对于 λ_base 的 47.5% 下降，最小样本量 n_min = (Z_α + Z_β)^2 * λ_base / (λ_base - λ_post)^2，若实际 n < n_min，则 p 值不显著，无法拒绝 H0。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

sample size calculation Poisson rate reduction statistical power
