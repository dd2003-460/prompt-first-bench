# N33: Qwen3.8-27B 实际架构参数核实：确认 num_hidden_layers (L)、num_key_value_heads (H_kv) 和 head_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3.8-27B 实际架构参数核实：确认 num_hidden_layers (L)、num_key_value_heads (H_kv) 和 head_dim (D_h)。当前计算假设 H_kv=8, D_h=128, L=32，但需查阅 config.json 确认 L 是否为 32 或其他值，因为这直接决定 KV Cache 总量是线性缩放还是固定。

## Corrected Claim

Qwen3.8-27B 的实际架构参数（num_hidden_layers, num_key_value_heads, head_dim）需查阅官方 config.json 确认，当前假设值（L=32, H_kv=8, D_h=128）未经过直接来源验证。

## Evidence

[质询]该陈述包含具体的经验参数值（L=32, H_kv=8, D_h=128），这些数值无法从第一性原理推导，必须依赖具体的模型配置文件（config.json）或官方文档确认。虽然来源[2]提到了解析config.json，但摘要中未直接列出这些具体数值，存在参数记忆错误或版本差异的风险。 | 经验事实，逻辑自洽但缺来源直接支持。来源[2]涉及config.json解析但未在摘要中提供具体数值验证，来源[1]和[3]主要关注架构特性而非具体超参数。

## Search Query

Qwen3.8-27B config.json num_hidden_layers num_key_value_heads head_dim huggingface

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_36149538/article/details/171411071&rut=ea155f02eb7b40fb4e721beca0af30eab8be024ab47acc7c0fc21784759c8d79', 'type': 'ddg', 'title': 'Qwen3.8-27B 源码拆解 + 保姆级本地部署 + 模型横评：270 亿参数如何用混合线性注意力打穿长序列天花板｜'}
- {'url': 'https://blog.csdn.net/gitblog_00829/article/details/168233310&rut=6062473e699e81b5a4ca09ebe85a1d99283387e2fb207a8425632ee71efc97ed', 'type': 'ddg', 'title': 'Qwen3.8-27B-MTP-bf16 config.json深度解析：block_size、mtp_num_hidden_layers与 ...'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=24c9807de7f70da9f46218badaf35c18091a4c13296dd9331327324cafe58715', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
