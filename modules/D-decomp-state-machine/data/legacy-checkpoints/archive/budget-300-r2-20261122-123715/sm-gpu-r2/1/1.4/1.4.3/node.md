# N48: Qwen3-27B 具体架构参数确认：num_layers=72, hidden_size=4096, num_attention_heads=32, num_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8, N9, N10

## Claim

Qwen3-27B 具体架构参数确认：num_layers=72, hidden_size=4096, num_attention_heads=32, num_key_value_heads=8 (GQA ratio 4:1)，这些参数直接决定权重和 KV Cache 的精确计算基数。

## Corrected Claim

Qwen3 系列 27B 规模模型（具体版本需确认，如 Qwen3-27B 或 Qwen3.6-27B）通常采用 GQA 架构，典型参数包括 num_layers 约 64-72, hidden_size 4096-8196, num_attention_heads 32-64, num_key_value_heads 8-16。具体数值需依据官方模型卡确认，不同小版本（3.0/3.6/3.8）可能存在差异。

## Evidence

[质询]参考来源均指向 Qwen3.6 或 Qwen3.8 版本，而非 Qwen3-27B（通常指 Qwen3 系列中的 27B 稠密模型，如 Qwen3-27B-Instruct 或 Qwen3-27B-Base）。不同版本（3.0 vs 3.6 vs 3.8）的架构参数（如层数、隐藏层维度、注意力头数）可能存在差异，且来源 [3] 提到 MoE 和线性注意力，这与陈述中隐含的标准 Transformer 稠密架构（GQA）可能存在冲突或版本混淆。 | 来源 [1] 和 [2] 分别讨论 Qwen3.8 和 Qwen3.6，未直接提供 Qwen3-27B 的具体参数；来源 [3] 讨论 Qwen3.8 的 MoE 架构，与陈述中的 GQA 稠密架构描述不完全匹配或属于不同版本。逻辑上参数量级合理（27B 模型通常 hidden_size 4096-8192, layers 64-80），但缺乏针对 'Qwen3-27B' 这一特定版本号的直接来源支持，且存在版本混淆风险。

## Search Query

Qwen3-27B config.json num_layers hidden_size num_key_value_heads

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=e5459bd6ec62e1937706a05f835d37baa128ee9ce9105b7cdd4ee711d207a8ed', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
- {'url': 'https://blog.csdn.net/weixin_29053383/article/details/163379093&rut=6a5387d1db40aec2f5cf2c6c65550cd4b5ffd18b1322ae362303b1763a41a362', 'type': 'ddg', 'title': 'Qwen3.6-27B模型解析：架构优化与本地部署实战指南-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29051193/article/details/163968270&rut=ade46d5d32e2befed8aa4477708d39cad081b45bcdfd3e9738c3fd952bd590af', 'type': 'ddg', 'title': 'Qwen3.8 27B架构解析：MoE与线性注意力如何实现百万上下文-CSDN博客'}
