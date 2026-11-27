# N66: 指数增长项的基底参数 β_growth：当 |ε_i| > θ_buyer 时，δT = β_noise * |ε_i| * e^(β_growth * (|ε

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

指数增长项的基底参数 β_growth：当 |ε_i| > θ_buyer 时，δT = β_noise * |ε_i| * e^(β_growth * (|ε_i| - θ_buyer)/σ_ε)，其中 β_growth 为买家困惑度放大系数（通常 β_growth ∈ [0.5, 1.5]），需通过长尾未成交商品的 T_deal 数据拟合得出。

## Corrected Claim

指数增长项的基底参数 β_growth：当 |ε_i| > θ_buyer 时，δT = β_noise * |ε_i| * e^(β_growth * (|ε_i| - θ_buyer)/σ_ε)，其中 β_growth 为买家困惑度放大系数（通常 β_growth ∈ [0.5, 1.5]），需通过长尾未成交商品的 T_deal 数据拟合得出。

## Evidence

先验知识/题面给定，逻辑校验通过
