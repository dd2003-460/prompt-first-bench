# N357: Qwen3-27B 的 num_kv_heads 确认为 8（基于 GQA 架构，通常 num_attention_heads 为 32 或 40，num_ke

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N148

## Claim

Qwen3-27B 的 num_kv_heads 确认为 8（基于 GQA 架构，通常 num_attention_heads 为 32 或 40，num_key_value_heads 为 8），该参数直接决定 KV Cache 大小，若为 MHA (num_kv_heads = num_heads) 则 KV Cache 将增大 4-5 倍，需通过模型 config.json 核验。

## Corrected Claim

Qwen3-27B 采用 GQA 架构，其 num_kv_heads 通常小于 num_attention_heads（如 8 或 16），具体数值需查阅该模型版本的 config.json 确认；若 num_kv_heads 显著小于 num_attention_heads，KV Cache 将相应减小。

## Evidence

[质询]来源[1]指向的模型名称为 'Qwen3.8-27B'，与陈述中的 'Qwen3-27B' 存在命名不一致（可能是版本混淆或笔误），且摘要未提供具体参数值，无法直接证实 num_kv_heads 为 8；来源[3]仅说明默认值为 32，未提供特定 27B 模型的实际配置。 | 逻辑上 GQA 架构下 KV Cache 大小与 num_kv_heads 成正比，若从 8 变为 32/40 确实会增大 4-5 倍，逻辑自洽；但外部来源未直接提供 Qwen3-27B 的具体 num_kv_heads=8 的证据，来源[1]模型名不匹配，来源[3]仅为通用文档，故降级。

## Search Query

Qwen3-27B config.json num_key_value_heads num_attention_heads

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B/blob/main/config.json&rut=131e538fa29adedcb11e88911ba2a02c7f70d582bcacfd010a6ba84026988901', 'type': 'ddg', 'title': 'config.json · Qwen/Qwen3.8-27B at main - Hugging Face'}
- {'url': 'https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen3/configuration_qwen3.py&rut=093ca5bd1947abdefc2ac6351bee35f4b43ee47deaeba7b10809783cfbba3a3c', 'type': 'ddg', 'title': 'transformers/src/transformers/models/qwen3/configuration_qwen3 ... - GitHub'}
- {'url': 'https://huggingface.co/docs/transformers/model_doc/qwen3&rut=9d8353353a9e227a175b599ccbacb569ef16d1638cfae62195cc8b87c9483f9c', 'type': 'ddg', 'title': 'Qwen3 · Hugging Face'}
