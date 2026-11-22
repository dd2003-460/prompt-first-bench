# N302: Qwen3-27B 的 num_kv_heads 确认为 8，依据 GQA 架构设计，num_attention_heads 为 64，GQA 比例为 8:1，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107, N108, N109

## Claim

Qwen3-27B 的 num_kv_heads 确认为 8，依据 GQA 架构设计，num_attention_heads 为 64，GQA 比例为 8:1，需从 config.json 的 'num_key_value_heads' 字段确认

## Corrected Claim

Qwen3-27B 采用 GQA 架构，num_attention_heads 为 64，num_kv_heads 推测为 8（比例 8:1），具体数值需以官方 config.json 为准。

## Evidence

[质询]具体数值（num_kv_heads=8, num_attention_heads=64）属于经验事实/模型配置参数，无法从第一性原理推导，且当前无可用外部来源直接证实该特定版本的具体配置值。 | 经验事实，逻辑自洽（GQA比例8:1符合常见设计）但缺来源支持

## Search Query

Qwen3-27B config.json num_key_value_heads GQA ratio site:huggingface.co
