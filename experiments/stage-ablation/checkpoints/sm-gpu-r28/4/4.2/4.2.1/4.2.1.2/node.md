# N180: RTX 4090 在 Qwen3-27B BF16 下的实测吞吐量基准值（tokens/s），作为对比基准，基于 vLLM 在 32K 上下文下的单卡实测数据，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N57

## Claim

RTX 4090 在 Qwen3-27B BF16 下的实测吞吐量基准值（tokens/s），作为对比基准，基于 vLLM 在 32K 上下文下的单卡实测数据，通常范围在 50-80 tokens/s 之间 [待核验]

## Corrected Claim

RTX 4090 在 Qwen3-27B BF16 下的实测吞吐量基准值（tokens/s），作为对比基准，基于 vLLM 在 32K 上下文下的单卡实测数据，通常范围在 50-80 tokens/s 之间（注：此数值为经验估计，缺乏当前参考来源的直接实证支持，建议补充具体基准测试报告）

## Evidence

[质询]该陈述为具体的经验性硬件性能数据（吞吐量基准值），属于经验事实，无法从第一性原理推导。参考来源中未包含任何关于 RTX 4090 运行 Qwen3-27B 模型在 vLLM 框架下 32K 上下文吞吐量的实测数据，缺乏直接证据支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]和[2]均与该具体性能测试无关）

## Search Query

NVIDIA RTX 4090 Qwen3-27B BF16 inference benchmark tokens per second vLLM 32k context

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
