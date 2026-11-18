# N50: vLLM 在 AMD ROCm 环境下运行 Qwen3-27B (BF16) 的实测吞吐 (tokens/s) 相比同代 NVIDIA CUDA 环境 (如 R

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

vLLM 在 AMD ROCm 环境下运行 Qwen3-27B (BF16) 的实测吞吐 (tokens/s) 相比同代 NVIDIA CUDA 环境 (如 RTX 4090) 的具体性能损耗百分比及关键瓶颈 (kernel launch overhead vs memory bandwidth)

## Corrected Claim

vLLM 在 AMD ROCm 环境下运行 Qwen3-27B (BF16) 的性能通常低于同代 NVIDIA CUDA 环境，具体损耗百分比取决于 AMD GPU 型号及驱动优化程度，主要瓶颈可能涉及 kernel launch overhead 或 memory bandwidth，但缺乏统一的具体实测数据支持。

## Evidence

[质询]该陈述询问具体的实测吞吐损耗百分比及瓶颈，属于高度依赖具体硬件型号（AMD具体GPU型号未指定，仅说ROCm环境）、软件版本及测试条件的经验事实，且参考来源中完全缺失相关数据，无法验证具体数值。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2][3]均与vLLM在AMD/NVIDIA上的具体性能对比无关）

## Search Query

vLLM ROCm vs CUDA performance benchmark Qwen 27B tokens per second latency overhead

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
