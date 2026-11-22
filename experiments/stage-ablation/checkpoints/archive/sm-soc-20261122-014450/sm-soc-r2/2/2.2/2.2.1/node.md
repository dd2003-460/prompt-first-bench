# N52: 柠檬市场逆向选择系数 β 的量化：β = β_base * (1 + γ * NonStandardization_Index)，其中 β_base 为标准化品

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

柠檬市场逆向选择系数 β 的量化：β = β_base * (1 + γ * NonStandardization_Index)，其中 β_base 为标准化品基准系数（预期 β_base ≈ 0.2），γ 为非标品放大系数（预期 γ ≈ 0.5），NonStandardization_Index 为商品非标程度指数（0-1）；需通过 A/B 测试或历史数据回归验证 β 在二手非标品中的具体数值（预期 β_used ≈ 0.35）。

## Corrected Claim

柠檬市场逆向选择系数 β 的量化：β = β_base * (1 + γ * NonStandardization_Index)，其中 β_base 为标准化品基准系数（预期 β_base ≈ 0.2），γ 为非标品放大系数（预期 γ ≈ 0.5），NonStandardization_Index 为商品非标程度指数（0-1）；需通过 A/B 测试或历史数据回归验证 β 在二手非标品中的具体数值（预期 β_used ≈ 0.35）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

lemon market adverse selection price drop consultation rate second hand
