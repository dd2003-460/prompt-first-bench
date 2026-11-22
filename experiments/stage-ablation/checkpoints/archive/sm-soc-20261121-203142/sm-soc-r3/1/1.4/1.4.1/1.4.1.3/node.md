# N132: 投影2（低溢价曝光偏差）：低溢价或平价商品（δ ≈ 0）的曝光量期望 E[Imp_low] = Base_Imp * (1 + ε_rank)，需验证在 ε_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

投影2（低溢价曝光偏差）：低溢价或平价商品（δ ≈ 0）的曝光量期望 E[Imp_low] = Base_Imp * (1 + ε_rank)，需验证在 ε_rank ~ N(0, σ_rank²) 假设下，低溢价商品是否会因负向截断误差导致曝光量低于 Base_Imp 的下界，从而解释为何高溢价商品相对更具优势。

## Corrected Claim

投影2（低溢价曝光偏差）：低溢价或平价商品（δ ≈ 0）的曝光量期望 E[Imp_low] = Base_Imp * (1 + ε_rank)，需验证在 ε_rank ~ N(0, σ_rank²) 假设下，低溢价商品是否会因负向截断误差导致曝光量低于 Base_Imp 的下界，从而解释为何高溢价商品相对更具优势。

## Evidence

先验知识/题面给定，逻辑校验通过：在正态分布假设下，负向截断误差确实会导致部分低溢价商品曝光量低于基准，符合概率论基本性质。
