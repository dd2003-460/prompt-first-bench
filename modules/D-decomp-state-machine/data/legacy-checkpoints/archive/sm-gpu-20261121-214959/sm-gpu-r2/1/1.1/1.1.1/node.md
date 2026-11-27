# N37: Qwen3-27B 的 Transformer 层数（num_layers）为 64 层（修正 N28 中的 60 层错误，依据 Qwen3-27B 官方模型配

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7, N8, N9

## Claim

Qwen3-27B 的 Transformer 层数（num_layers）为 64 层（修正 N28 中的 60 层错误，依据 Qwen3-27B 官方模型配置文件 config.json 及 HuggingFace 模型卡）。

## Corrected Claim

Qwen3-27B 的 Transformer 层数（num_layers）据称约为 64 层（基于官方配置文件的常见报告，但当前缺乏直接来源验证）。

## Evidence

[质询]该陈述属于具体的硬件/模型架构规格（经验事实），且参考来源显示检索失败，无法通过外部证据直接验证其数值准确性（64层 vs 其他可能值）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法排除其他可能性）

## Search Query

Qwen3-27B config.json num_hidden_layers
