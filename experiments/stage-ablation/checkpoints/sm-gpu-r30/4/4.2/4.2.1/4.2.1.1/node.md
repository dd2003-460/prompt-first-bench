# N179: H100 SXM 在 Qwen3-27B BF16 下的实测吞吐量基准值（tokens/s），基于 vLLM 或 TensorRT-LLM 在 32K 上下文下

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N57

## Claim

H100 SXM 在 Qwen3-27B BF16 下的实测吞吐量基准值（tokens/s），基于 vLLM 或 TensorRT-LLM 在 32K 上下文下的单卡实测数据，通常范围在 80-120 tokens/s 之间 [待核验]

## Corrected Claim

H100 SXM 在 Qwen3-27B BF16 下的实测吞吐量基准值（tokens/s），基于 vLLM 或 TensorRT-LLM 在 32K 上下文下的单卡实测数据，通常范围在 80-120 tokens/s 之间（注：此为经验估计值，缺乏当前参考来源的直接实测数据支持，具体数值需依据实际部署环境验证）

## Evidence

[质询]该陈述为具体的经验性硬件性能基准数据（H100 SXM + Qwen3-27B + BF16 + 32K上下文 + 单卡吞吐量），属于经验事实，无法从第一性原理推导。参考来源中未包含针对该特定模型和配置的直接实测数据，且不同推理引擎（vLLM vs TensorRT-LLM）及具体实现细节可能导致数值波动，缺乏直接来源支持。 | 经验事实，逻辑自洽但缺来源支持。来源[3]提及H100上的LLM服务性能研究，但未提供Qwen3-27B在32K上下文下的具体吞吐量数值，无法直接验证80-120 tokens/s的范围。

## Search Query

NVIDIA H100 SXM Qwen3-27B BF16 inference benchmark tokens per second vLLM 32k context

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'http://arxiv.org/abs/2609.19657v1', 'type': 'arxiv', 'title': 'PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LL'}
- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
