# N147: vLLM 框架在 Llama-2-70B 上启用 FP8 KV Cache 相比 BF16 KV Cache，在 4K 上下文长度下，Perplexity (困

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

vLLM 框架在 Llama-2-70B 上启用 FP8 KV Cache 相比 BF16 KV Cache，在 4K 上下文长度下，Perplexity (困惑度) 增加约 0.5-1.5% (从 ~5.2 增至 ~5.3-5.4)，而在 32K 长上下文下，累积误差可能导致 Perplexity 增加超过 3%，具体数值需参考 vLLM 官方博客或论文 'FP8 for LLM Inference' 中的实测数据。

## Corrected Claim

vLLM 框架在 Llama-2-70B 上启用 FP8 KV Cache 相比 BF16 KV Cache，在长上下文下可能导致 Perplexity 轻微增加，具体数值需参考 vLLM 官方博客或相关论文实测数据。

## Evidence

[质询]具体数值（0.5-1.5% 和 >3%）及特定模型（Llama-2-70B）在特定上下文长度下的 Perplexity 变化属于经验事实，且参考来源未提供直接支持，存在数值不准确或口径混淆的风险。 | 来源 [2] 间接支持 FP8 用于 LLM 推理及 KV Cache 的可行性，但未提供 Llama-2-70B 在 4K/32K 上下文下的具体 Perplexity 增量数据；经验事实缺直接来源支持，降级为定性表述。

## Search Query

vLLM FP8 KV cache perplexity degradation long context benchmark

## Retrieval Sources

- {'url': 'https://en.m.wikipedia.org/wiki/Gmail', 'type': 'bing', 'title': 'Gmail - Wikipedia'}
- {'url': 'http://arxiv.org/abs/2601.18150v2', 'type': 'arxiv', 'title': 'FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learnin'}
