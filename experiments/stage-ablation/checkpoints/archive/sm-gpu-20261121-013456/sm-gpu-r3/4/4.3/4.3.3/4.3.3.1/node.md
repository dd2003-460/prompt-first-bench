# N201: 2×RTX 4090 在 INT4 量化下运行 Qwen3-27B 的实际推理吞吐量基准值，需区分软件栈（vLLM vs llama.cpp）与 Batch S

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

2×RTX 4090 在 INT4 量化下运行 Qwen3-27B 的实际推理吞吐量基准值，需区分软件栈（vLLM vs llama.cpp）与 Batch Size（1 vs 8），预期范围 55-75 tokens/s，具体数值需实测验证。

## Corrected Claim

2×RTX 4090 在 INT4 量化下运行 Qwen3-27B 的推理吞吐量受软件栈和 Batch Size 影响显著，参考双卡 8bit 量化实测约 28 tokens/s，INT4 量化下预期吞吐量可能更高，具体数值需实测验证。

## Evidence

[质询]来源[3]提供的双卡实测数据（28 tokens/s）与陈述中的预期范围（55-75 tokens/s）存在显著偏差，且来源[3]使用的是8bit量化而非INT4，不同量化精度和软件栈（vLLM vs llama.cpp）下的吞吐量差异巨大，单一来源无法支撑该特定范围。 | 来源[3]显示双卡8bit量化下为28 tokens/s，虽低于预期范围，但INT4量化通常比8bit更快，且不同软件栈性能差异大，逻辑上55-75 tokens/s在INT4下是可能的，但缺乏直接支持该具体数值的来源，属于经验事实且证据不足。

## Search Query

Qwen3-27B INT4 inference throughput 2x RTX 4090 vLLM llama.cpp tokens per second benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_34885746/article/details/171083516&rut=a1a3392f7d33f6a0359d57acc6fa072b89b168c3ca5afa91293ccfd492d9c1b9', 'type': 'ddg', 'title': '270亿参数塞进RTX 4090：Qwen3.8-27B开源，用TaoToken统一Key跑通本地推理-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/98629002&rut=e2ee4e99ed1f6135cc3c4f4f85d3da527c1b19d9dcc148b777bfe0f607abfcc8', 'type': 'ddg', 'title': 'Qwen 3.8-27B模型单卡RTX 4090本地部署与量化推理实战'}
- {'url': 'https://blog.csdn.net/weixin_29039773/article/details/163150694&rut=dd0bee7e1e7a9f212ae7b560584ca388f4623f362afb9c420f601ada77e71d02', 'type': 'ddg', 'title': '双RTX 4090部署Qwen3.5-27B大模型实战指南 - CSDN博客'}
