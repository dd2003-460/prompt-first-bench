# N256: r_high 的分布参数估计：假设卖家挂价 P_ask 服从对数正态分布 LogNormal(μ_log, σ_log)，其中 μ_log 为成交价中位数对应的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

r_high 的分布参数估计：假设卖家挂价 P_ask 服从对数正态分布 LogNormal(μ_log, σ_log)，其中 μ_log 为成交价中位数对应的对数均值，σ_log 为价格离散度（典型值 0.2-0.4），则 r_high = 1 - Φ((ln(1.15) - 0) / σ_log)，需代入具体 σ_log 计算。

## Corrected Claim

r_high 的分布参数估计：假设卖家挂价 P_ask 服从对数正态分布 LogNormal(μ_log, σ_log)，其中 μ_log 为成交价中位数对应的对数均值，σ_log 为价格离散度（典型值 0.2-0.4），则 r_high = 1 - Φ((ln(1.15) - 0) / σ_log)，需代入具体 σ_log 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布定义及概率计算逻辑自洽，σ_log典型值符合市场常识。

## Search Query

log-normal distribution of asking prices in second-hand markets variance estimation
