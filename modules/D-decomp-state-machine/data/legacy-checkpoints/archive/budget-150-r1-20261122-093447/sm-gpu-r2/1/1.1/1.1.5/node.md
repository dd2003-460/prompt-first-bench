# N50: Runtime_Overhead_MB 的组成部分：包括 CUDA Context (通常 0.5-1GB), cuDNN/CUDA 库加载, 框架内部数据结构

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Runtime_Overhead_MB 的组成部分：包括 CUDA Context (通常 0.5-1GB), cuDNN/CUDA 库加载, 框架内部数据结构 (如 PyTorch 的 Tensor 对象头), 以及推理引擎 (vLLM/TensorRT) 的调度器和缓存池预分配。

## Corrected Claim

Runtime_Overhead_MB 的组成部分：包括 CUDA Context (通常 0.5-1GB), cuDNN/CUDA 库加载, 框架内部数据结构 (如 PyTorch 的 Tensor 对象头), 以及推理引擎 (vLLM/TensorRT) 的调度器和缓存池预分配。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory overhead LLM inference
