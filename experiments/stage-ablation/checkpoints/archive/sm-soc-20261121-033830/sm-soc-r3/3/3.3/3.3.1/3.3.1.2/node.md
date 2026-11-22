# N196: 交互项β2的边际效应量化：高价高互动商品的曝光放大效应为 β2 * (log(P_i) - log(P_median))，需计算当 P_i = P_median

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

交互项β2的边际效应量化：高价高互动商品的曝光放大效应为 β2 * (log(P_i) - log(P_median))，需计算当 P_i = P_median * 1.2 且 Interaction_i = 1 时，曝光相对于基准商品的倍数 Ratio = exp(β1*log(1.2) + β2*1)，验证该倍数是否显著大于1.5

## Corrected Claim

交互项β2的边际效应量化：高价高互动商品的曝光放大效应为 β2 * (log(P_i) - log(P_median))，需计算当 P_i = P_median * 1.2 且 Interaction_i = 1 时，曝光相对于基准商品的倍数 Ratio = exp(β1*log(1.2) + β2*1)，验证该倍数是否显著大于1.5

## Evidence

先验知识/题面给定，逻辑校验通过
