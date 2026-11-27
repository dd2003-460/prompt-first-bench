# N280: 框架临时缓冲 (CUDA Context + Workspace) 的固定开销量化：vLLM/TensorRT-LLM 在初始化时分配的 CUDA Contex

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

框架临时缓冲 (CUDA Context + Workspace) 的固定开销量化：vLLM/TensorRT-LLM 在初始化时分配的 CUDA Context 和 Workspace 缓冲通常为 0.5-1.5GB，取决于显存大小和框架版本。此开销与模型大小和序列长度无关，是固定常数。在 24GB 显存中，此开销占 2-6%，不可忽略。若使用 PagedAttention，KV Cache 碎片开销降低，但 Workspace 开销保持不变。

## Corrected Claim

框架临时缓冲 (CUDA Context + Workspace) 的固定开销量化：vLLM/TensorRT-LLM 在初始化时分配的 CUDA Context 和 Workspace 缓冲通常为 0.5-1.5GB，取决于显存大小和框架版本。此开销与模型大小和序列长度无关，是固定常数。在 24GB 显存中，此开销占 2-6%，不可忽略。若使用 PagedAttention，KV Cache 碎片开销降低，但 Workspace 开销保持不变。

## Evidence

父节点级核验未通过：不完备（父节点明确讨论的是‘框架临时缓冲 (CUDA Context + Workspace)’的固定开销，强调其与模型大小、序列长度无关且为常数。然而，唯一的子节点讨论的是‘Attention 层激活峰值’（Activation Memory），这属于推理过程中的动态内存占用，且明确取决于层数、维度等模型结构参数，甚至提到了 Flash Attention 对 S=QK^T 矩阵存储的影响。子节点的内容完全偏离了父节点关于‘固定框架开销’的主题，未能覆盖父节点的核心内容（如 CUDA Context 具体大小、Workspace 分配机制、PagedAttention 对 KV Cache 碎片的影响等），反而引入了一个新的、不相关的主题（激活内存）。因此，虽然只有一个子节点不存在内部正交性问题（trivially true），但其内容未能覆盖父节点的关键方面，导致分解不完备且主题不匹配。）
