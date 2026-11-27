# N287: λ_decay 的分布形态与不确定性：λ_decay 不服从固定常数，而是服从对数正态分布 LogNormal(μ_λ, σ_λ²)，其中 μ_λ 和 σ_λ 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91

## Claim

λ_decay 的分布形态与不确定性：λ_decay 不服从固定常数，而是服从对数正态分布 LogNormal(μ_λ, σ_λ²)，其中 μ_λ 和 σ_λ 需通过时间序列分解（如 ARIMA 模型）估计；当 σ_λ > 0.2 时，T_effective 的置信区间宽度超过 50%，导致干预窗口预测失效。

## Corrected Claim

λ_decay 不服从固定常数，而是服从对数正态分布 LogNormal(μ_λ, σ_λ²)，其中 μ_λ 和 σ_λ 需通过时间序列分解估计；当 σ_λ 较大时，T_effective 的置信区间宽度显著增加，可能导致干预窗口预测精度下降。

## Evidence

[质询]该陈述包含具体的经验性阈值（σ_λ > 0.2 导致置信区间宽度超过 50%），这属于特定模型假设下的统计推导结果，而非普适的物理或数学定律。不同时间序列分解方法（如 ARIMA 与其他状态空间模型）对参数不确定性的传播计算不同，该具体数值阈值缺乏通用性，且“干预窗口预测失效”的定义模糊，属于强经验假设。 | 先验知识/题面给定，逻辑校验通过。虽然对数正态分布常用于描述衰减率等正偏态参数，且不确定性传播导致置信区间变宽符合统计直觉，但具体的阈值 0.2 和 50% 宽度属于特定模型下的经验参数，非第一性原理可严格推导的普适事实，故降级为定性表述。

## Search Query

distribution of seller adaptation rate in market interventions
