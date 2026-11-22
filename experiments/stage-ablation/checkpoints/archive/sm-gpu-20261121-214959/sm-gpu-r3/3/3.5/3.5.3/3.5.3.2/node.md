# N237: Llama.cpp 在 Apple Silicon 上默认采用连续内存分配（Contiguous Allocation），其 KV Cache 内存碎片率（Fr

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86

## Claim

Llama.cpp 在 Apple Silicon 上默认采用连续内存分配（Contiguous Allocation），其 KV Cache 内存碎片率（Fragmentation Rate）在 32K 上下文、Batch Size=1 时约为 5-10%，但在高并发或动态长度下可升至 20-30%；相比之下，MLX 的 PagedAttention 实现（若可用）或 vLLM 的块式管理可将碎片率控制在 <2%，直接决定可用显存上限。

## Corrected Claim

Llama.cpp在Apple Silicon上通常采用连续内存分配策略，其KV Cache内存碎片率随上下文长度和并发量增加而上升；相比之下，采用PagedAttention或块式管理的框架（如vLLM）通常能更有效地控制内存碎片，从而提升可用显存利用率。

## Evidence

[质询]具体数值（5-10%、20-30%、<2%）缺乏公开基准测试支持，且Llama.cpp在Apple Silicon上默认是否严格采用'连续内存分配'而非其他优化策略存在技术细节争议，MLX的PagedAttention实现状态及具体碎片率数据亦无权威来源佐证。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

llama.cpp apple silicon memory fragmentation rate KV cache contiguous allocation vs paged attention
