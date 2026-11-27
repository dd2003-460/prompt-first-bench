# N390: FP8量化对Qwen3-27B通用对话任务（MMLU）的质量损失具体数值为[待核验]，需参考Qwen官方技术报告或第三方评测，预期损失范围为0.5%-1.0%，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N162

## Claim

FP8量化对Qwen3-27B通用对话任务（MMLU）的质量损失具体数值为[待核验]，需参考Qwen官方技术报告或第三方评测，预期损失范围为0.5%-1.0%，若低于1.0%则FP8适用于通用场景

## Corrected Claim

FP8量化对Qwen3-27B通用对话任务（MMLU）的质量损失具体数值需参考Qwen官方技术报告或第三方评测，预期损失范围约为0.5%-1.0%，若低于1.0%则FP8适用于通用场景

## Evidence

[质询]参考来源[1]仅提供了MathVision评测的提示词格式说明，完全未包含MMLU基准测试的具体数值或FP8量化带来的质量损失百分比，无法直接支持或证伪0.5%-1.0%的预期损失范围。 | 经验事实，逻辑自洽但缺来源支持（来源[1]与MMLU质量损失数值无关，仅涉及MathVision提示词）

## Search Query

Qwen3-27B FP8 quantization MMLU benchmark accuracy loss

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B-FP8&rut=14136281e1ef2fc006f2a2d3b080ee78368ef2e65dbc32e90d1e2479a0f7bd3d', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B-FP8 · Hugging Face'}
