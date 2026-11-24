# N311: K_event 共享随机源定义：事件触发过程服从泊松分布，参数 λ_month = 2.5（即每月平均2.5次热点事件），单次事件流量增幅 ΔK_event 服

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N102

## Claim

K_event 共享随机源定义：事件触发过程服从泊松分布，参数 λ_month = 2.5（即每月平均2.5次热点事件），单次事件流量增幅 ΔK_event 服从对数正态分布，均值 ln(1.5)≈0.405，标准差 σ_ln ≈ 0.3，持续时间 T_event 服从指数分布，均值 90分钟（1.5小时）。

## Corrected Claim

K_event 共享随机源定义：事件触发过程服从泊松分布，参数 λ_month = 2.5（即每月平均2.5次热点事件），单次事件流量增幅 ΔK_event 服从对数正态分布，均值 ln(1.5)≈0.405，标准差 σ_ln ≈ 0.3，持续时间 T_event 服从指数分布，均值 90分钟（1.5小时）。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松、对数正态、指数分布均为标准随机过程模型，参数量级（月均2.5次、增幅均值1.5倍、持续1.5小时）符合热点事件的一般工程直觉，无内部矛盾。

## Search Query

viral video traffic spike poisson process lognormal distribution duration
