# N71: 卖家利润损失量化：计算干预前后卖家期望利润变化 ΔProfit_seller = (P_new * Q_new - C_holding) - (P_old * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

卖家利润损失量化：计算干预前后卖家期望利润变化 ΔProfit_seller = (P_new * Q_new - C_holding) - (P_old * Q_old - C_holding)。其中 P_new = P_old * (1 - η * ΔP_high_ratio)，Q_new 需根据需求弹性 ε_d 估算：Q_new = Q_old * (1 + ε_d * η * ΔP_high_ratio)。若 ΔProfit_seller < -5% * Profit_old，则卖家受显著伤害。

## Corrected Claim

卖家利润损失量化：计算干预前后卖家期望利润变化 ΔProfit_seller = (P_new * Q_new - C_holding) - (P_old * Q_old - C_holding)。其中 P_new = P_old * (1 - η * ΔP_high_ratio)，Q_new 需根据需求弹性 ε_d 估算：Q_new = Q_old * (1 + ε_d * η * ΔP_high_ratio)。若 ΔProfit_seller < -5% * Profit_old，则卖家受显著伤害。

## Evidence

先验知识/题面给定，逻辑校验通过
