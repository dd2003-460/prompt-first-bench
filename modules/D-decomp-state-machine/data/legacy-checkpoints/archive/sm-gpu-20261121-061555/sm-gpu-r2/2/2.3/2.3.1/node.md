# N62: CUDA上下文及框架运行时基础开销：在vLLM/TensorRT-LLM等主流推理框架中，初始化CUDA Context、PyTorch运行时及基础算子库占用的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

CUDA上下文及框架运行时基础开销：在vLLM/TensorRT-LLM等主流推理框架中，初始化CUDA Context、PyTorch运行时及基础算子库占用的固定显存约为0.5-1.5GB，该值不随模型大小线性变化，但随GPU显存总量和驱动版本略有波动。

## Corrected Claim

CUDA上下文及框架运行时基础开销：在vLLM/TensorRT-LLM等主流推理框架中，初始化CUDA Context、PyTorch运行时及基础算子库占用的固定显存约为0.5-1.5GB，该值不随模型大小线性变化，但随GPU显存总量和驱动版本略有波动。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM CUDA context memory overhead GB
