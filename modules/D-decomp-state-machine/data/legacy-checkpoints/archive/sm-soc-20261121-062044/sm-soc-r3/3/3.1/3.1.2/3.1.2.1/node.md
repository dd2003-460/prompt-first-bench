# N167: P_target 的统计口径：P_target = Σ(P_i * Q_i) / Σ(Q_i)，其中 Q_i 为近7天成交量，若成交量加权平均价与简单算术平均价

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

P_target 的统计口径：P_target = Σ(P_i * Q_i) / Σ(Q_i)，其中 Q_i 为近7天成交量，若成交量加权平均价与简单算术平均价偏差 > 10%，则必须使用加权口径以反映真实市场出清价格。

## Corrected Claim

P_target 的统计口径：P_target = Σ(P_i * Q_i) / Σ(Q_i)，其中 Q_i 为近7天成交量，若成交量加权平均价与简单算术平均价偏差 > 10%，则必须使用加权口径以反映真实市场出清价格。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

volume weighted average price vs simple average price market clearing
