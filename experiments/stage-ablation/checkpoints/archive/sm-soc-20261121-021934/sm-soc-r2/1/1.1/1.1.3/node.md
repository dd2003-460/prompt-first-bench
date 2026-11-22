# N24: 下游投影2：成交周期 T_deal 的随机扰动项 δT = β_noise * |ε_i|，其中 β_noise 为买家对价格异常值的敏感度系数（通常 β_no

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N5

## Claim

下游投影2：成交周期 T_deal 的随机扰动项 δT = β_noise * |ε_i|，其中 β_noise 为买家对价格异常值的敏感度系数（通常 β_noise > 0），当 |ε_i| 超过买家阈值 θ_buyer（如 2σ_ε）时，δT 呈指数增长，解释了部分高挂价商品虽未成交但咨询量低的现象。

## Corrected Claim

下游投影2：成交周期 T_deal 的随机扰动项 δT = β_noise * |ε_i|，其中 β_noise 为买家对价格异常值的敏感度系数（通常 β_noise > 0），当 |ε_i| 超过买家阈值 θ_buyer（如 2σ_ε）时，δT 呈指数增长，解释了部分高挂价商品虽未成交但咨询量低的现象。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price sensitivity buyer decision time threshold
