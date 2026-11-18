# N235: vLLM 与 llama.cpp 在 RTX 4090 上运行 27B INT8 的吞吐量差异主要源于内存管理策略：vLLM 使用 PagedAttention

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

vLLM 与 llama.cpp 在 RTX 4090 上运行 27B INT8 的吞吐量差异主要源于内存管理策略：vLLM 使用 PagedAttention 减少内存碎片但引入 CPU-GPU 同步开销，llama.cpp 使用连续内存分配但支持更灵活的量化内核 (如 GGUF Q8_0 vs Q8_1)，实测差异通常在 10-30% 之间，具体取决于 Batch Size 和序列长度。

## Corrected Claim

vLLM 与 llama.cpp 在 RTX 4090 上运行 27B INT8 的吞吐量存在差异，主要源于内存管理策略（vLLM 的 PagedAttention vs llama.cpp 的连续内存/量化内核优化），具体差异幅度取决于 Batch Size 和序列长度，但缺乏统一的标准数值范围。

## Evidence

[质询]陈述包含具体的经验数值断言（吞吐量差异 10-30%）和特定的技术实现细节（如 llama.cpp 使用连续内存分配、vLLM 引入 CPU-GPU 同步开销），这些属于经验事实，无法从第一性原理推导，且参考来源中完全缺失相关数据支持。 | 逻辑上自洽（内存管理策略差异确实会导致性能差异），但参考来源 [1]-[3] 均与 vLLM/llama.cpp 性能对比无关，属于经验事实且缺乏来源支持，故降级。

## Search Query

vLLM vs llama.cpp RTX 4090 27B INT8 throughput comparison

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
