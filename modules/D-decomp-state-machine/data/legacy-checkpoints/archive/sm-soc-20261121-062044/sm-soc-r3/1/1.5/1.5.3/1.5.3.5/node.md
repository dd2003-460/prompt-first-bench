# N135: 右偏分布修正项：若 Δp 实际分布服从对数正态分布 ln(Δp) ~ N(μ_ln, σ_ln²)，则需将正态 CDF 替换为对数正态 CDF F_ln(Δp)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

右偏分布修正项：若 Δp 实际分布服从对数正态分布 ln(Δp) ~ N(μ_ln, σ_ln²)，则需将正态 CDF 替换为对数正态 CDF F_ln(Δp)，计算 P_no_inquiry = 1 - F_ln(Δp)，修正后的 μ_pct 和 σ_pct 需通过矩匹配法（Method of Moments）重新估计。

## Corrected Claim

右偏分布修正项：若 Δp 实际分布服从对数正态分布 ln(Δp) ~ N(μ_ln, σ_ln²)，则需将正态 CDF 替换为对数正态 CDF F_ln(Δp)，计算 P_no_inquiry = 1 - F_ln(Δp)，修正后的 μ_pct 和 σ_pct 需通过矩匹配法（Method of Moments）重新估计。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布常用于建模右偏正变量，矩匹配法是估计分布参数的标准统计方法，逻辑自洽且符合统计学原理。

## Search Query

log-normal distribution price change perception correction
