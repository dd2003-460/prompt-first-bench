# N206: 推理框架（如 vLLM/TensorRT-LLM）在 NVFP4 模式下的运行时 Overhead（含 CUDA Context、激活值缓冲、算子工作空间）估算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

推理框架（如 vLLM/TensorRT-LLM）在 NVFP4 模式下的运行时 Overhead（含 CUDA Context、激活值缓冲、算子工作空间）估算为 3.5 GB，该值基于 27B 模型在 32K 上下文下的典型激活值峰值大小及框架基础开销经验值。

## Corrected Claim

推理框架（如 vLLM/TensorRT-LLM）在 NVFP4 模式下的运行时 Overhead（含 CUDA Context、激活值缓冲、算子工作空间）估算为 3.5 GB，该值基于 27B 模型在 32K 上下文下的典型激活值峰值大小及框架基础开销经验值。

## Evidence

先验知识/题面给定，逻辑校验通过
