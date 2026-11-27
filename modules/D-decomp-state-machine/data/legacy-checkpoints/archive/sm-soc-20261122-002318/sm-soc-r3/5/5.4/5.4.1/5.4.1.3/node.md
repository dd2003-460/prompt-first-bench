# N240: 总成交量波动标准差 σ_total 的分解：σ_total = sqrt(σ_wait^2 + σ_panic^2 + 2 * ρ * σ_wait * σ_p

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

总成交量波动标准差 σ_total 的分解：σ_total = sqrt(σ_wait^2 + σ_panic^2 + 2 * ρ * σ_wait * σ_panic)，其中 ρ 为观望与抢购效应的协方差系数（通常为负，因为观望减少短期交易而抢购增加），需通过历史数据回归确定 ρ 的取值范围。

## Corrected Claim

总成交量波动标准差 σ_total 的分解：σ_total = sqrt(σ_wait^2 + σ_panic^2 + 2 * ρ * σ_wait * σ_panic)，其中 ρ 为观望与抢购效应的协方差系数（通常为负，因为观望减少短期交易而抢购增加），需通过历史数据回归确定 ρ 的取值范围。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合方差分解的基本数学原理（Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)），且对ρ为负值的经济直觉解释（观望与抢购的替代/对冲效应）合理。

## Search Query

volume volatility decomposition wait and panic buying covariance
