# N92: Qwen3-27B 在 AWQ-INT8 量化下，WikiText2 数据集的 Perplexity (PPL) 绝对值约为 5.8-6.2，相较于 BF16 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 AWQ-INT8 量化下，WikiText2 数据集的 Perplexity (PPL) 绝对值约为 5.8-6.2，相较于 BF16 基准 (约 5.5-5.7) 增加约 2-4%；具体数值需根据 HuggingFace 社区发布的 Qwen3-27B-AWQ-INT8 模型评测报告核验。

## Corrected Claim

Qwen3-27B 在 AWQ-INT8 量化下，WikiText2 数据集的 Perplexity (PPL) 相较于 BF16 基准会有轻微上升（通常约 2-4%），具体绝对数值需根据 HuggingFace 社区发布的 Qwen3-27B-AWQ-INT8 模型评测报告核验。

## Evidence

[质询]具体数值（PPL 5.8-6.2 及 BF16 基准 5.5-5.7）属于经验事实，缺乏来源支持，且不同量化实现或评测脚本可能导致数值波动，无法确认该特定区间是否准确。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B AWQ INT8 perplexity WikiText2 benchmark
