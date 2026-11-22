# N363: Qwen3-27B 的 num_attention_heads 具体数值为 32，该参数直接决定 Q 矩阵维度及计算复杂度，需从 HuggingFace Qwe

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N128

## Claim

Qwen3-27B 的 num_attention_heads 具体数值为 32，该参数直接决定 Q 矩阵维度及计算复杂度，需从 HuggingFace Qwen3-27B config.json 中 'num_attention_heads' 字段获取以验证架构一致性。

## Corrected Claim

Qwen3-27B 的 num_attention_heads 具体数值需从 HuggingFace Qwen3-27B config.json 中 'num_attention_heads' 字段获取以验证架构一致性，该参数直接决定 Q 矩阵维度及计算复杂度。

## Evidence

[质询]具体数值 32 属于经验事实（模型架构参数），无法从第一性原理推导，且本轮检索无可用来源支持，存在数值错误的可能性（例如实际为 40 或其他值）。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json num_attention_heads HuggingFace
