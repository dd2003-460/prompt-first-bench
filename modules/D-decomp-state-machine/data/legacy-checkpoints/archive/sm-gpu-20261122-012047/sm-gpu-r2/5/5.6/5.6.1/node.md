# N153: TensorRT-LLM 8.0+ 对 Qwen3-27B 的推理优化包括 FP8 量化加速和 KV Cache 压缩，相比 vLLM 可提升吞吐量 20-30

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

TensorRT-LLM 8.0+ 对 Qwen3-27B 的推理优化包括 FP8 量化加速和 KV Cache 压缩，相比 vLLM 可提升吞吐量 20-30%，但仅支持 NVIDIA 硬件，AMD 和 Apple 平台无法使用此优化。

## Corrected Claim

TensorRT-LLM 对 Qwen3-27B 的推理优化通常包括 FP8 量化加速和 KV Cache 压缩，相比 vLLM 在特定 NVIDIA 硬件上可提升吞吐量，但仅支持 NVIDIA 硬件，AMD 和 Apple 平台无法使用此优化。

## Evidence

[质询]具体版本号（8.0+）及特定模型（Qwen3-27B）的性能提升幅度（20-30%）属于经验事实，缺乏通用性，且TensorRT-LLM对Qwen3的支持情况随版本快速迭代，具体数值可能因硬件配置和测试场景而异，存在夸大或过时风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

TensorRT-LLM 8.0 Qwen3-27B inference optimization FP8 KV cache compression
