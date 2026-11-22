# N217: 需求抑制系数 ε_price：价格每增加 1%，成交量下降的百分比；在二手市场，ε_price 通常在 [-1.5, -0.8] 之间；需计算 ε_exposu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

需求抑制系数 ε_price：价格每增加 1%，成交量下降的百分比；在二手市场，ε_price 通常在 [-1.5, -0.8] 之间；需计算 ε_exposure * Δln(Exposure) + ε_price * Δln(Price) > 0 是否成立以验证短周期机制

## Corrected Claim

需求抑制系数 ε_price：价格每增加 1%，成交量下降的百分比；在二手市场，ε_price 通常在 [-1.5, -0.8] 之间；需计算 ε_exposure * Δln(Exposure) + ε_price * Δln(Price) > 0 是否成立以验证短周期机制

## Evidence

先验知识/题面给定，逻辑校验通过
