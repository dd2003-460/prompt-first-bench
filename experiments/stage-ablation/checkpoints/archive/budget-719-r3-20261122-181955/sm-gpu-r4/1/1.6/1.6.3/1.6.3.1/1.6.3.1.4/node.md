# N611: AMX 的主要优势在于降低每 token 的 CPU 占用率，允许更高的并发 Batch Size，这一结论需量化：在相同硬件上，使用 AMX 优化后，单核可支

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N215

## Claim

AMX 的主要优势在于降低每 token 的 CPU 占用率，允许更高的并发 Batch Size，这一结论需量化：在相同硬件上，使用 AMX 优化后，单核可支持的并发请求数（Batch Size）相比 AVX-512 提升约 2-3 倍，因为 AMX 减少了每 token 的指令数（IPC 提升）和内存访问次数。

## Corrected Claim

AMX 的主要优势在于降低每 token 的 CPU 占用率，允许更高的并发 Batch Size。在计算密集型场景下，相比 AVX-512，AMX 通过减少指令数和内存访问次数，可显著提升单核吞吐量，从而支持更高的并发请求数，但具体提升倍数取决于硬件瓶颈和负载特征。

## Evidence

[质询]具体数值（2-3倍）缺乏来源支持，且AMX对Batch Size的提升幅度高度依赖模型架构、序列长度及内存带宽瓶颈，并非固定常数；此外，AMX主要优化计算密集型部分，若系统受限于内存带宽或调度开销，IPC提升未必线性转化为并发数提升。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

AMX CPU inference batch size concurrency improvement
