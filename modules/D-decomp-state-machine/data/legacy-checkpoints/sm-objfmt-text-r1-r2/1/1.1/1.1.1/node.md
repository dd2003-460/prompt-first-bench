# N25: Qwen3-27B 的 Transformer 层数 (n_layers) 确切值为 64 层，该参数直接决定 KV Cache 总显存的线性倍数

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7, N8, N9

## Claim

Qwen3-27B 的 Transformer 层数 (n_layers) 确切值为 64 层，该参数直接决定 KV Cache 总显存的线性倍数

## Corrected Claim

Qwen3-27B 的 Transformer 层数通常为 64 层（需查阅官方 config.json 确认），该参数决定了 KV Cache 显存占用的线性倍数关系。

## Evidence

[质询]参考来源主要讨论的是 'Qwen3.8' 或 'Qwen3.6' 的混合架构（线性注意力），并未直接提供 'Qwen3-27B' 这一特定版本的标准 Transformer 层数为 64 的确切配置数据；且不同版本间架构可能存在差异，存在版本混淆风险。 | 来源 [1][2] 提及 Qwen3.x 系列 27B 模型及 KV Cache 问题，但未直接证实 n_layers=64 的具体数值；该数值符合 27B 参数量级下常见 Transformer 深度（如 Llama-3-70B 为 80 层，Qwen2-72B 为 80 层，27B 级别 64 层在量级上合理），但缺乏直接来源支持，属经验事实。

## Search Query

Qwen3-27B architecture n_layers hidden_size num_attention_heads

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29057237/article/details/163968271&rut=a4fbd625d747d63df65fbed28c8f18469200c9f3b884a721b6c2587cf6815ea9', 'type': 'ddg', 'title': 'Qwen3.8 27B架构解析：线性注意力与混合设计如何实现百万级上下文-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_30952479/article/details/163968289&rut=284c52077cc031c2a9d6b72d3debb4fd25fe4565faf35467825f9731725c78b9', 'type': 'ddg', 'title': 'Qwen3.8 27B混合架构解析：线性注意力如何突破百万上下文部署瓶颈-CSDN博客'}
- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=dc8a166013362d6a9cce3dbf8a5f64fd158b3f2b0f51dc21a9ad7520fb478aa4', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
