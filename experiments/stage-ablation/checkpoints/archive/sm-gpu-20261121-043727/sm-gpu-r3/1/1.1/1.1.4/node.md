# N42: Qwen3-27B 的 Grouped Query Attention (GQA) 配置：确认 num_key_value_heads 的值（通常为 hidde

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 的 Grouped Query Attention (GQA) 配置：确认 num_key_value_heads 的值（通常为 hidden_size/128 的约数，如 8 或 16）。N7 中的公式使用了 '头维度(128)'，但 KV Cache 大小取决于 KV 头数 (num_key_value_heads) 而非 Q 头数。若 num_key_value_heads=8，则 KV Cache 体积将比 MHA (Multi-Head Attention) 减少 (128/8)=16 倍（假设 hidden_size=4096, head_dim=128, num_heads=32）。

## Corrected Claim

Qwen3-27B 采用 Grouped Query Attention (GQA) 配置。KV Cache 大小取决于 KV 头数 (num_key_value_heads) 而非 Q 头数。若 num_key_value_heads 显著小于 Q 头数（例如 8 或 16），则 KV Cache 体积将比 MHA 显著减少。具体数值需参考 Qwen3-27B 官方模型配置。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（num_key_value_heads=8, hidden_size=4096等），属于经验事实。参考来源[1]仅确认Qwen3系列使用GQA机制，但未提供Qwen3-27B的具体头数配置，无法直接支持该具体数值。此外，Qwen3-27B的具体架构参数需查阅官方技术报告或配置文件，仅凭逻辑推导（hidden_size/128的约数）不足以确认为8。 | 来源[1]间接支持Qwen3使用GQA，但未提供Qwen3-27B的具体num_key_value_heads数值；该事实为经验事实，逻辑自洽但缺直接来源支持。

## Search Query

Qwen3-27B num_key_value_heads config.json GQA configuration

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1905664754569185060&rut=996eead263dea3540db5dd80d1c2d089ec97a6079e18ef49b1c485c5cace2d64', 'type': 'ddg', 'title': '图解Qwen3混合专家模型推理过程--GQA和MoE - 知乎'}
