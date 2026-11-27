# N174: GSM8K 任务中，中间推理步骤（Chain-of-Thought）长度对量化误差的累积效应：随着 CoT 长度增加（如从 100 tokens 到 500 t

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N51

## Claim

GSM8K 任务中，中间推理步骤（Chain-of-Thought）长度对量化误差的累积效应：随着 CoT 长度增加（如从 100 tokens 到 500 tokens），INT8 量化导致的最终答案错误率增加比例（通常呈线性或超线性增长）

## Corrected Claim

GSM8K 任务中，随着 Chain-of-Thought 推理步骤长度增加，INT8 量化导致的最终答案错误率通常会增加，但具体的增长比例和模式（线性/超线性）及特定 token 范围下的表现需依赖具体实验数据验证。

## Evidence

[质询]该陈述包含具体的经验性数值范围（100-500 tokens）和特定的增长模式（线性或超线性），属于经验事实。缺乏直接来源支持时，无法确认INT8量化误差累积是否严格遵循此特定模式或量级，可能存在非线性波动或依赖具体模型架构的差异。 | 经验事实，逻辑自洽（量化误差随推理步数累积符合直觉）但缺来源支持，且检索无可用来源，无法验证具体数值范围和增长模式。

## Search Query

INT8 quantization error accumulation Chain-of-Thought length GSM8K
