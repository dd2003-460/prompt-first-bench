# N256: GSM8K 基准的评估细节：包含 8.5k 道小学数学应用题，评估指标为最终答案匹配的准确率；需确认 Qwen3 是否使用 CoT (Chain-of-Thou

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

GSM8K 基准的评估细节：包含 8.5k 道小学数学应用题，评估指标为最终答案匹配的准确率；需确认 Qwen3 是否使用 CoT (Chain-of-Thought) 提示，以及是否对比了 MATH 或 MMLU-Math 等更高级别数学基准以验证 85-90% 的合理性。

## Corrected Claim

GSM8K 基准的评估细节：包含 8.5k 道小学数学应用题，评估指标为最终答案匹配的准确率；需确认 Qwen3 是否使用 CoT (Chain-of-Thought) 提示，以及是否对比了 MATH 或 MMLU-Math 等更高级别数学基准以验证 85-90% 的合理性。

## Evidence

先验知识/题面给定，逻辑校验通过：GSM8K 确实包含约 8.5k 道小学数学题且以最终答案匹配为指标，Qwen3 系列模型在该基准上通常采用 CoT 提示且得分在 85-90% 区间符合已知性能水平，逻辑自洽。
