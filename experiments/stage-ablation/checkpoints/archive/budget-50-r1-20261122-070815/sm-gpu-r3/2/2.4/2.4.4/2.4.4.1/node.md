# N233: Qwen3-27B 在 BF16 精度下的参考 Perplexity (PPL) 基准值（基于 WikiText-2 或 C4 数据集），用于计算 Delta 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N68

## Claim

Qwen3-27B 在 BF16 精度下的参考 Perplexity (PPL) 基准值（基于 WikiText-2 或 C4 数据集），用于计算 Delta PPL 的基准分母，需从 Qwen3 官方技术报告或 HuggingFace 模型卡片获取具体数值（如 5.2 或 5.4）。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的参考 Perplexity (PPL) 基准值需从 Qwen3 官方技术报告或 HuggingFace 模型卡片获取具体数值，用于计算 Delta PPL 的基准分母。

## Evidence

[质询]该陈述包含具体的经验数值（如 5.2 或 5.4），属于硬件/模型性能指标，无法从第一性原理推导，且当前无可用来源支持具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体 PPL 数值）

## Search Query

Qwen3-27B BF16 perplexity wikitext2 benchmark official
