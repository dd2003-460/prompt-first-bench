# N46: Qwen3-27B 的架构参数确认：num_layers=48, hidden_dim=4096, num_attention_heads=32, num_ke

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Qwen3-27B 的架构参数确认：num_layers=48, hidden_dim=4096, num_attention_heads=32, num_key_value_heads=8 (GQA ratio 4:1), head_dim=128

## Corrected Claim

Qwen3-27B 的架构参数通常包括 num_layers=48, hidden_dim=4096, num_attention_heads=32, num_key_value_heads=8, head_dim=128，但需注意参考来源主要讨论的是 Qwen3.8-27B 的混合注意力变体，具体参数需以官方模型卡为准。

## Evidence

[质询]参考来源均指向 'Qwen3.8-27B' 且描述为混合架构（48层线性+16层全注意力），与陈述中的 'Qwen3-27B' 及纯 Transformer 架构参数（48层全注意力）存在版本/架构混淆风险；此外，来源未直接提供 hidden_dim 等具体数值，仅确认了层数相关描述。 | 来源 [1][2] 确认了 27B 模型具有 48 层结构（尽管描述为混合架构，可能与 Qwen3 标准版或特定变体混淆），但缺乏对 hidden_dim=4096, heads=32 等具体参数的直接支持；作为经验事实（硬件/模型规格），逻辑自洽但缺直接来源支持，故降级。

## Search Query

Qwen3-27B model config num_layers num_key_value_heads hidden_size

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00007/article/details/170349415&rut=5700697a541d38dce0309a4ee2fb2fe07439f27b5d53add09d5eaf77e90562de', 'type': 'ddg', 'title': '解剖Qwen3.8-27B-AWQ混合架构：48层Gated DeltaNet+16层全注意力如何实现超低成本256K上下文'}
- {'url': 'https://blog.csdn.net/liu8485/article/details/164724304&rut=b7c08168b53b511f68674c156d96aa9524b8914fb42107a4a9b9b614dca3f054', 'type': 'ddg', 'title': 'Qwen3.8-27B 混合注意力拆解：48 层线性 + 16 层全注意力，75 万 token KV 显存打到 1/4'}
- {'url': 'https://happyrock.cloud/zh/blog/2026-08-16_qwen3.8-27b/&rut=a7d764fc762910ca9e2b13877451933cafd0da78e6b8c4cd0a98654ddeda2997', 'type': 'ddg', 'title': 'Qwen3.8-27B混合注意力架构深度解析：48层Gated DeltaNet + 16层Attention如何让270亿参数模型跑在消费级 ...'}
