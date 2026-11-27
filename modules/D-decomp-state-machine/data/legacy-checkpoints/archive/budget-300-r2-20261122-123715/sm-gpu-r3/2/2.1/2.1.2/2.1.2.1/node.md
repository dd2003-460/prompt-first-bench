# N198: Qwen3-27B BF16 基准模型在 HumanEval (164 problems) 上的 Pass@1 准确率为 68.0%，在 MBPP (500 p

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54

## Claim

Qwen3-27B BF16 基准模型在 HumanEval (164 problems) 上的 Pass@1 准确率为 68.0%，在 MBPP (500 problems) 上的 Pass@1 准确率为 72.0%，作为代码生成质量评估的绝对基线。

## Corrected Claim

Qwen3-27B BF16 基准模型在 HumanEval 和 MBPP 上的 Pass@1 准确率分别约为 68% 和 72%，作为代码生成质量评估的绝对基线。

## Evidence

[质询]具体数值（68.0% 和 72.0%）属于经验事实，且不同评测设置（如温度、采样次数、提示词格式）会导致结果波动，缺乏来源支持无法确认该特定基准测试的精确数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B HumanEval Pass@1 score MBPP baseline accuracy
