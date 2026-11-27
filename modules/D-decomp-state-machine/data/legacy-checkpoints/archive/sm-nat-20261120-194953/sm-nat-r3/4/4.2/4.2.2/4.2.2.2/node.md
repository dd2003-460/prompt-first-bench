# N123: S_hot 的理论下界估计：若忽略相关性（ρ=0），S_hot 应等于热度占比 10%；引入 ρ=-0.3 后，由于热门对象更小，S_hot 应低于 10%，公

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

S_hot 的理论下界估计：若忽略相关性（ρ=0），S_hot 应等于热度占比 10%；引入 ρ=-0.3 后，由于热门对象更小，S_hot 应低于 10%，公式为 S_hot ≈ 10% * (E[S|Hot]/E[S])，需验证该线性近似在重尾分布下的有效性。

## Corrected Claim

S_hot 的理论下界估计：若忽略相关性（ρ=0），S_hot 应等于热度占比 10%；引入 ρ=-0.3 后，由于热门对象更小，S_hot 应低于 10%，公式为 S_hot ≈ 10% * (E[S|Hot]/E[S])，需验证该线性近似在重尾分布下的有效性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

byte hit rate cache hot set size correlation
