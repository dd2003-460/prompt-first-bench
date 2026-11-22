# N183: 工作点1（高获取成本/低持有成本）：假设商品获取成本 C_acq_high = 0.7 * P_market，持有成本 C_hold_low = 0.1 * P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

工作点1（高获取成本/低持有成本）：假设商品获取成本 C_acq_high = 0.7 * P_market，持有成本 C_hold_low = 0.1 * P_market，则总成本 C_high = 0.8 * P_market，基线利润 Margin_high = P_base - C_high = 1.2 * P_market - 0.8 * P_market = 0.4 * P_market，此工作点下卖家对价格下降的敏感度 ε_seller_high = 0.6（因获取成本固定，利润缓冲较小）。

## Corrected Claim

工作点1（高获取成本/低持有成本）：假设商品获取成本 C_acq_high = 0.7 * P_market，持有成本 C_hold_low = 0.1 * P_market，则总成本 C_high = 0.8 * P_market，基线利润 Margin_high = P_base - C_high = 1.2 * P_market - 0.8 * P_market = 0.4 * P_market，此工作点下卖家对价格下降的敏感度 ε_seller_high = 0.6（因获取成本固定，利润缓冲较小）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1.2 - 0.8 = 0.4 正确，成本构成 0.7 + 0.1 = 0.8 正确，敏感度参数为模型假设值，无逻辑矛盾。

## Search Query

seller acquisition cost holding cost breakdown second hand goods market
