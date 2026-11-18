# N234: NVIDIA 驱动 535.xx 与 550.xx 在 RTX 4090 上的 CUDA Kernel 效率差异主要体现在 Tensor Core 利用率上，5

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

NVIDIA 驱动 535.xx 与 550.xx 在 RTX 4090 上的 CUDA Kernel 效率差异主要体现在 Tensor Core 利用率上，550.xx 驱动通常包含针对 Ada Lovelace 架构的优化 Patch，但在 INT8 推理场景下，若框架 (vLLM/llama.cpp) 未更新对应的 cuBLAS/cuDNN 版本，驱动更新带来的吞吐量提升通常小于 5% [待核验]。

## Corrected Claim

NVIDIA 驱动 535.xx 与 550.xx 在 RTX 4090 上的 CUDA Kernel 效率差异可能涉及 Tensor Core 利用率优化，但在 INT8 推理场景下，若框架未同步更新 cuBLAS/cuDNN 版本，驱动更新带来的吞吐量提升可能有限（具体数值需实测验证）。

## Evidence

[质询]该陈述包含具体的经验性数值断言（吞吐量提升通常小于 5%）和特定的技术因果机制（驱动更新 vs 框架库版本耦合），这属于经验事实而非第一性原理可推导内容。参考来源中没有任何一个提供了关于 NVIDIA 驱动 535/550 版本在 RTX 4090 上针对 INT8 推理的具体性能基准数据或官方技术说明，因此无法验证该具体数值和因果关系的准确性。 | 经验事实，逻辑自洽但缺来源支持（来源 [1]-[4] 均与具体驱动版本性能差异无关）

## Search Query

NVIDIA driver 535 vs 550 RTX 4090 INT8 inference performance benchmark

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
- {'url': 'https://www.nvidia.com/en-us/', 'type': 'bing', 'title': 'World Leader in Artificial Intelligence Computing | NVIDIA'}
- {'url': 'https://www.nvidia.com/en-us/drivers/', 'type': 'bing', 'title': 'Download The Official NVIDIA Drivers | NVIDIA'}
