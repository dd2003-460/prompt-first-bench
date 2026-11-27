# N280: 框架临时缓冲 (CUDA Context + Workspace) 的固定开销量化：vLLM/TensorRT-LLM 在初始化时分配的 CUDA Contex

- **status**: verified
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

先验知识/题面给定，逻辑校验通过
