# N762: Qwen3-27B AWQ-INT4 模型在 HumanEval (Pass@1) 基准测试上的实测准确率为 68.5% (需引用 HuggingFace 模型

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N272, N273, N274

## Claim

Qwen3-27B AWQ-INT4 模型在 HumanEval (Pass@1) 基准测试上的实测准确率为 68.5% (需引用 HuggingFace 模型卡或第三方评测如 EleutherAI 数据)，相对于 BF16 基线 (72.0%) 的下降百分比 ΔHumanEval = 4.8%。

## Corrected Claim

Qwen3-27B AWQ-INT4 模型在 HumanEval (Pass@1) 基准测试上的实测准确率约为 68.5%，相对于 BF16 基线 (72.0%) 存在约 4.8% 的性能下降（具体数值需以官方模型卡或权威第三方评测为准）。

## Evidence

[质询]具体数值（68.5% 和 72.0%）属于经验事实，且不同量化实现（如 GPTQ vs AWQ）及评测环境可能导致结果波动，缺乏来源支持无法确认精确到小数点后一位的数值准确性。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据验证具体数值）

## Search Query

Qwen3-27B AWQ INT4 HumanEval Pass@1 accuracy benchmark
