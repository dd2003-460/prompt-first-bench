# N169: 推理框架运行时显存开销 (Runtime Overhead)：除模型权重外，vLLM/TensorRT-LLM 等框架需分配 CUDA Context, Ker

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

推理框架运行时显存开销 (Runtime Overhead)：除模型权重外，vLLM/TensorRT-LLM 等框架需分配 CUDA Context, Kernel 编译缓存, 以及临时激活内存。通常额外占用 0.5 - 1.5 GB 显存，需从总显存中预留。

## Corrected Claim

推理框架运行时显存开销 (Runtime Overhead)：除模型权重外，vLLM/TensorRT-LLM 等框架需分配 CUDA Context, Kernel 编译缓存, 以及临时激活内存。通常额外占用 0.5 - 1.5 GB 显存，需从总显存中预留。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM runtime memory overhead CUDA context size
