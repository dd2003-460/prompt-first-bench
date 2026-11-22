# N54: 推理框架额外开销的总预留建议：对于 32K 长上下文推理，建议预留 4-6 GB 显存给非权重/非KV 开销（CUDA Context 2GB + Activa

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

推理框架额外开销的总预留建议：对于 32K 长上下文推理，建议预留 4-6 GB 显存给非权重/非KV 开销（CUDA Context 2GB + Activations 2-4GB），而非 N9 中提到的 2.5-5GB 的宽泛范围。具体值需根据实际框架 (vLLM vs llama.cpp) 和 GPU 型号 (Hopper vs Ampere) 微调，Hopper 架构因 FP8 支持可能减少 Activation 精度从而降低开销。

## Corrected Claim

推理框架额外开销的总预留建议：对于 32K 长上下文推理，建议预留 4-6 GB 显存给非权重/非KV 开销（CUDA Context 2GB + Activations 2-4GB），而非 N9 中提到的 2.5-5GB 的宽泛范围。具体值需根据实际框架 (vLLM vs llama.cpp) 和 GPU 型号 (Hopper vs Ampere) 微调，Hopper 架构因 FP8 支持可能减少 Activation 精度从而降低开销。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对不同的硬件（RTX 4090/Ampere）和软件栈（vLLM/TensorRT-LLM）提供了具体的量化推导，两者在场景上互斥且互补，覆盖了父节点关于‘具体值需根据框架和GPU微调’的核心要求。虽然结构相似，但属于针对不同变量的具体实例化，而非简单的参数重复，因此不构成冗余。）
