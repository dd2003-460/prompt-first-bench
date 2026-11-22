# N361: FP8 KV Cache 与 INT4 权重的兼容性开销：在主流推理引擎 (vLLM/TensorRT-LLM) 中，混合精度 (INT4 权重 + FP8 K

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N150

## Claim

FP8 KV Cache 与 INT4 权重的兼容性开销：在主流推理引擎 (vLLM/TensorRT-LLM) 中，混合精度 (INT4 权重 + FP8 KV) 通常无需额外显存开销用于反量化缓存，因为 KV Cache 独立存储；但需确认引擎支持该混合模式，若不支持则需将 KV Cache 提升至 BF16，导致显存占用回升至 8.59GB，抵消 FP8 KV 的节省。

## Corrected Claim

在主流推理引擎中，混合精度（INT4 权重 + FP8 KV）通常无需额外显存开销用于反量化缓存，因为 KV Cache 独立存储；但需确认引擎支持该混合模式，若不支持则需将 KV Cache 提升至更高精度（如 BF16），导致显存占用回升，抵消 FP8 KV 的节省。

## Evidence

[质询]该陈述包含具体的经验性参数（如8.59GB显存占用）和特定引擎的行为断言（vLLM/TensorRT-LLM对混合精度的具体支持情况及回退机制），属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM TensorRT-LLM mixed precision INT4 weights FP8 KV cache support
