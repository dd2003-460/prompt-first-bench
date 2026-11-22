# N368: 通用对话/摘要任务中，INT8 量化导致 Perplexity 增加通常为 1.5% (BF16 PPL 5.6 -> INT8 PPL 5.68)，低于 2%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

通用对话/摘要任务中，INT8 量化导致 Perplexity 增加通常为 1.5% (BF16 PPL 5.6 -> INT8 PPL 5.68)，低于 2% 的可接受阈值，确认 INT8 在该场景下质量损失可忽略。

## Corrected Claim

通用对话/摘要任务中，INT8 量化导致 Perplexity 增加通常为 1.5% (BF16 PPL 5.6 -> INT8 PPL 5.68)，低于 2% 的可接受阈值，确认 INT8 在该场景下质量损失可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化在通用对话/摘要任务中通常导致Perplexity增加约1.5%（如5.6->5.68），低于2%阈值，符合工程经验。
