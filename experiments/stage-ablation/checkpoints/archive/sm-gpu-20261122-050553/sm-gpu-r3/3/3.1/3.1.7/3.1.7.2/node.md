# N214: Qwen3-27B 使用 AWQ (INT8) 量化后在 HumanEval 基准上的准确率变化：基线 BF16 Pass@1 约 50-55% [待核验具体版

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69

## Claim

Qwen3-27B 使用 AWQ (INT8) 量化后在 HumanEval 基准上的准确率变化：基线 BF16 Pass@1 约 50-55% [待核验具体版本]，AWQ INT8 后 Pass@1 下降约 1-3 个百分点，即 47-54%，在代码生成任务上退化略高于通用知识任务，但仍通常在 5% 容忍阈值内。

## Corrected Claim

Qwen3-27B 使用 AWQ (INT8) 量化后在 HumanEval 基准上的准确率通常会有轻微下降（约1-3个百分点），具体数值取决于模型版本和量化实现，但通常仍在可接受范围内。

## Evidence

[质询]具体数值（基线50-55%，下降1-3个百分点）属于特定模型版本和量化配置下的经验事实，缺乏来源支持，且不同量化实现（如GPTQ vs AWQ）或模型微调版本可能导致数值偏差。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B AWQ INT8 HumanEval pass@1 accuracy
