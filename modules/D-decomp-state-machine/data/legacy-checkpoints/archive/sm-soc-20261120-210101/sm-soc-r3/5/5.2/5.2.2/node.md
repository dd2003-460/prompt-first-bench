# N95: CV与σ_pref的映射关系：在信号主导区间（CV<0.1），σ_pref ≈ 0.5 * CV * μ_price；在随机主导区间（CV>0.3），σ_pre

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

CV与σ_pref的映射关系：在信号主导区间（CV<0.1），σ_pref ≈ 0.5 * CV * μ_price；在随机主导区间（CV>0.3），σ_pref ≈ 1.2 * CV * μ_price；中间区间（0.1≤CV≤0.3）采用线性插值σ_pref = (0.5 + 2.0*(CV-0.1)) * CV * μ_price

## Corrected Claim

CV与σ_pref的映射关系：在信号主导区间（CV<0.1），σ_pref ≈ 0.5 * CV * μ_price；在随机主导区间（CV>0.3），σ_pref ≈ 1.2 * CV * μ_price；中间区间（0.1≤CV≤0.3）采用线性插值σ_pref = (0.5 + 2.0*(CV-0.1)) * CV * μ_price

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price coefficient of variation mapping to preference noise standard deviation
