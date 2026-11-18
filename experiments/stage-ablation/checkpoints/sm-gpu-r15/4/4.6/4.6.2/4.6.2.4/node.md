# N234: NVIDIA 驱动 535.xx 与 550.xx 在 RTX 4090 上的 CUDA Kernel 效率差异主要体现在 Tensor Core 利用率上，5

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

NVIDIA 驱动 535.xx 与 550.xx 在 RTX 4090 上的 CUDA Kernel 效率差异主要体现在 Tensor Core 利用率上，550.xx 驱动通常包含针对 Ada Lovelace 架构的优化 Patch，但在 INT8 推理场景下，若框架 (vLLM/llama.cpp) 未更新对应的 cuBLAS/cuDNN 版本，驱动更新带来的吞吐量提升通常小于 5% [待核验]。

## Corrected Claim

NVIDIA 驱动 550.xx 通常包含针对 Ada Lovelace 架构的优化，但在 INT8 推理场景下，若框架未更新对应的 cuBLAS/cuDNN 版本，驱动更新带来的吞吐量提升可能有限（具体数值需实测验证，通常较小）。

## Evidence

[质询]该陈述包含具体的经验性数值断言（'吞吐量提升通常小于 5%'）和特定的技术归因（'主要体现在 Tensor Core 利用率上'），这些属于硬件/软件性能经验事实，无法从第一性原理推导，且参考来源中完全缺乏支持该具体数值或机制对比的证据。 | 经验事实，逻辑自洽但缺来源支持（参考来源[1]-[4]均为通用介绍或无关规格，未覆盖驱动版本间的具体性能差异数据）。

## Search Query

NVIDIA driver 535 vs 550 RTX 4090 INT8 inference performance benchmark

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
- {'url': 'https://www.nvidia.com/en-us/', 'type': 'bing', 'title': 'World Leader in Artificial Intelligence Computing | NVIDIA'}
- {'url': 'https://www.nvidia.com/en-us/drivers/', 'type': 'bing', 'title': 'Download The Official NVIDIA Drivers | NVIDIA'}
- {'url': 'https://en.m.wikipedia.org/wiki/Nvidia', 'type': 'bing', 'title': 'Nvidia - Wikipedia'}
