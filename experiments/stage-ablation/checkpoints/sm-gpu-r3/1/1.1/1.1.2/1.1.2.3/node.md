# N143: CUDA 上下文及运行时开销：PyTorch/CUDA 初始化、算子缓存等固定开销通常在 0.5-1.5 GB 之间，该部分与模型大小无关，但在显存紧张时（如 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

CUDA 上下文及运行时开销：PyTorch/CUDA 初始化、算子缓存等固定开销通常在 0.5-1.5 GB 之间，该部分与模型大小无关，但在显存紧张时（如 RTX 4090 24GB）需从总预算中明确扣除

## Corrected Claim

CUDA 上下文及运行时开销：PyTorch/CUDA 初始化、算子缓存等固定开销通常在 0.5-1.5 GB 之间，该部分与模型大小无关，但在显存紧张时（如 RTX 4090 24GB）需从总预算中明确扣除

## Evidence

先验知识/题面给定，逻辑校验通过
