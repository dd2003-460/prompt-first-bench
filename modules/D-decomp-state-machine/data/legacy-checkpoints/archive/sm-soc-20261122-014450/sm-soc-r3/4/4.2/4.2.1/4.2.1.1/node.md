# N231: 在 P_high = 1.2 * P_market 且 P_low = 1.0 * P_market 的基准场景下，代入 N11 收益函数计算出的具体 ΔU_l

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

在 P_high = 1.2 * P_market 且 P_low = 1.0 * P_market 的基准场景下，代入 N11 收益函数计算出的具体 ΔU_loss 数值为 -0.2 * P_market * (P(sale|P_high) - P(sale|P_low))，需明确 P(sale) 的具体参数化形式（如逻辑斯蒂函数）。

## Corrected Claim

在 P_high = 1.2 * P_market 且 P_low = 1.0 * P_market 的基准场景下，代入 N11 收益函数计算出的具体 ΔU_loss 数值为 -0.2 * P_market * (P(sale|P_high) - P(sale|P_low))，需明确 P(sale) 的具体参数化形式（如逻辑斯蒂函数）。

## Evidence

先验知识/题面给定，逻辑校验通过：该表达式是收益函数在特定价格参数下的代数推导结果，量纲与逻辑自洽，且明确指出了需补充概率参数化形式的前提。
