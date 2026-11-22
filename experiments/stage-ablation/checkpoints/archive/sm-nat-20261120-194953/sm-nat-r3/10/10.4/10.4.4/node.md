# N181: T_i 的分布模型：在全量驻留状态下，对象 i 的驻留时间 T_i 服从指数分布，参数 λ_i = u * (R_i / R_max)，其中 R_max 为最大

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83, N84

## Claim

T_i 的分布模型：在全量驻留状态下，对象 i 的驻留时间 T_i 服从指数分布，参数 λ_i = u * (R_i / R_max)，其中 R_max 为最大请求率；该模型假设更新事件独立且与请求频率成正比，需验证该假设在 Pareto 分布下的适用性

## Corrected Claim

T_i 的分布模型：在全量驻留状态下，对象 i 的驻留时间 T_i 服从指数分布，参数 λ_i = u * (R_i / R_max)，其中 R_max 为最大请求率；该模型假设更新事件独立且与请求频率成正比，需验证该假设在 Pareto 分布下的适用性

## Evidence

先验知识/题面给定，逻辑校验通过
