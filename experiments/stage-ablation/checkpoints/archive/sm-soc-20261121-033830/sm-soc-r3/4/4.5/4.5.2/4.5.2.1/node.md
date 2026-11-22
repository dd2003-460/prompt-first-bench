# N260: 强制价格上限 (N18-A) 下的佣金率变化：若佣金率 k 恒定，则 Δcommission_rate = 0，但佣金基数降低导致总佣金收入下降；需计算新均衡下

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85

## Claim

强制价格上限 (N18-A) 下的佣金率变化：若佣金率 k 恒定，则 Δcommission_rate = 0，但佣金基数降低导致总佣金收入下降；需计算新均衡下的有效佣金率 k_eff_new = k * (P_median * (1-k) / P_old) 以量化收入变化。

## Corrected Claim

强制价格上限 (N18-A) 下的佣金率变化：若佣金率 k 恒定，则 Δcommission_rate = 0，但佣金基数降低导致总佣金收入下降；需计算新均衡下的有效佣金率 k_eff_new = k * (P_median * (1-k) / P_old) 以量化收入变化。

## Evidence

先验知识/题面给定，逻辑校验通过
