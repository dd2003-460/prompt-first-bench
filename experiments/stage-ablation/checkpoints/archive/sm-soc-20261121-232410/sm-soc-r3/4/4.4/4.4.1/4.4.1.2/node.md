# N180: 工作点2（低抽成/高交易量）：假设 r_low = 0.03，则平台单笔收入 Rev_platform_low = 0.03 * P_market，此工作点下卖

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

工作点2（低抽成/高交易量）：假设 r_low = 0.03，则平台单笔收入 Rev_platform_low = 0.03 * P_market，此工作点下卖家利润 Margin_seller_low = 0.4 * P_market - 0.03 * P_market = 0.37 * P_market，需验证平台总收益 Rev_total_low = r_low * Q_low * P_market 是否大于 Rev_total_high = r_high * Q_high * P_market，其中 Q_low/Q_high 为不同费率下的成交量，假设价格弹性 β_price = 1.5 导致 Q_low = Q_high * (1 + 1.5 * (0.10 - 0.03)/0.05) = Q_high * 3.1。

## Corrected Claim

工作点2（低抽成/高交易量）：假设 r_low = 0.03，则平台单笔收入 Rev_platform_low = 0.03 * P_market，此工作点下卖家利润 Margin_seller_low = 0.4 * P_market - 0.03 * P_market = 0.37 * P_market，需验证平台总收益 Rev_total_low = r_low * Q_low * P_market 是否大于 Rev_total_high = r_high * Q_high * P_market，其中 Q_low/Q_high 为不同费率下的成交量，假设价格弹性 β_price = 1.5 导致 Q_low = Q_high * (1 + 1.5 * (0.10 - 0.03)/0.05) = Q_high * 3.1。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

platform commission rate 3% transaction volume elasticity second hand market
