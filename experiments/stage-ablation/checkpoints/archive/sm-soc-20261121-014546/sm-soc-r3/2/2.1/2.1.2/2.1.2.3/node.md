# N191: 下游投影 2：买家决策边界，当 SNR < 1.5 时，买家后验信念 P(quality|price) 更新幅度小于先验方差，导致咨询率 ΔQ_inquiry 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N54

## Claim

下游投影 2：买家决策边界，当 SNR < 1.5 时，买家后验信念 P(quality|price) 更新幅度小于先验方差，导致咨询率 ΔQ_inquiry ≈ 0，具体公式为 ΔQ = k * max(0, SNR - SNR_crit)。

## Corrected Claim

在简化的阈值模型假设下，当 SNR 低于临界值（如 1.5）时，买家咨询率的边际变化趋近于零，具体形式可近似为 ΔQ ≈ k * max(0, SNR - SNR_crit)，但该模型忽略了买家异质性和非线性效应。

## Evidence

[质询]该陈述将复杂的买家决策行为简化为单一的线性阈值函数（ΔQ = k * max(0, SNR - SNR_crit)），且断言在 SNR < 1.5 时咨询率变化严格为 0。这忽略了价格信号的非线性影响、买家异质性（不同买家对 SNR 敏感度不同）以及先验分布的具体形态，属于过度简化的经验模型，缺乏普适的理论推导支持。 | source=knowledge，逻辑上自洽（阈值模型在简化假设下成立），但作为经验事实/具体模型参数，缺乏外部来源直接支持或第一性原理严格推导，依据经验事实排除条款降级。

## Search Query

bayesian updating buyer inquiry rate signal to noise ratio
