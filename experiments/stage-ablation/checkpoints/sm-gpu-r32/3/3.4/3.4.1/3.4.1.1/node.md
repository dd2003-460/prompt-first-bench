# N156: AMD ROCm 环境下 vLLM 运行 Qwen3-27B BF16 的实测吞吐量通常为同代 NVIDIA CUDA 环境 (RTX 4090) 的 70%-

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N50

## Claim

AMD ROCm 环境下 vLLM 运行 Qwen3-27B BF16 的实测吞吐量通常为同代 NVIDIA CUDA 环境 (RTX 4090) 的 70%-85%，主要瓶颈在于 Kernel Launch Overhead 和内存带宽利用率较低 (ROCm 驱动优化滞后)

## Corrected Claim

AMD ROCm 环境下 vLLM 运行 Qwen3-27B BF16 的吞吐量通常低于同代 NVIDIA CUDA 环境 (RTX 4090)，主要瓶颈可能涉及 Kernel Launch Overhead 和内存带宽利用率，但具体性能差距比例需依据最新实测数据确定。

## Evidence

[质询]该陈述包含具体的经验数值（70%-85%）和特定的硬件对比（ROCm vs RTX 4090），属于经验事实。参考来源中没有任何一个提供了关于 vLLM 在 AMD ROCm 与 NVIDIA CUDA 环境下运行 Qwen3-27B 的吞吐量对比数据或瓶颈分析，无法验证具体数值区间及瓶颈归因的准确性。 | 经验事实，逻辑自洽但缺来源支持（来源[1]-[4]均与具体性能对比无关）

## Search Query

vLLM AMD ROCm vs NVIDIA CUDA throughput benchmark Qwen27B

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
- {'url': 'https://www.amd.com/en.html', 'type': 'bing', 'title': 'AMD ׀ together we advance_AI'}
