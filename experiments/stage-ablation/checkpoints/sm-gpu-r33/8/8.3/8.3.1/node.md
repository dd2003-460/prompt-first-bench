# N267: H100 SXM 在 Qwen3-27B BF16 推理（batch_size=1, seq_len=32K）下的稳态平均功耗为 650W ± 15W，该值基于

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

H100 SXM 在 Qwen3-27B BF16 推理（batch_size=1, seq_len=32K）下的稳态平均功耗为 650W ± 15W，该值基于 NVIDIA 官方能效曲线及第三方实测（如 ServeLLM 基准）的 P95 均值确定，用于年电力成本计算。

## Corrected Claim

H100 SXM 在 Qwen3-27B BF16 推理（batch_size=1, seq_len=32K）下的稳态平均功耗约为 650W（基于典型推理负载估算，具体数值需参考特定实测基准如 ServeLLM 等，当前来源未直接证实该精确值）。

## Evidence

[质询]该陈述包含具体的经验数值（650W ± 15W）及特定负载下的功耗断言，属于硬件性能/功耗的经验事实，无法从第一性原理推导。参考来源中未包含任何关于 H100 在 Qwen3-27B 推理场景下的具体功耗实测数据或能效曲线细节，来源 [1] 仅列出通用规格（TDP 通常为 700W），来源 [3] 关注内存带宽而非功耗，来源 [4] 关注微调任务而非推理功耗。缺乏直接来源支持具体数值。 | 经验事实，逻辑自洽（H100 SXM TDP 为 700W，推理负载下 650W 在合理范围内），但参考来源未提供该特定场景下的具体功耗实测数据支持，故降级。

## Search Query

H100 SXM power consumption Qwen27B inference benchmark average watts

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units', 'type': None, 'title': 'wiki-full: List of Nvidia graphics processing units'}
- {'url': 'https://nvidia.com', 'type': None, 'title': 'direct-browser: nvidia.com'}
- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
- {'url': 'http://arxiv.org/abs/2608.13681v1', 'type': 'arxiv', 'title': 'Fine-Tuning Qwen3-27B for C-to-Rust Code Translation: A Three-Stage Curriculum o'}
