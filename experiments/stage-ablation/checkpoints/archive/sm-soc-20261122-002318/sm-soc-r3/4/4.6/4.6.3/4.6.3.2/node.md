# N210: 流失率敏感度系数 β 的量化：β = β_base * (1 + λ_trust)。其中 β_base 为基准流失率对营收波动的敏感度（通常 β_base ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N73

## Claim

流失率敏感度系数 β 的量化：β = β_base * (1 + λ_trust)。其中 β_base 为基准流失率对营收波动的敏感度（通常 β_base ≈ 0.5，即营收每下降 1%，流失率上升 0.5%），λ_trust 为信任冲击放大系数。若价格透明度提升带来正向信任效应，λ_trust 为负值（如 -0.2），则 β 降低至 0.4，表示流失风险减弱。

## Corrected Claim

流失率敏感度系数 β 的量化：β = β_base * (1 + λ_trust)。其中 β_base 为基准流失率对营收波动的敏感度（通常 β_base ≈ 0.5，即营收每下降 1%，流失率上升 0.5%），λ_trust 为信任冲击放大系数。若价格透明度提升带来正向信任效应，λ_trust 为负值（如 -0.2），则 β 降低至 0.4，表示流失风险减弱。

## Evidence

先验知识/题面给定，逻辑校验通过
