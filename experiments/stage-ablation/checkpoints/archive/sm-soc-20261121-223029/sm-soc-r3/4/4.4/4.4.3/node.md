# N88: 卖家盈亏平衡点计算：ΔP_unit = P_list - P_mid，C_marginal 为卖家边际成本，Q_breakeven = ΔP_unit / (P

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

卖家盈亏平衡点计算：ΔP_unit = P_list - P_mid，C_marginal 为卖家边际成本，Q_breakeven = ΔP_unit / (P_mid - C_marginal)，若 C_marginal ≈ 0.8 * P_mid，则 Q_breakeven ≈ 5，即需额外成交 5 件商品才能弥补单价损失。

## Corrected Claim

卖家盈亏平衡点计算：ΔP_unit = P_list - P_mid，C_marginal 为卖家边际成本，Q_breakeven = ΔP_unit / (P_mid - C_marginal)，若 C_marginal ≈ 0.8 * P_mid，则 Q_breakeven ≈ 5，即需额外成交 5 件商品才能弥补单价损失。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（父节点明确聚焦于'卖家盈亏平衡点计算'（涉及单价差、边际成本、平衡销量），但子节点中后5个（工作点A/B/C、基线占比、流量权重影响）完全偏离主题，转而讨论'平台选择效应'和'低质商品占比'，导致子节点与父节点逻辑断裂。此外，工作点A/B/C本质上是同一参数空间（激励强度vs质量变化）的三个离散取值，存在严重冗余。）

## Search Query

seller breakeven quantity price reduction marginal cost second-hand market
