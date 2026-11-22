# N353: 成交量权重 w_vol 与时间衰减权重 w_time 的组合方式：w_i = w_vol_i * w_time_i，其中 w_vol_i = Q_i / Σ(Q

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

成交量权重 w_vol 与时间衰减权重 w_time 的组合方式：w_i = w_vol_i * w_time_i，其中 w_vol_i = Q_i / Σ(Q_j)，需验证乘法组合是否引入偏差

## Corrected Claim

成交量权重 w_vol 与时间衰减权重 w_time 的组合方式：w_i = w_vol_i * w_time_i，其中 w_vol_i = Q_i / Σ(Q_j)，需验证乘法组合是否引入偏差

## Evidence

先验知识/题面给定，逻辑校验通过
