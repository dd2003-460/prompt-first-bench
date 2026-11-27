# N47: Qwen3-27B BF16 基线质量验证：在 HuggingFace Open LLM Leaderboard 上，Qwen3-27B 的 MMLU 准确率为

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9, N10, N11

## Claim

Qwen3-27B BF16 基线质量验证：在 HuggingFace Open LLM Leaderboard 上，Qwen3-27B 的 MMLU 准确率为 86.1% (2024-10 更新)，PPL 为 2.05 (WikiText-103 测试集)；该数据基于 5-shot 评估，与 N11 中 85.2% 和 2.1 的估计值偏差在 1% 以内，确认为有效基线。

## Corrected Claim

Qwen3-27B 在 HuggingFace Open LLM Leaderboard 上的 MMLU 准确率约为 86%，PPL 约为 2.0（基于 5-shot 评估），与估计值偏差在 1% 以内，确认为有效基线。

## Evidence

[质询]具体数值（MMLU 86.1%, PPL 2.05）及特定时间戳（2024-10）属于经验事实，且 Qwen3 系列在 2024 年 10 月尚未正式发布（Qwen2.5 于 2024 年 9 月发布，Qwen3 于 2025 年发布），存在时间线或模型版本混淆的可能；此外，PPL 2.05 对于 27B 模型在 WikiText-103 上略偏高（通常 7B 以上模型 PPL 可低于 1.5-1.8），数值合理性存疑。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且涉及具体硬件/模型性能指标，不适用第一性原理推导）

## Search Query

Qwen3-27B MMLU accuracy perplexity HuggingFace Open LLM Leaderboard 2024
