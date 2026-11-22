# N176: GSM8K 准确率从 80% 降至 76% 的下降值 4.0% 是基于 Few-Shot (5-shot) 设置，若使用 Zero-Shot 或 Chain-o

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

GSM8K 准确率从 80% 降至 76% 的下降值 4.0% 是基于 Few-Shot (5-shot) 设置，若使用 Zero-Shot 或 Chain-of-Thought (CoT) 提示，W4 量化的下降幅度可能扩大至 5-6%，因 CoT 依赖多步中间推理的精确性，对量化误差更敏感。

## Corrected Claim

GSM8K 准确率从 80% 降至 76% 的下降值 4.0% 是基于 Few-Shot (5-shot) 设置。理论上，若使用 Zero-Shot 或 Chain-of-Thought (CoT) 提示，由于 CoT 依赖多步中间推理的精确性，对量化误差可能更敏感，W4 量化的下降幅度可能会扩大，但具体数值需实证验证。

## Evidence

[质询]该陈述包含具体的经验性数值预测（Zero-Shot/CoT下下降幅度扩大至5-6%），这属于特定模型在特定量化方案下的实证结果，无法从第一性原理或数学公理中严格推导出来，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B GSM8K W4 quantization accuracy drop Chain-of-Thought sensitivity
