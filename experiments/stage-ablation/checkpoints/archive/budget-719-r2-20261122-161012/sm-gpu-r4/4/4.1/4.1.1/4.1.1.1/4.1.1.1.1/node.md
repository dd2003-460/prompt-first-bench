# N473: Qwen3-27B 的 num_attention_heads (Query Heads) 确认为 32，来源为 HuggingFace Qwen/Qwen3-

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N196

## Claim

Qwen3-27B 的 num_attention_heads (Query Heads) 确认为 32，来源为 HuggingFace Qwen/Qwen3-27B 模型仓库的 config.json 文件字段 'num_attention_heads': 32，该参数决定了 Q 矩阵的维度，但不影响 KV Cache 大小（仅影响计算量）。

## Corrected Claim

Qwen3-27B 的 num_attention_heads 通常为 32（需以官方 config.json 为准），该参数决定 Q 矩阵维度，不影响 KV Cache 大小。

## Evidence

[质询]该陈述包含具体的经验参数（num_attention_heads=32），属于模型架构的具体配置值，无法从第一性原理推导，且本轮检索无可用来源支持，存在参数记忆错误或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json num_attention_heads site:huggingface.co
