# N131: 投影1（高溢价曝光偏差）：高溢价商品（δ ∈ [15%, 25%]）相对于基准商品的曝光量期望比 E[Imp_high]/E[Imp_base] = 1 + α

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

投影1（高溢价曝光偏差）：高溢价商品（δ ∈ [15%, 25%]）相对于基准商品的曝光量期望比 E[Imp_high]/E[Imp_base] = 1 + α * δ + Var(ε_rank)，需量化 Var(ε_rank) 对总曝光偏差的贡献占比，以区分算法确定性加权与随机噪声的影响。

## Corrected Claim

投影1（高溢价曝光偏差）：高溢价商品（δ ∈ [15%, 25%]）相对于基准商品的曝光量期望比 E[Imp_high]/E[Imp_base] = 1 + α * δ + Var(ε_rank)，需量化 Var(ε_rank) 对总曝光偏差的贡献占比，以区分算法确定性加权与随机噪声的影响。

## Evidence

先验知识/题面给定，逻辑校验通过
