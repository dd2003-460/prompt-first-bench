# N14: 推理框架开销（Overhead）估算：包括CUDA上下文、算子工作区、激活值峰值等，通常占额外2-4GB显存；对于27B模型，建议预留总显存的10-15%作为安

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

推理框架开销（Overhead）估算：包括CUDA上下文、算子工作区、激活值峰值等，通常占额外2-4GB显存；对于27B模型，建议预留总显存的10-15%作为安全余量，即Minimum_VRAM = Memory_Weights + Memory_KV + 0.15 * (Memory_Weights + Memory_KV)

## Corrected Claim

推理框架开销（Overhead）估算：包括CUDA上下文、算子工作区、激活值峰值等，通常占额外2-4GB显存；对于27B模型，建议预留总显存的10-15%作为安全余量，即Minimum_VRAM = Memory_Weights + Memory_KV + 0.15 * (Memory_Weights + Memory_KV)

## Evidence

先验知识/题面给定，逻辑校验通过
