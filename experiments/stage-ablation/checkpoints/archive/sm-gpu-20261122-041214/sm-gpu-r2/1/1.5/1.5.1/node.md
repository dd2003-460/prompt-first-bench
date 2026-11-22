# N59: Qwen3-27B 的具体架构参数：层数 n_layers=64, KV 头数 n_heads_kv=8, 头维度 head_dim=128（基于 Qwen2.

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Qwen3-27B 的具体架构参数：层数 n_layers=64, KV 头数 n_heads_kv=8, 头维度 head_dim=128（基于 Qwen2.5-32B 架构推断，需官方配置确认）。若参数不同，KV Cache 计算需修正。

## Corrected Claim

Qwen3-27B 的层数 n_layers=64 得到来源间接支持，但 n_heads_kv=8 和 head_dim=128 的具体数值缺乏直接来源确认，且需注意区分 Qwen3-27B 与后续版本（如 Qwen3.8-27B）的架构差异，建议以官方 config.json 为准。

## Evidence

[质询]来源[2]和[3]明确指向的是 'Qwen3.8-27B'（或类似版本），且描述其为 'dense vision-language model'（稠密视觉语言模型）或具有混合解码器架构，这与陈述中基于 'Qwen2.5-32B' 推断的纯文本 LLM 架构（n_layers=64, n_heads_kv=8, head_dim=128）存在版本和架构类型的潜在混淆。虽然 Qwen3 系列确实有 27B 模型，但具体参数（如 KV 头数）需针对特定版本（如 Qwen3-27B 纯文本版 vs Qwen3.8-27B 多模态版）确认，来源未直接提供 Qwen3-27B 纯文本版的 config 细节，且来源标题存在版本不一致（3.6/3.8 vs 3）。 | 来源[2]提及 64 层解码器，与陈述中的 n_layers=64 一致，但来源主要讨论 Qwen3.8-27B 的混合架构，未直接确认 Qwen3-27B 的 n_heads_kv=8 和 head_dim=128 等具体 KV Cache 参数，属于间接支持且存在版本歧义。

## Search Query

Qwen3-27B config.json n_layers n_heads_kv head_dim

## Retrieval Sources

- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=491048fbd02524bd361edaffe1d0de87ffd29f2609913dd907f9f50dc16b0f37', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
- {'url': 'https://liminalml.com/concepts/qwen-3-8-27b&rut=e4aa5413bea991ba34a862bca3368466e8a20cf32d7d37e0464362bfc20749e8', 'type': 'ddg', 'title': 'Qwen3.8-27B: Architecture Explained · LiminalML'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=e1a4a75338ea7b8dd9906f6fd7993bdcd78532cfd255bfc4583f3ebbf527f720', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
