# N42: 框架运行时基础开销：CUDA/ROCm 上下文、cuBLAS 工作区、以及框架内部对象（如 PyTorch 张量元数据）的固定显存占用。在 RTX 4090/5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

框架运行时基础开销：CUDA/ROCm 上下文、cuBLAS 工作区、以及框架内部对象（如 PyTorch 张量元数据）的固定显存占用。在 RTX 4090/5090 上，CUDA 上下文初始化通常占用 200-500MB；llama.cpp 的 C++ 运行时开销低于 PyTorch 栈，可能仅 50-100MB。需区分不同推理后端（llama.cpp vs vLLM）的固定开销差异。

## Corrected Claim

框架运行时基础开销：CUDA/ROCm 上下文、cuBLAS 工作区、以及框架内部对象（如 PyTorch 张量元数据）的固定显存占用。在 RTX 4090/5090 上，CUDA 上下文初始化通常占用 200-500MB；llama.cpp 的 C++ 运行时开销低于 PyTorch 栈，可能仅 50-100MB。需区分不同推理后端（llama.cpp vs vLLM）的固定开销差异。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory footprint vLLM llama.cpp fixed overhead GB
