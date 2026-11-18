# N169: RTX 4090 在 Qwen3-27B INT8 量化下的实测吞吐量基准值（tokens/s），作为对比基准，需基于 vLLM 或 TensorRT-LLM 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

RTX 4090 在 Qwen3-27B INT8 量化下的实测吞吐量基准值（tokens/s），作为对比基准，需基于 vLLM 或 TensorRT-LLM 在 32K 上下文下的单卡实测数据，通常范围在 80-120 tokens/s 之间 [待核验]

## Corrected Claim

RTX 4090 在 Qwen3-27B INT8 量化下的实测吞吐量基准值需基于具体推理框架（如 vLLM 或 TensorRT-LLM）及上下文长度（如 32K）的实测数据确定，通常范围可能在 80-120 tokens/s 之间，但具体数值需以实际基准测试为准。

## Evidence

[质询]该陈述属于具体的硬件性能经验数据（吞吐量基准值），无法从第一性原理推导。参考来源中未包含任何关于 RTX 4090 运行 Qwen3-27B 在 32K 上下文下的实测吞吐量数据，且来源 [3] 仅提及 RTX 4060 的功耗，与事实节点中的 RTX 4090 及吞吐量指标无关。缺乏直接来源支持，且不同推理框架（vLLM vs TensorRT-LLM）及具体配置可能导致数值波动，80-120 tokens/s 的范围虽在逻辑上可能合理（取决于 batch size 和具体实现），但缺乏实证依据。 | 经验事实，逻辑自洽但缺来源支持（来源 [1][2][3] 均与该具体性能指标无关）

## Search Query

NVIDIA RTX 4090 Qwen3-27B INT8 inference benchmark tokens per second vLLM TensorRT-LLM 32k context

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
