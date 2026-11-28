# N143: ρ = (I - P_single) / (1 - P_single) 公式的有效性前提是 Agent 错误独立同分布；若存在系统性偏差（如所有 Agent 均

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N56

## Claim

ρ = (I - P_single) / (1 - P_single) 公式的有效性前提是 Agent 错误独立同分布；若存在系统性偏差（如所有 Agent 均受某类数据污染），该公式会低估真实相关性，需引入偏误修正项 β_bias，修正后公式为 ρ_corrected = (I - P_single - β_bias) / (1 - P_single) [待核验]

## Corrected Claim

ρ = (I - P_single) / (1 - P_single) 公式的有效性通常假设 Agent 错误独立；若存在系统性偏差，该公式可能无法准确反映真实相关性，需根据具体偏差模型引入相应的修正项，而非通用的 β_bias 线性修正。

## Evidence

[质询]该公式及其修正项 β_bias 缺乏标准的统计学或机器学习理论支撑，属于特定场景下的启发式假设，且‘系统性偏差导致低估相关性’的因果机制及修正公式的具体形式（线性减去 β_bias）在通用理论中并非标准结论，存在定义模糊和过度拟合特定问题的风险。 | 先验知识/题面给定，逻辑校验通过（公式结构在代数上自洽，量纲合理），但作为经验性修正模型，其普适性和具体形式缺乏广泛公认的理论基础，故降级为定性表述。

## Search Query

systematic bias correction LLM agent agreement rate formula
