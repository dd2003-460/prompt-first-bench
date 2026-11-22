# N305: Qwen3-27B 架构参数核验：需从 Hugging Face 官方 config.json 确认 n_layers, n_heads, n_kv_heads

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

Qwen3-27B 架构参数核验：需从 Hugging Face 官方 config.json 确认 n_layers, n_heads, n_kv_heads, head_dim。若 n_layers=64, n_kv_heads=8, head_dim=128, 则 BF16 KV Cache = 2 * 64 * 8 * 128 * 32768 * 2B = 8.59GB，这与 N130 中基于 n_layers=28 计算的 3.98GB 存在巨大差异，需以官方配置为准修正 N130 的假设。

## Corrected Claim

Qwen3-27B（或 Qwen3.8-27B）的 KV Cache 大小需依据官方 config.json 中的 n_layers, n_kv_heads, head_dim 计算。若参数为 n_layers=64, n_kv_heads=8, head_dim=128，则 BF16 KV Cache 约为 8.59GB；此前基于 n_layers=28 计算的 3.98GB 需根据实际配置修正。

## Evidence

[质询]参考来源中未提供具体的 config.json 参数（如 n_layers, n_kv_heads, head_dim），无法直接验证陈述中假设的数值（64层, 8 KV头, 128维）是否准确，且来源标题显示为 Qwen3.8-27B 而非 Qwen3-27B，存在版本或命名混淆的可能。 | 逻辑推导成立（2*64*8*128*32768*2B ≈ 8.59GB），但参考来源 [1][2][3] 仅确认模型存在及大致参数量，未提供具体架构参数以直接支持或反驳 n_layers=64 等假设，属于经验事实且缺来源直接支持。

## Search Query

Qwen3-27B config.json num_hidden_layers num_key_value_heads head_dim huggingface

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B&rut=3d7831a77a0759778bf5fe7ec23242f552eacd18fef689ac2e5e92ec3eccaa2a', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B · Hugging Face'}
- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B-FP8&rut=14136281e1ef2fc006f2a2d3b080ee78368ef2e65dbc32e90d1e2479a0f7bd3d', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B-FP8 · Hugging Face'}
- {'url': 'https://zhuanlan.zhihu.com/p/2072113076694955181&rut=7c00bb34c8ed9b13f67a5019eebdc6ea1b42e7d4627904db112f24ca1e5b4599', 'type': 'ddg', 'title': 'Qwen3.8‑27B 刚开源!社区魔改未审查版出炉，17G 显存本地就能跑无滤镜 27B 大模型'}
