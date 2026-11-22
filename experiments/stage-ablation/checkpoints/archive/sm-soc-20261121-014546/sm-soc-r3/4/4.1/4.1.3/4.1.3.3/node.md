# N281: 成交量补偿效应 Q_comp：价格下移带来的成交量增加 ΔQ 对利润的补偿比例，ΔQ = ε_d * 10%。当 ε_d > 1.0 时，ΔQ > 10%，利润

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N84

## Claim

成交量补偿效应 Q_comp：价格下移带来的成交量增加 ΔQ 对利润的补偿比例，ΔQ = ε_d * 10%。当 ε_d > 1.0 时，ΔQ > 10%，利润可能不降反升；当 ε_d < 0.5 时，ΔQ < 5%，利润显著下降。该阈值决定了干预措施对不同弹性商品的差异化伤害。

## Corrected Claim

成交量补偿效应 Q_comp：价格下移带来的成交量增加 ΔQ 对利润的补偿比例，ΔQ = ε_d * 10%。当 ε_d > 1.0 时，ΔQ > 10%，利润可能不降反升；当 ε_d < 0.5 时，ΔQ < 5%，利润显著下降。该阈值决定了干预措施对不同弹性商品的差异化伤害。

## Evidence

先验知识/题面给定，逻辑校验通过：基于需求价格弹性定义 ΔQ% = ε_d * ΔP%，当 ΔP=-10% 时，ΔQ = 10% * ε_d。若 ε_d > 1，收入增加；若 ε_d < 0.5，收入显著下降，推导自洽。

## Search Query

volume compensation effect of price reduction on seller profit in inelastic markets
