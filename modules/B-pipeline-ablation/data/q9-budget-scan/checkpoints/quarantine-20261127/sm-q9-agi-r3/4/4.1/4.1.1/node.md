# N62: Qwen3.8-27B 的架构参数具体数值：n_layers (总层数), n_kv_heads (KV头数), head_dim (头维度)。Qwen2/3 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

Qwen3.8-27B 的架构参数具体数值：n_layers (总层数), n_kv_heads (KV头数), head_dim (头维度)。Qwen2/3 系列 27B 模型通常 n_layers=32, n_kv_heads=8 (GQA), head_dim=128。需确认 Qwen3.8-27B 的确切参数，因为 KV 大小直接正比于 n_layers * n_kv_heads * head_dim。

## Corrected Claim

Qwen3.8-27B 采用混合线性注意力架构，其 KV 缓存特性与传统 GQA Transformer 不同。虽然参数量级相近，但具体的 n_layers、n_kv_heads 及 head_dim 需查阅官方 config.json 确认，不能直接等同于 Qwen2/3 标准版的 32/8/128 配置。

## Evidence

[质询]陈述假设 Qwen3.8-27B 沿用 Qwen2/3 标准 Transformer 架构（n_layers=32, n_kv_heads=8, head_dim=128），但参考来源 [2] 和 [3] 明确指出 Qwen3.8 采用了“线性注意力”和“混合设计”，这意味着其 KV Cache 计算逻辑和架构参数可能与传统 GQA Transformer 不同，直接套用旧版参数可能导致 KV 大小估算错误。 | 来源 [2] 和 [3] 证实 Qwen3.8 采用线性注意力/混合架构，但未提供具体的 n_layers/n_kv_heads/head_dim 数值；来源 [1] 仅介绍模型概况。由于缺乏直接数值支持且架构变更导致原假设存在不确定性，判为 degraded。

## Search Query

Qwen3 27B model architecture num layers num key value heads head dimension

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=5f69e53cf37790b6e21cecf0865561f9a7b73267f9067ba9d47d24b7bad8b5fa', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
- {'url': 'https://blog.csdn.net/weixin_29057237/article/details/163968271&rut=a4fbd625d747d63df65fbed28c8f18469200c9f3b884a721b6c2587cf6815ea9', 'type': 'ddg', 'title': 'Qwen3.8 27B架构解析：线性注意力与混合设计如何实现百万级上下文-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_43977163/article/details/163824568&rut=7b719ca61613ac6b2a1bf43a367e3f156f654543eec376b548c1cf586a0e3710', 'type': 'ddg', 'title': 'Qwen3.8-27B 源码拆解 + 保姆级本地部署 + 模型横评：270 亿参数如何用混合线性注意力打穿长序列天花板'}
