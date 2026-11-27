# N158: TensorRT-LLM 目前仅支持 NVIDIA GPU，不支持 AMD GPU。在 AMD 上需使用 vLLM 或 SGLang，这些框架支持 FP8/IN

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

TensorRT-LLM 目前仅支持 NVIDIA GPU，不支持 AMD GPU。在 AMD 上需使用 vLLM 或 SGLang，这些框架支持 FP8/INT8 量化，但性能可能低于 TensorRT-LLM 在 NVIDIA 上的优化版本

## Corrected Claim

TensorRT-LLM 目前仅支持 NVIDIA GPU，不支持 AMD GPU。在 AMD 上需使用 vLLM 或 SGLang，这些框架支持 FP8/INT8 量化，但性能可能低于 TensorRT-LLM 在 NVIDIA 上的优化版本

## Evidence

先验知识/题面给定，逻辑校验通过
