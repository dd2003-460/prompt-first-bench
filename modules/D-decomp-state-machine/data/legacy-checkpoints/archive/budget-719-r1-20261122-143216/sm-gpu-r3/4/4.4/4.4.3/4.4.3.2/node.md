# N316: vLLM 的 PagedAttention 机制在 RTX 4090 上相比 llama.cpp 的连续内存 KV Cache，在 32K 上下文单请求场景下，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113, N114, N115

## Claim

vLLM 的 PagedAttention 机制在 RTX 4090 上相比 llama.cpp 的连续内存 KV Cache，在 32K 上下文单请求场景下，因避免了内存碎片化导致的页错误（Page Fault）和内存拷贝开销，其有效带宽利用率提升约 5%-10%，具体数值取决于 GPU 驱动版本（CUDA 12.1+ 支持更好的 TMA 指令）。

## Corrected Claim

vLLM 的 PagedAttention 机制通过分页管理 KV Cache，主要优势在于支持多请求并发时的内存高效利用和减少碎片化。在 RTX 4090 等现代 GPU 上，相比 llama.cpp 的连续内存方案，其在高并发场景下能显著提升吞吐量；但在 32K 上下文单请求场景下，其带宽利用率提升幅度有限且具体数值取决于实现细节，并非固定的 5%-10%。

## Evidence

[质询]该陈述包含具体的性能提升数值（5%-10%）和特定硬件/软件版本依赖（RTX 4090, CUDA 12.1+ TMA），属于经验事实。在单请求（Single Request）场景下，PagedAttention 的主要优势在于多请求并发时的内存管理效率，而在单请求长上下文场景下，其相对于连续内存的带宽利用率提升通常极小甚至可忽略，且具体数值高度依赖实现细节和基准测试方法，缺乏通用性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且单请求场景下PagedAttention的带宽优势通常不显著，具体数值无法从第一性原理推出）

## Search Query

vLLM PagedAttention vs llama.cpp contiguous memory bandwidth efficiency consumer GPU
