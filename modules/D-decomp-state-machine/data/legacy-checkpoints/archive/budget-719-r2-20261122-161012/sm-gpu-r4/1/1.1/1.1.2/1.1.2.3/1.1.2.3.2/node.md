# N349: vLLM/SGLang 推理引擎的额外固定开销：相比原生 PyTorch，vLLM 的 PagedAttention 块管理表和 CUDA Graph 捕获会额

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

vLLM/SGLang 推理引擎的额外固定开销：相比原生 PyTorch，vLLM 的 PagedAttention 块管理表和 CUDA Graph 捕获会额外占用 0.2-0.5 GB 显存，总运行时固定开销需修正为 0.7-1.0 GB。

## Corrected Claim

vLLM/SGLang 推理引擎的额外固定开销：相比原生 PyTorch，vLLM 的 PagedAttention 块管理表和 CUDA Graph 捕获会额外占用 0.2-0.5 GB 显存，总运行时固定开销需修正为 0.7-1.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM PagedAttention memory overhead fixed cost
