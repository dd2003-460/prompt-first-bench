# N42: 显存碎片与运行时开销 (C_overhead_runtime) 通常占总显存需求的 5-10%，包括 CUDA 上下文、临时缓冲区及内存对齐损耗，需从可用显存中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

显存碎片与运行时开销 (C_overhead_runtime) 通常占总显存需求的 5-10%，包括 CUDA 上下文、临时缓冲区及内存对齐损耗，需从可用显存中预留。

## Corrected Claim

显存碎片与运行时开销 (C_overhead_runtime) 通常占总显存需求的 5-10%，包括 CUDA 上下文、临时缓冲区及内存对齐损耗，需从可用显存中预留。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU memory fragmentation overhead LLM inference vLLM
