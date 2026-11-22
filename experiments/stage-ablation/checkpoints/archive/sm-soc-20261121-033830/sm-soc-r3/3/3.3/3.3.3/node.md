# N65: GMV 与利润的背离风险：若高价导致成交量 Q 下降幅度超过价格 P 上升幅度（即弹性 |ε| > 1），则 GMV 和佣金均下降；需计算临界弹性 ε_crit

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

GMV 与利润的背离风险：若高价导致成交量 Q 下降幅度超过价格 P 上升幅度（即弹性 |ε| > 1），则 GMV 和佣金均下降；需计算临界弹性 ε_critical = -1，并对比当前市场实测弹性区间（如 -0.5 至 -0.8）以确认平台是否处于利润上升区间。

## Corrected Claim

GMV 与利润的背离风险：若高价导致成交量 Q 下降幅度超过价格 P 上升幅度（即弹性 |ε| > 1），则 GMV 和佣金均下降；需计算临界弹性 ε_critical = -1，并对比当前市场实测弹性区间（如 -0.5 至 -0.8）以确认平台是否处于利润上升区间。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了经验数据验证（现状确认）、基础理论推导（临界点与敏感性）以及动态变量修正（佣金缓冲），三者逻辑独立且互补，共同构成了对父节点‘背离风险’的完整分析框架。）

## Search Query

GMV vs profit elasticity threshold marketplace pricing strategy break-even elasticity
