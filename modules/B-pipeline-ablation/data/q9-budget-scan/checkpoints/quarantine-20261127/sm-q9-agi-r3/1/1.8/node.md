# N13: Prompt 工程策略需采用 Chain-of-Thought (CoT) 与 Self-Consistency 结合，对于数学/逻辑推理任务，采样 k=5 次

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

Prompt 工程策略需采用 Chain-of-Thought (CoT) 与 Self-Consistency 结合，对于数学/逻辑推理任务，采样 k=5 次并投票，可将准确率从 70% 提升至 85%，但推理成本增加 5 倍。

## Corrected Claim

Prompt 工程策略采用 Chain-of-Thought (CoT) 与 Self-Consistency 结合，对于数学/逻辑推理任务，通过多次采样（如 k=5）并投票，通常可显著提升准确率，但推理成本随采样次数线性增加。

## Evidence

[质询]数值过于具体且缺乏普适性：'70%提升至85%'和'成本增加5倍'是特定实验条件下的经验数据，并非CoT+Self-Consistency的固有属性或第一性原理推论，不同模型、任务难度下差异巨大。 | 先验知识/题面给定，逻辑校验通过（Self-Consistency确实通过多次采样投票提升准确率，且线性增加采样次数会线性增加推理成本，量级关系合理），但具体数值为经验事实，无来源支持，故降级。
