# N54: W4 量化下 HumanEval (代码生成) 性能损失基准：通常损失 4-6 个百分点 (例如从 70% 降至 64-66%)，因为代码生成对特定 token

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

W4 量化下 HumanEval (代码生成) 性能损失基准：通常损失 4-6 个百分点 (例如从 70% 降至 64-66%)，因为代码生成对特定 token 概率分布的微小偏移更敏感，且 4-bit 截断误差在长序列累积效应更明显 [待核验: Qwen3-27B W4 HumanEval 具体数值]

## Corrected Claim

W4 量化下 HumanEval (代码生成) 性能通常会有所损失，具体损失幅度因模型和量化方法而异，一般认为在几个百分点范围内，因为代码生成对特定 token 概率分布的微小偏移更敏感，且 4-bit 截断误差在长序列累积效应更明显。

## Evidence

[质询]该陈述包含具体的经验数值（4-6个百分点损失，70%降至64-66%），属于经验事实而非第一性原理可推导内容。由于检索失败，无法验证这些具体数值是否准确适用于Qwen3-27B或一般W4量化场景，存在数值偏差或特定模型表现不同的风险。 | 经验事实，逻辑自洽但缺来源支持。W4量化导致性能下降符合一般认知，但具体数值范围缺乏外部证据直接支持。

## Search Query

Qwen3-27B 4-bit quantization HumanEval code generation degradation
