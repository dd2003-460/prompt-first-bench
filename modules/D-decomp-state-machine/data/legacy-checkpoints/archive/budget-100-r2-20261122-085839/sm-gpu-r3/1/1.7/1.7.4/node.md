# N51: INT8 量化下 GSM8K (数学推理) 性能损失基准：通常损失 2-4 个百分点 (例如从 90% 降至 87-88%)，高于 MMLU 的损失幅度，因为数

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N12

## Claim

INT8 量化下 GSM8K (数学推理) 性能损失基准：通常损失 2-4 个百分点 (例如从 90% 降至 87-88%)，高于 MMLU 的损失幅度，因为数学推理对中间步骤的精度更敏感 [待核验: Qwen3-27B 具体 GSM8K 基线及量化后数值]

## Corrected Claim

INT8 量化通常会导致 GSM8K 性能出现一定程度的损失，且由于数学推理对中间步骤精度更敏感，其损失幅度往往高于 MMLU 等知识密集型任务。具体损失数值（如 2-4 个百分点）取决于模型架构、量化算法及校准策略，需针对特定模型（如 Qwen3-27B）进行实测验证。

## Evidence

[质询]该陈述包含具体的经验数值（2-4个百分点损失、90%降至87-88%），属于经验事实而非第一性原理可推导内容。由于检索失败无外部来源支持，且不同模型架构、量化方法（如GPTQ, AWQ, SmoothQuant）及校准数据集对GSM8K的影响差异巨大，无法确认该特定数值范围具有普适性或针对Qwen3-27B的准确性。 | 经验事实，逻辑自洽（数学推理对精度敏感符合直觉）但缺来源支持，且具体数值缺乏实证依据。

## Search Query

Qwen3-27B INT8 GSM8K math reasoning benchmark degradation
