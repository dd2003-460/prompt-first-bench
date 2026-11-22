# N107: 在长文本生成任务（如 8K+ tokens 输出）中，FP8 量化导致的困惑度累积效应使得最终输出连贯性评分（Coherence Score）下降约 5-8%，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

在长文本生成任务（如 8K+ tokens 输出）中，FP8 量化导致的困惑度累积效应使得最终输出连贯性评分（Coherence Score）下降约 5-8%，主要源于 KV Cache 中微小误差的逐层放大。

## Corrected Claim

在长文本生成任务中，FP8量化可能导致困惑度累积，进而影响输出连贯性，但具体下降幅度（如5-8%）需更多实证数据支持。

## Evidence

[质询]具体数值（5-8%）和特定指标（Coherence Score）缺乏来源支持，且来源主要讨论RL训练稳定性而非长文本生成的连贯性评分。 | 来源[1]仅提及FP8在RL中的稳定性挑战，未提供长文本生成中困惑度累积导致连贯性下降5-8%的具体数据，属于经验事实且缺直接来源支持。

## Search Query

FP8 quantization long context generation coherence degradation LLM

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2609.22870&rut=1c3b12697f1f5301a0b8e82c1a86448ec9dd0f46b798c598e93b3e44a23db3cc', 'type': 'ddg', 'title': 'Towards Full Pipeline FP8 Reinforcement Learning for LLMs'}
