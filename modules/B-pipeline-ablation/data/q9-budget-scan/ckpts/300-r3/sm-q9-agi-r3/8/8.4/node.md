# N121: 人类反馈延迟的临界点分析：当 T_cycle > 15min 时，人类注意力衰减导致纠错效率下降；量化指标为 Attention_Decay_Rate = ex

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

人类反馈延迟的临界点分析：当 T_cycle > 15min 时，人类注意力衰减导致纠错效率下降；量化指标为 Attention_Decay_Rate = exp(-lambda * T_wait)，其中 lambda 约为 0.05/min，意味着等待 15min 后注意力保留率约为 e^-0.75 ≈ 47%，低于 50% 阈值时自动修正收益超过人工干预。

## Corrected Claim

在基于单指数衰减模型的假设下，若设定注意力衰减系数 lambda 约为 0.05/min，则等待 15min 后注意力保留率约为 47%。此时若低于 50% 阈值，理论上自动修正的收益可能超过人工干预，但该模型参数需根据具体任务场景校准。

## Evidence

[质询]该陈述将具体的认知心理学参数（lambda=0.05/min）和工程阈值（15min）作为既定事实呈现，但缺乏实证数据支持。注意力衰减并非简单的单指数衰减过程，且不同任务复杂度下 lambda 差异巨大，0.05/min 这一特定数值属于经验拟合参数，无法从第一性原理严格推导，存在过度简化和参数武断的风险。 | 逻辑自洽（数学计算 e^-0.75≈0.472 正确，阈值判断逻辑通顺），但 source 为 knowledge 且无外部来源支持，属于具体经验参数，无法确证 lambda 值的普适性，故降级。
