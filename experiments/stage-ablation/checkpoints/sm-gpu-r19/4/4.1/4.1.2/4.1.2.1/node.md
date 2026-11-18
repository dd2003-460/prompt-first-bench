# N168: AMD Radeon RX 7900 XTX 在 ROCm 6.1+ 环境下运行 Qwen3-27B INT8 量化的实测吞吐量基准值（tokens/s），需基

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

AMD Radeon RX 7900 XTX 在 ROCm 6.1+ 环境下运行 Qwen3-27B INT8 量化的实测吞吐量基准值（tokens/s），需基于 llama.cpp 或 vLLM 的 ROCm 后端在 32K 上下文下的实测数据，若缺乏直接数据，需使用 H100 的 ROCm 性能折扣系数（通常为 0.6-0.8）进行折算 [待核验]

## Corrected Claim

AMD Radeon RX 7900 XTX 在 ROCm 6.1+ 环境下运行 Qwen3-27B INT8 量化的实测吞吐量基准值需基于 llama.cpp 或 vLLM 的 ROCm 后端在 32K 上下文下的实测数据；若缺乏直接数据，可参考 H100 的 ROCm 性能折扣系数（通常估计在 0.6-0.8 之间）进行折算，但具体数值需以实际基准测试为准。

## Evidence

[质询]该陈述包含具体的经验性数值（吞吐量基准值、0.6-0.8的折扣系数），属于硬件性能与软件栈实测数据，无法从第一性原理推导，且参考来源中完全缺乏相关实测数据支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]-[4]均为通用页面，未包含RX 7900 XTX在ROCm下运行Qwen3-27B的具体吞吐量或H100对比折扣系数数据）。

## Search Query

AMD Radeon RX 7900 XTX ROCm Qwen3-27B INT8 inference benchmark tokens per second 32k context

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://www.amd.com/en.html', 'type': 'bing', 'title': 'AMD ׀ together we advance_AI'}
- {'url': 'https://www.amd.com/en/support/download/drivers.html', 'type': 'bing', 'title': 'Drivers and Support for Processors and Graphics'}
- {'url': 'https://en.wikipedia.org/wiki/AMD', 'type': 'bing', 'title': 'AMD - Wikipedia'}
