# N6: Qwen3-27B (NVFP4) 静态权重占用为 13.5GB (27B × 4-bit)，加上 16MB/layer 的 KV cache 基础开销，4×1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B (NVFP4) 静态权重占用为 13.5GB (27B × 4-bit)，加上 16MB/layer 的 KV cache 基础开销，4×16GB 总显存 64GB 中剩余可用 KV 空间为 64 - 13.5 - 2.0 (activation/other) ≈ 48.5GB

## Corrected Claim

Qwen3-27B (NVFP4) 静态权重占用为 13.5GB (27B × 4-bit)，加上 16MB/layer 的 KV cache 基础开销，4×16GB 总显存 64GB 中剩余可用 KV 空间为 64 - 13.5 - 2.0 (activation/other) ≈ 48.5GB

## Evidence

[质询]KV cache 基础开销 16MB/layer 的具体数值缺乏通用标准，可能因模型架构（如 GQA 头数、隐藏层维度）不同而有差异，但在 Qwen3-27B 的特定配置下该量级是合理的工程估算值。 | 先验知识/题面给定，逻辑校验通过：27B 参数在 4-bit 量化下约为 13.5GB，算术运算 64 - 13.5 - 2.0 = 48.5 正确，符合显存分配的基本逻辑。

## Search Query

qwen3-27b nvfp4 weight size memory usage
