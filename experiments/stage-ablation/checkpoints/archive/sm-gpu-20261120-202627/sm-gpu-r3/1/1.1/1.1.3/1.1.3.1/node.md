# N166: Qwen3-27B 的 tie_word_embeddings 配置状态：若为 true，Output Head 不占用额外显存；若为 false，需额外增加 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Qwen3-27B 的 tie_word_embeddings 配置状态：若为 true，Output Head 不占用额外显存；若为 false，需额外增加 vocab_size * hidden_dim * 2 bytes 的显存。[待核验：需查阅 Qwen3 官方模型卡或 config.json]。

## Corrected Claim

Qwen3-27B 的 tie_word_embeddings 配置状态需查阅官方模型卡确认；若为 true，Output Head 不占用额外显存；若为 false，需额外增加 vocab_size * hidden_dim * 2 bytes 的显存。

## Evidence

[质询]该陈述包含具体的硬件/模型配置经验事实（Qwen3-27B 的 tie_word_embeddings 具体取值及显存计算公式），属于经验事实范畴，无法仅凭第一性原理推导其具体配置状态，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法确认 Qwen3-27B 的具体配置值，但显存计算公式逻辑正确）

## Search Query

Qwen3-27B tie_word_embeddings true false
