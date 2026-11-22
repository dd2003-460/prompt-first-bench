# N475: Qwen3-27B 的 num_key_value_heads (KV Heads) 确认为 8，来源为 HuggingFace Qwen/Qwen3-27B 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N196

## Claim

Qwen3-27B 的 num_key_value_heads (KV Heads) 确认为 8，来源为 HuggingFace Qwen/Qwen3-27B 模型仓库的 config.json 文件字段 'num_key_value_heads': 8，该参数与 num_attention_heads (32) 共同确定 GQA 比例 4:1，而非 N196 中声称的 8:1（N196 错误地使用了 64 作为分子，实际 Q Heads 为 32）。

## Corrected Claim

Qwen3-27B 采用 GQA 机制，其 num_key_value_heads 与 num_attention_heads 的比例为 4:1（基于 num_attention_heads=32, num_key_value_heads=8 的假设，需进一步核实具体头数配置）。

## Evidence

[质询]该陈述包含具体的模型架构参数（num_key_value_heads=8, num_attention_heads=32），属于经验事实。虽然逻辑上 32/8=4:1 的 GQA 比例计算自洽，且与 Qwen3 系列通常采用 GQA 的设计一致，但缺乏直接来源验证具体数值是否为 8 和 32（例如，若 heads 为 64 且 kv_heads 为 8，则比例为 8:1，需确认分子确实是 32 而非 64）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法确认具体参数值）

## Search Query

Qwen3-27B config.json num_key_value_heads site:huggingface.co
