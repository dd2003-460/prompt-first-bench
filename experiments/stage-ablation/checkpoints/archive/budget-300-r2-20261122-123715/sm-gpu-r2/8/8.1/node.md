# N107: Qwen3-27B 的 GQA 配置参数：Q_heads=32, KV_heads=8, Head_dim=128 (基于 Qwen2.5-32B 架构推断，需

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26, N27

## Claim

Qwen3-27B 的 GQA 配置参数：Q_heads=32, KV_heads=8, Head_dim=128 (基于 Qwen2.5-32B 架构推断，需核验 Qwen3 具体配置)

## Corrected Claim

Qwen3.8-27B 的 GQA 配置参数：Q_heads=24, KV_heads=4, Head_dim=256

## Evidence

[质询]陈述声称 Qwen3-27B 的 GQA 配置为 Q_heads=32, KV_heads=8, Head_dim=128，但参考来源 [1] 明确指出 Qwen3.8-27B（属于 Qwen3 系列）的配置为 24 个 Q 头、4 个 KV 头、head_dim 256，数值与陈述完全矛盾。 | 来源 [1] 直接提供了 Qwen3.8-27B 的具体 GQA 参数（24 Q heads, 4 KV heads, 256 head_dim），与陈述中的 32/8/128 配置存在明确矛盾。

## Search Query

Qwen3-27B GQA heads configuration num_key_value_heads

## Retrieval Sources

- {'url': 'https://iqilian.com/learn/qwen38-gated-attention-24-4/&rut=576e3d11a5501e4ae9573a03f4621866501ddfed510ba56bae9e3f480f4eb106', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 GQA：24 个 Q 头配 4 个 KV 头、head_dim 是 256'}
- {'url': 'https://blog.csdn.net/gitblog_00033/article/details/151733507&rut=846674eec5e651f1be84ea0c521eb32dd20754549d6280297fcf5139d2f43350', 'type': 'ddg', 'title': 'Qwen3-32B模型结构解析：64层Transformer与GQA注意力机制详解-CSDN博客'}
- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=0b10fe0d815af316e8374ea97a2024ed873765fdf7691a90951d7aedc81374a1', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
