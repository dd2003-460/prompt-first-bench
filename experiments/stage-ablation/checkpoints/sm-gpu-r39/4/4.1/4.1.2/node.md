# N55: AMD Radeon RX 7900 XTX (24GB) 的显存带宽 (960 GB/s) 与 RTX 4090 (1008 GB/s) 的对比，以及 ROC

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N16

## Claim

AMD Radeon RX 7900 XTX (24GB) 的显存带宽 (960 GB/s) 与 RTX 4090 (1008 GB/s) 的对比，以及 ROCm 环境下 Qwen3-27B INT8 推理的实测 tokens/s，计算其每美元吞吐比 (tokens/s per $) 相对于 RTX 4090 的修正系数

## Corrected Claim

AMD Radeon RX 7900 XTX (24GB) 与 RTX 4090 的显存带宽对比及 ROCm 环境下 Qwen3-27B INT8 推理的每美元吞吐比修正系数需基于具体实测数据计算，当前参考来源未提供相关数值支持。

## Evidence

[质询]该陈述包含具体的硬件规格数值（960 GB/s, 1008 GB/s）和特定的实测性能数据（Qwen3-27B INT8 tokens/s），属于经验事实。参考来源中仅包含通用的 arXiv 介绍、RTX 4060 的无关规格、AMD 官网首页及驱动下载页，均未提供 RX 7900 XTX 和 RTX 4090 的具体显存带宽对比数据，也未包含任何关于 Qwen3-27B 在 ROCm 环境下的实测吞吐数据或每美元吞吐比的计算依据。 | 经验事实，逻辑自洽但缺来源支持（来源[1]-[4]均与具体硬件参数及实测数据无关）

## Search Query

RX 7900 XTX vs RTX 4090 LLM inference benchmark Qwen 27B INT8 tokens per second cost efficiency

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
- {'url': 'https://www.amd.com/en.html', 'type': 'bing', 'title': 'AMD ׀ together we advance_AI'}
- {'url': 'https://www.amd.com/en/support/download/drivers.html', 'type': 'bing', 'title': 'Drivers and Support for Processors and Graphics'}
