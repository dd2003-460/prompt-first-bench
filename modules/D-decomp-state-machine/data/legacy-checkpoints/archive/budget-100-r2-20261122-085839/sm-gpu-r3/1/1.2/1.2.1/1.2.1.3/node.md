# N130: Qwen3-27B 配置文件中 head_dim（头维度）的具体数值，通常等于 hidden_size / num_attention_heads，需从 con

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

Qwen3-27B 配置文件中 head_dim（头维度）的具体数值，通常等于 hidden_size / num_attention_heads，需从 config.json 或计算得出，常见值为 128 或 160，用于计算每个头的向量长度。

## Corrected Claim

Qwen3-27B 配置文件中 head_dim（头维度）的具体数值通常等于 hidden_size / num_attention_heads，需从 config.json 或计算得出，具体值取决于模型架构设计。

## Evidence

[质询]该陈述包含具体的经验参数（head_dim 常见值为 128 或 160），属于经验事实，无法仅从第一性原理严格推出具体数值，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json head_dim hidden_size
