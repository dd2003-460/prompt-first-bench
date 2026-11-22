# N65: GMV 与利润的背离风险：若高价导致成交量 Q 下降幅度超过价格 P 上升幅度（即弹性 |ε| > 1），则 GMV 和佣金均下降；需计算临界弹性 ε_crit

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

GMV 与利润的背离风险：若高价导致成交量 Q 下降幅度超过价格 P 上升幅度（即弹性 |ε| > 1），则 GMV 和佣金均下降；需计算临界弹性 ε_critical = -1，并对比当前市场实测弹性区间（如 -0.5 至 -0.8）以确认平台是否处于利润上升区间。

## Corrected Claim

GMV 与利润的背离风险：若高价导致成交量 Q 下降幅度超过价格 P 上升幅度（即弹性 |ε| > 1），则 GMV 和佣金均下降；需计算临界弹性 ε_critical = -1，并对比当前市场实测弹性区间（如 -0.5 至 -0.8）以确认平台是否处于利润上升区间。

## Evidence

先验知识/题面给定，逻辑校验通过：基于微积分与经济学基本原理，GMV=P*Q，当价格弹性|ε|>1时，价格上升导致的数量下降幅度大于价格上升幅度，导致GMV下降，推导逻辑自洽且数值量级合理。

## Search Query

GMV vs profit elasticity threshold marketplace pricing strategy break-even elasticity
