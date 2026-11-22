# N196: Qwen3-27B 架构参数验证：num_layers=64, num_kv_heads=8, head_dim=128 来源于 Qwen3 官方 Huggin

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

Qwen3-27B 架构参数验证：num_layers=64, num_kv_heads=8, head_dim=128 来源于 Qwen3 官方 HuggingFace 配置文件 config.json，该配置确认 GQA 比例为 64:8=8:1，与 Llama3-70B 架构一致，确保 KV Cache 计算基础正确

## Corrected Claim

Qwen3-27B 系列模型（如 Qwen3.8-27B）采用混合注意力架构，64 层中仅部分层（如 16 层）使用完整 GQA 注意力，其余层使用线性注意力或恒定循环状态，KV Cache 计算需考虑混合架构特性，而非简单的 64:8 GQA 比例。

## Evidence

[质询]来源显示 Qwen3 系列 27B 模型（如 Qwen3.8-27B）采用了混合注意力架构（Hybrid Attention），其中仅部分层（如 16/64 层）使用完整注意力，其余层使用线性注意力或恒定循环状态，这与陈述中隐含的“所有 64 层均为标准 GQA 注意力”的架构假设矛盾，且来源未提供 num_kv_heads=8 的直接证据，反而暗示架构复杂性远超简单 GQA。 | 来源 [1] 和 [3] 指出 Qwen3.8-27B 基于混合注意力主干，64 层中仅 16 层运行完整注意力，其余为线性/恒定状态，这与陈述中基于纯 GQA 架构（64:8）的 KV Cache 计算基础不符，且无来源直接支持 num_kv_heads=8 这一具体参数。

## Search Query

Qwen3-27B config.json num_layers num_kv_heads head_dim

## Retrieval Sources

- {'url': 'https://docs.vllm.ai/projects/ascend/zh-cn/latest/tutorials/models/Qwen3.8-27B.html&rut=5a4f55da49df759aedfa90729139963283b74379830cbe07bff0084f7310c0c0', 'type': 'ddg', 'title': 'Qwen3.8-27B - vLLM Ascend (中文)'}
- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=0b10fe0d815af316e8374ea97a2024ed873765fdf7691a90951d7aedc81374a1', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
- {'url': 'https://blog.csdn.net/weixin_29061997/article/details/163968287&rut=d8bcdaad59c325dd9cad4b0f2c92c1c5099f1710ea83e3806ae5b07aec6e1d03', 'type': 'ddg', 'title': 'Qwen3.8 27B架构解析：75%非Transformer层如何优化KV Cache与长上下文推理-CSDN博客'}
