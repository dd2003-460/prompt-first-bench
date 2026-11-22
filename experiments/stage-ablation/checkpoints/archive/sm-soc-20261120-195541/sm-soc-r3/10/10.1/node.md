# N203: 噪声临界值 σ_crit 的标定方法：通过蒙特卡洛模拟 1000 次买家决策过程，统计不同 σ_noise 值下买家咨询概率 P_consult 的下降斜率 d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

噪声临界值 σ_crit 的标定方法：通过蒙特卡洛模拟 1000 次买家决策过程，统计不同 σ_noise 值下买家咨询概率 P_consult 的下降斜率 dP_consult/dσ；σ_crit 定义为斜率绝对值首次超过 0.5 的 σ 值，预期 σ_crit ∈ [0.10, 0.15]。

## Corrected Claim

噪声临界值 σ_crit 的标定方法：通过蒙特卡洛模拟 1000 次买家决策过程，统计不同 σ_noise 值下买家咨询概率 P_consult 的下降斜率 dP_consult/dσ；σ_crit 定义为斜率绝对值首次超过 0.5 的 σ 值，预期 σ_crit ∈ [0.10, 0.15]。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

monte carlo simulation buyer consultation probability noise threshold calibration
