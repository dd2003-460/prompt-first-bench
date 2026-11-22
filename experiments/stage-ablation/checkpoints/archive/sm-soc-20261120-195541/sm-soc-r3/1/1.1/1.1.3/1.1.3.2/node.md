# N79: P_market 加权中位数的空间衰减修正：在 N25 定义基础上增加空间权重 w_space = exp(-λ_space * d_i)，其中 d_i 为成交

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

P_market 加权中位数的空间衰减修正：在 N25 定义基础上增加空间权重 w_space = exp(-λ_space * d_i)，其中 d_i 为成交地点与当前商品地点的地理距离，λ_space 需通过空间计量模型估计；若 λ_space 显著，则 P_market 需按区域细分，否则跨区交易会导致公允价估计偏差，影响卖家挂价合理性判断。

## Corrected Claim

在 N25 定义基础上，可考虑引入基于地理距离的空间权重（如 w_space = exp(-λ_space * d_i)）以修正 P_market 加权中位数。若空间衰减效应显著，建议按区域细分 P_market，以减少跨区交易对公允价估计的偏差，从而提升卖家挂价合理性判断的准确性。

## Evidence

[质询]该陈述包含具体的参数估计方法（空间计量模型）和特定的数学形式（指数衰减），属于经验性建模假设，无法从第一性原理严格推导，且缺乏来源支持其作为标准做法的普适性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

spatial decay weight market price geographic distance second-hand trading
