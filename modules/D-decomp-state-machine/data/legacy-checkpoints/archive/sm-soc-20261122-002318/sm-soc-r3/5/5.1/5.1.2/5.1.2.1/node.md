# N217: 曝光权重衰减因子 w_decay 与时间衰减参数 δ 的独立估计：w_decay ≈ 0.15 是基于线性假设的简化值，需通过 A/B 测试数据回归 ln(Ex

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N77

## Claim

曝光权重衰减因子 w_decay 与时间衰减参数 δ 的独立估计：w_decay ≈ 0.15 是基于线性假设的简化值，需通过 A/B 测试数据回归 ln(Exposure) = β0 + β1*IsPriceDrop + β2*ln(1 - t/T_decay) + ε 来分别估计 β1 (对应 w_decay) 和 β2 (对应 δ)，并检验交互项是否显著。

## Corrected Claim

曝光权重衰减因子 w_decay 与时间衰减参数 δ 的独立估计：w_decay 的具体数值（如 0.15）需基于特定业务场景数据确定，通常需通过 A/B 测试数据回归 ln(Exposure) = β0 + β1*IsPriceDrop + β2*ln(1 - t/T_decay) + ε 来分别估计 β1 (对应 w_decay) 和 β2 (对应 δ)，并检验交互项是否显著。

## Evidence

[质询]该陈述包含具体的经验数值（w_decay ≈ 0.15）和特定的统计模型设定，属于经验事实而非第一性原理可推导内容；且缺乏外部来源支持该具体数值或模型的有效性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

regression model exposure decay factor price drop algorithm A/B test
