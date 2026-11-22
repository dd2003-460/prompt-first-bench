# N129: 修正 Qwen3-27B 的架构参数：查阅官方 config.json，Qwen3-27B 的 n_layers=48, num_key_value_heads

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

修正 Qwen3-27B 的架构参数：查阅官方 config.json，Qwen3-27B 的 n_layers=48, num_key_value_heads=8, head_dim=128, hidden_size=4096，需确认是否启用 GQA (Grouped Query Attention) 及具体的 kv 头数比例。

## Corrected Claim

需查阅 Qwen3-27B 官方 config.json 以确认 n_layers, num_key_value_heads, head_dim, hidden_size 等具体架构参数及 GQA 配置。

## Evidence

[质询]参考来源指向的模型版本（Qwen3.8-27B, Qwen3.6-27B）与陈述中的模型版本（Qwen3-27B）不一致，且摘要未提供具体的架构参数数值，无法直接验证 n_layers, num_key_value_heads 等具体数值。 | 来源 [1] 和 [2] 指向不同版本号的 Qwen 模型 config.json，与陈述中的 'Qwen3-27B' 版本不匹配，且摘要内容未包含具体参数值，属于间接/无关证据，无法直接支持具体数值。

## Search Query

Qwen3-27B model config n_layers num_key_value_heads head_dim

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B/blob/main/config.json&rut=96999dbb34495711fbad1a527423b80454bb8588158b454d8a51e703f4b894d7', 'type': 'ddg', 'title': 'config.json · Qwen/Qwen3.8-27B at main - Hugging Face'}
- {'url': 'https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/config.json&rut=8ea4a8b12be09fc0ed058dcd5b472d0efe9211b44d6b3edd0bf4ba38352b2849', 'type': 'ddg', 'title': 'config.json · Qwen/Qwen3.6-27B at main - Hugging Face'}
