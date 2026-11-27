# N103: 曝光加成函数 f_exposure(P_ask) 的具体形式：定义为 f_exposure = E[Exposure(P_ask)] / E[Exposure(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

曝光加成函数 f_exposure(P_ask) 的具体形式：定义为 f_exposure = E[Exposure(P_ask)] / E[Exposure(μ_p)]，其中 E[Exposure] 为期望曝光量。若假设线性关系，则 f_exposure = 1 + β_exp * (P_ask - μ_p)/μ_p，其中 β_exp 为价格敏感度系数，需通过A/B测试或日志回归估计。

## Corrected Claim

曝光加成函数 f_exposure(P_ask) 的具体形式：定义为 f_exposure = E[Exposure(P_ask)] / E[Exposure(μ_p)]，其中 E[Exposure] 为期望曝光量。若假设线性关系，则 f_exposure = 1 + β_exp * (P_ask - μ_p)/μ_p，其中 β_exp 为价格敏感度系数，需通过A/B测试或日志回归估计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

exposure premium linear model price sensitivity marketplace
