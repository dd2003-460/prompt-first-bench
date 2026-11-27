# N163: 时间窗口敏感性分析：48小时窗口的选择对 P(0) 估计的偏差，量化为当窗口从 48h 变为 24h 时，λ_consult_after 的估计值变化率 Δλ/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

时间窗口敏感性分析：48小时窗口的选择对 P(0) 估计的偏差，量化为当窗口从 48h 变为 24h 时，λ_consult_after 的估计值变化率 Δλ/λ = (λ_24h - λ_48h) / λ_48h，若 |Δλ/λ| > 0.1 则说明衰减过程非平稳，需引入时间依赖的强度函数 λ(t)。

## Corrected Claim

时间窗口敏感性分析：48小时窗口的选择对 P(0) 估计的偏差，量化为当窗口从 48h 变为 24h 时，λ_consult_after 的估计值变化率 Δλ/λ = (λ_24h - λ_48h) / λ_48h，若 |Δλ/λ| > 0.1 则说明衰减过程非平稳，需引入时间依赖的强度函数 λ(t)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

sensitivity analysis time window Poisson process rate estimation
