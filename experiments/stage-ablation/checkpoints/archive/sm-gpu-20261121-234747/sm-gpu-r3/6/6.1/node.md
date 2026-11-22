# N138: Qwen3-27B的hidden_size、num_hidden_layers、num_attention_heads等架构参数，需从HuggingFace官方

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

Qwen3-27B的hidden_size、num_hidden_layers、num_attention_heads等架构参数，需从HuggingFace官方模型卡片的config.json中提取，用于计算各精度下的权重大小

## Corrected Claim

Qwen3-27B的hidden_size、num_hidden_layers、num_attention_heads等架构参数通常可从HuggingFace官方模型卡片的config.json中提取，用于计算各精度下的权重大小。

## Evidence

[质询]该陈述包含具体的经验性事实（Qwen3-27B的具体架构参数值），且声称需从特定来源提取，但当前无可用外部来源验证这些具体数值或提取路径的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json hidden_size num_hidden_layers HuggingFace
