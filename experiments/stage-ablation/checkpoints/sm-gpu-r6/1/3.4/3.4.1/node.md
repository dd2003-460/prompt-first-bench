# N50: vLLM 在 AMD ROCm 环境下运行 Qwen3-27B (BF16) 的实测吞吐 (tokens/s) 相比同代 NVIDIA CUDA 环境 (如 R

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

vLLM 在 AMD ROCm 环境下运行 Qwen3-27B (BF16) 的实测吞吐 (tokens/s) 相比同代 NVIDIA CUDA 环境 (如 RTX 4090) 的具体性能损耗百分比及关键瓶颈 (kernel launch overhead vs memory bandwidth)

## Corrected Claim

vLLM 在 AMD ROCm 环境下运行 Qwen3-27B (BF16) 的实测吞吐相比同代 NVIDIA CUDA 环境存在性能差异，具体损耗百分比及关键瓶颈需参考特定硬件组合的基准测试报告，当前来源未提供相关数据。

## Evidence

[质询]该陈述涉及具体的硬件性能对比（AMD ROCm vs NVIDIA CUDA）及特定模型（Qwen3-27B）的实测数据，属于经验事实。参考来源仅提供了RTX 4060的功耗信息，完全未覆盖RTX 4090、AMD GPU、vLLM或Qwen3-27B的相关性能数据，无法验证具体的损耗百分比和瓶颈归因。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅涉及RTX 4060规格，与事实主题无关）

## Search Query

vLLM ROCm vs CUDA performance benchmark Qwen 27B tokens per second latency overhead

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
